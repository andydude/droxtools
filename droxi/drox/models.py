#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# droxi
# Copyright (c) 2014, Andrew Robbins, All rights reserved.
# 
# This library ("it") is free software; it is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; you can redistribute it and/or modify it under the terms of the
# GNU Lesser General Public License ("LGPLv3") <https://www.gnu.org/licenses/lgpl.html>.
from __future__ import absolute_import

from .m.config import MATHML_NS
from .omcdbase.config import OPENMATH_CDBASE
from .om.config import OPENMATH_NS
from .etree import etree

class Id(object):
    """
    Represents an abstract identifier.
    """
    def __init__(self):
        raise NotImplementedError

class Op(Id):
    """
    Represents an operator.
    """

    def __init__(self, oper, url=None):
        """
        Constructs an operator.
        """
        self.url = url
        self.oper = oper

class Sym(Id):
    """
    Represents a symbol.
    """

    def __init__(self, url):
        """
        Constructs a symbol.
        """
        self.url = url

    def __tree__(self):
        return self.cmathml

    def __eval__(self, env):
        return self
    
    def __call__(self, *args):
        return NotImplemented

    @staticmethod
    def resolve(sym, tree=None):
        import importlib
        from .config import BUILTIN_CD, BUILTIN_NS
        exp = None
        
        if '::' in sym.url:
            ns = sym.xmlns[0]
            prefix = None
            for prefix2, ns2 in BUILTIN_NS.items():
                if ns == ns2:
                    prefix = prefix2
            module_name = 'drox.' + prefix + '.reader'
            #print("module_name = " + module_name)
            lib = importlib.import_module(module_name)
            exp = lib.Reader()(sym, tree)
        else:
            cdbase = sym.omsym[0]
            prefix = None
            lib = None
            
            for prefix2, cdbase2 in BUILTIN_CD.items():
                try:
                    prefix = prefix2
                    module_name = 'drox.' + prefix + '.resolver'
                    #print("module_name = " + module_name)
                    lib = importlib.import_module(module_name)
                    exp = lib.Resolver()(sym)
                except ImportError:
                    pass
                else:
                    break
            
            if not lib:
                raise NotImplementedError
            
        return exp
    
    @classmethod
    def from_url(cls, url):
        """
        Converts a URL into a symbol, same as Sym(url).
        """
        return cls(url)

    @classmethod
    def from_etree(cls, tag_str):
        """
        Converts an ElementTree tag string into a valid URL.
        """
        if tag_str[0] != '{':
            raise ValueError, tag_str
        
        ns, name = tag_str[1:].rsplit('}', 1)
        return cls.from_xmlns(ns, name)

    @property
    def etree(self):
        """
        Converts a URL into an ElementTree tag string.
        """
        ns, name = self.xmlns
        tag_str = '{' + ns + '}' + name
        return tag_str

    @classmethod
    def from_xmlns(cls, ns, name):
        """
        Converts an XML Namespaced element name into a URL, 
        according to the algorithm specified in ECMA-357,
        "E4X" section 13.3.4.2 QName.prototype.toString(),
        which says that:

            uri :: localName

        is the string representation of this QName object.
        
        Not mentioned in ECMA-357 is that it is a valid URL.
        """
        url = ns + '::' + name
        return cls(url)

    @property
    def xmlns(self):
        """
        Converts a URL into an XML Namespace element.
        """
        if '::' in self.url:
            return self.url.rsplit('::', 1)
        if '#' in self.url:
            ns, name = self.url.rsplit('#', 1)
            return ns+'#', name
        if '/' in self.url:
            ns, name = self.url.rsplit('/', 1)
            return ns+'/', name
        return None

    @classmethod
    def from_omsym(cls, cdbase, cd, name):
        """
        Converts an OpenMath/MathML symbol into a URL,
        according to the OpenMath 2.0 standard
        """
        url = cdbase + '/' + cd + '#' + name
        return cls(url)

    @property
    def omsym(self):
        """
        Converts a URL into an OpenMath/MathML symbol.
        """
        if '::' in self.url:
            ns, name = self.url.rsplit('::', 1)
            return ns, '::', name
        if '#' not in self.url:
            return None
        ns, name = self.url.rsplit('#', 1)
        if '/' not in ns:
            return None
        cdbase, cd = ns.rsplit('/', 1)
        return cdbase, cd, name

    @classmethod
    def from_cmathml(cls, tree):
        name = tree.tag.rsplit('}')[1]
        if name == 'csymbol':
            sym = cls.from_cmathml_symbol(tree)
            return Sym.resolve(sym)
        else:
            return cls.from_cmathml_element(tree)

    @property
    def cmathml(self):
        if '::' in self.url:
            return self.cmathml_element
        else:
            return self.cmathml_symbol
 
    @classmethod
    def from_cmathml_symbol(cls, tree):
        cdbase = cls._symbolCdbase
        if tree.attrib.has_key('cdbase') and tree.attrib.get('cdbase') != OPENMATH_CDBASE:
            cdbase = tree.attrib['cdbase']
        cd, name = tree.attrib['cd'], tree.text
        return cls.from_omsym(cdbase, cd, name)
    
    @property
    def cmathml_symbol(self):
        tag = '{' + self._contentNs + '}' + self._contentName
        cdbase, cd, name = self.omsym
        
        tree = etree.Element(tag)
        if cdbase != OPENMATH_CDBASE:
            tree.attrib['cdbase'] = cdbase
        tree.attrib['cd'] = cd
        tree.text = name
        return tree

    @classmethod
    def from_cmathml_element(cls, tree):
        return cls.from_etree(tree.tag)
    
    @property
    def cmathml_element(self):
        return etree.Element(self.etree)

    @classmethod
    def from_openmath(cls, tree):
        cdbase = cls._symbolCdbase
        if tree.attrib['cdbase'] != OPENMATH_CDBASE:
            cdbase = tree.attrib['cdbase']
        cd, name = tree.attrib['cd'], tree.attrib['name']
        return cls.from_omsym(cdbase, cd, name)
    
    @property
    def openmath(self):
        tag = '{' + self._openmathNs + '}' + self._openmathName
        cdbase, cd, name = self.omsym
        
        tree = etree.Element(tag)
        if cdbase != OPENMATH_CDBASE:
            tree.attrib['cdbase'] = cdbase
        tree.attrib['cd'] = cd
        tree.attrib['name'] = name
        return tree

    _contentNs = MATHML_NS
    _contentName = 'csymbol'
    
    _openmathNs = OPENMATH_NS
    _openmathName = 'OMS'
    
    _symbolCdbase = OPENMATH_CDBASE
    _symbolCd = None
    _symbolName = None

