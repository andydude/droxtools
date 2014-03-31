'''
Created on Mar 30, 2014

@author: ajr
'''

import importlib

from ..etree import etree
from ..models import Sym
from .config import DROSOFT_CDBASE

class Resolver(object):
    def __init__(self):
        pass

    def __call__(self, sym):
        if not isinstance(sym, Sym):
            raise ValueError, sym
        
        cdbase, cd, name = sym.omsym
        if cdbase != DROSOFT_CDBASE:
            #raise ValueError, cdbase
            cdbase = DROSOFT_CDBASE
    
        DictCls = importlib.import_module(__package__ + '.' + cd + '._mapping')
        if hasattr(DictCls, '__content_dictionary_mapping__'):
            ElemCls = DictCls.__content_dictionary_mapping__[name]
        else:
            ElemCls = getattr(DictCls, name)
        url = cdbase + '/' + cd + '#' + name
        ast = ElemCls(url)
        return ast
