'''
Created on Mar 30, 2014

@author: ajr
'''

from ...models import Sym, Var
from ...omcdbase.config import OPENMATH_CDBASE

class OMSym(Sym):
    _symbolCdbase = OPENMATH_CDBASE
    _symbolCd = None
    _symbolName = None
   
class OMVar(Var):
    pass
