'''
Created on Mar 30, 2014

@author: ajr
'''

from ....models import Sym
from ....etree import etree
from ...config import MATHML_NS

class CPlus(Sym):
    _symbolCd = 'arith1'
    _symbolName = 'plus'
    url = MATHML_NS + '::' + _symbolName
    
    def __call__(self, *args):
        cls = args[0].__class__
        return cls(sum([it.num for it in args]))
    
    @classmethod
    def from_cmathml(cls, tree):
        return cls(cls.url)
    
    @property
    def cmathml(self):
        tag = '{' + MATHML_NS + '}' + self._symbolName
        return etree.Element(tag)
