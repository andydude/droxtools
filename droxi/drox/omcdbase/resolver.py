'''
Created on Mar 30, 2014

@author: ajr
'''

import importlib

from ..etree import etree
from ..models import Sym
from .config import OPENMATH_CDBASE

class Resolver(object):
    def __init__(self):
        pass

    def __call__(self, sym):
        if not isinstance(sym, Sym):
            raise ValueError, sym
        
        cdbase, cd, name = sym.omsym
        if cdbase != OPENMATH_CDBASE:
            raise ValueError, cdbase
        
        #print("package = " + __package__)
        DictCls = importlib.import_module(__package__ + '.' + cd + '._mapping')
        ElemCls = getattr(DictCls, name)
        ast = ElemCls(sym.url)
        return ast