class Var(Id):
    """
    Represents a variable.
    """
    
    def __init__(self, name, url=None):
        """
        """
        self.url = url
        self.name = name

    @property
    def url(self):
        """
        The URL representation of this object is <_:{self.name}>
        """
        return "_:" + self.name

    @classmethod
    def from_cmathml(cls, tree):
        return cls(cls.url)
    
    @property
    def cmathml(self):
        tag = '{' + self._contentNs + '}' + self._contentName
        tree = etree.Element(tag)
        tree.text = self.name
        return tree
    
    @classmethod
    def from_openmath(cls, tree):
        return cls(cls.url)
    
    @property
    def openmath(self):
        tag = '{' + self._openmathNs + '}' + self._openmathName
        tree = etree.Element(tag)
        tree.attrib['name'] = self.name
        return tree

    _contentNs = MATHML_NS
    _contentName = 'ci'
    
    _openmathNs = OPENMATH_NS
    _openmathName = 'OMV'

class Env(dict):
    def __init__(self):
        pass

class Error(Exception):
    def __init__(self):
        pass

class Lit(Sym):
    def __init__(self):
        pass

class Apply(Sym):
    _contentName = 'apply'
    _openmathName = 'OMA'
    
    def __init__(self, applier, *args):
        self.applier = applier
        self.args = args

