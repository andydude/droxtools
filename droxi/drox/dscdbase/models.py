'''
Created on Mar 31, 2014

@author: ajr
'''

from ..models import Sym
from .config import DROSOFT_CDBASE

class DSSym(Sym):
    _symbolCdbase = DROSOFT_CDBASE

    @classmethod
    def called(cls, cd, name):
        def decorator(obj):
            obj._symbolCdbase = DSSym._symbolCdbase
            obj._symbolCd = cd
            obj._symbolName = name
            obj.url = DSSym._symbolCdbase + '/' + cd + '#' + name
            return obj
        return decorator
