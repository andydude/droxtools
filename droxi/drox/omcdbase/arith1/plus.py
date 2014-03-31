'''
Created on Mar 30, 2014

@author: ajr
'''

from ...models import Sym, Number

class OMPlus(Sym):
    _symbolCd = 'arith1'
    _symbolName = 'plus'
    url = Sym._symbolCdbase + '/' + _symbolCd + '#' + _symbolName
    
    def __call__(self, *args):
        cls = Number.result_type(*args)
        return cls(sum([it.num for it in args]))