class Bind(object):
    pass

class Lambda(Bind):
    pass

class Decl(Apply):
    pass

class Stmt(Apply):
    pass

class Syntax(object):
    pass

class SItem(Syntax):
    pass

class STerm(Syntax):
    pass

class SData(Syntax):
    pass

class DItem(Syntax):
    pass

class DTerm(Syntax):
    pass

class DData(Syntax):
    pass


class Constant(Lit):
    
    @classmethod
    def from_cmathml(cls, tree):
        url = tree.tag
        return cls(url)

    @property
    def cmathml(self):
        tag = self.url
        return etree.Element(tag)

class Boolean(Lit):

    def __init__(self, flag):
        self.flag = flag
    
    @classmethod
    def from_cmathml(cls, tree):
        name = tree.tag[1:].split('}')[1]
        flag = True if name == 'true' else False if name == 'false' else None
        return cls(flag)
    
    @property
    def cmathml(self):
        tag = '{' + MATHML_NS + '}' + str(self.flag).lower()
        return etree.Element(tag)

class Number(Lit):
    _contentName = 'cn'
    
    def __init__(self, num, type='real', base=10):
        self.num = num
        self.type = type
        self.base = base

    def __tree__(self):
        return self.cmathml

    @classmethod
    def from_cmathml(cls, tree):
        mapping = {
            'integer': Integer.from_cmathml,
            'real': Real.from_cmathml,
            'double': Real.from_cmathml,
            'hexdouble': Real.from_hexdouble,
            'e-notation': Real.from_enotation,
        }

        type = tree.attrib.get('type', 'real')
        fn = mapping.get(type, Real.from_cmathml)
        return fn(tree)
    
    @property
    def cmathml(self):
        num = repr(self.num)
        if num.endswith("L"):
            num = num[:-1]
        if 'E' not in num.upper() and '.' in num:
            num = num.rstrip('0').rstrip('.')
        tag = '{' + MATHML_NS + '}' + self._contentName
        type = self.type or 'real'
        #if 'E' not in num.upper() and '.' not in num and type == "real":
        #    type = 'integer'
        attrib = {'type': type or "real"}
        if self.base and self.base != 10:
            attrib['base'] = self.base
        tree = etree.Element(tag, attrib)
        tree.text = num
        return tree
    
    def result_type(self, *args):
        types = map(lambda it: it.type, args)
        
        if filter(lambda it: it != "integer", types) == []:
            return Integer
        
        # TODO: more stuff, like rational, complex
        return Real
        
class Integer(Number):
    _openmathName = 'OMI'
    
    def __init__(self, num, type='integer', base=10):
        self.num = num
        self.type = type
        self.base = base

    @classmethod
    def from_cmathml(cls, tree):
        type = tree.attrib.get('type') or "integer"
        if type != 'integer':
            raise TypeError, type
        base = tree.attrib.get('base')
        base = int(base, 10) if base else 10
        num = int(str(tree.text), base)
        return cls(num, type, base)

class Real(Number):
    _openmathName = 'OMF'

    @classmethod
    def from_cmathml(cls, tree):
        type = tree.attrib.get('type') or "real"
        base = tree.attrib.get('base')
        if base: base = int(base, 10)
        if base and base != 10:
            raise ValueError, base            
        num = float(tree.text)
        if 'E' not in tree.text.upper() and \
            tree.attrib.get('type') is None:
            try:
                text = tree.text
                if 'E' not in text.upper() and '.' in text:
                    text = text.rstrip('0').rstrip('.')
                num2 = int(text, 10)
                return Integer(num2, 'integer')
            except ValueError:
                pass
        return cls(num, type)

    @classmethod
    def from_enotation(cls, tree):
        raise NotImplementedError
        
    @property
    def enotation(self):
        return None

    @classmethod
    def from_hexdouble(cls, tree):
        raise NotImplementedError
        
    @property
    def hexdouble(self):
        return None
