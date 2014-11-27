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

import importlib

from .config import DEBUG
from .models import Sym
from .etree import etree

class BuiltinResolver(object):
    def __init__(self, cdbase=None, package=None):
        self.cdbase = cdbase
        self.package = package

    def __call__(self, sym):
        if not isinstance(sym, Sym):
            raise ValueError, sym
        
        _, cd, name = sym.omsym
        module_name = '.'.join([self.package, cd, '_mapping'])
        if DEBUG: print("module_name = " + module_name)
        DictCls = importlib.import_module(module_name)
        
        if hasattr(DictCls, '_namespace_mapping'): # preferred
            ElemCls = getattr(DictCls._namespace_mapping, name)
        elif hasattr(DictCls, '__content_dictionary_mapping__'): # legacy (yesterday)
            ElemCls = DictCls.__content_dictionary_mapping__[name]
        else:
            ElemCls = getattr(DictCls, name)
#         if hasattr(DictCls, '__content_dictionary_mapping__'):
#             ElemCls = DictCls.__content_dictionary_mapping__[name]
#         else:
#             ElemCls = getattr(DictCls, name)
        url = self.cdbase + '/' + cd + '#' + name
        ast = ElemCls(url)
        return ast

class BuiltinReader(object):
    def __init__(self, ns=None, package=None):
        self.package = package
        self.ns = ns

    def __call__(self, sym, tree):
        if not etree.iselement(tree):
            raise ValueError, tree
        
        ns, name = Sym.from_etree(tree.tag).xmlns
        if ns != self.ns:
            raise ValueError, ns
        
        module_name = '.'.join([self.package, '_mapping'])
        if DEBUG: print("module_name = " + module_name)
        DictCls = importlib.import_module(module_name)
        
        if hasattr(DictCls, '_namespace_mapping'): # preferred
            ElemCls = getattr(DictCls._namespace_mapping, name)
        elif hasattr(DictCls, '__content_dictionary_mapping__'): # legacy (yesterday)
            ElemCls = DictCls.__content_dictionary_mapping__[name]
        else:
            ElemCls = getattr(DictCls, name)
    
        ast = ElemCls.from_cmathml(tree)
        return ast

class BuiltinWriter(object):
    def __init__(self):
        pass
    
    def __call__(self, ast):
        try:
            tree =  ast.__tree__() # preferred
            return tree
        except Exception as err:
            try:
                tree =  ast.cmathml # legacy (yesterday)
                return tree
            except Exception as err:
                print("cought exception in Writer" + repr(err))
                raise

        raise NotImplementedError
