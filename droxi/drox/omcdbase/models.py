'''
Created on Mar 31, 2014

@author: ajr
'''

from ..models import Sym
from .config import OPENMATH_CDBASE

class OMSym(Sym):
    _symbolCdbase = OPENMATH_CDBASE

    @classmethod
    def called(cls, cd, name):
        def decorator(obj):
            obj._symbolCdbase = OPENMATH_CDBASE
            obj._symbolCd = cd
            obj._symbolName = name
            obj.url = OMSym._symbolCdbase + '/' + cd + '#' + name
            return obj
        return decorator
