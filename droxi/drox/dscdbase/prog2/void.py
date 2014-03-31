'''
Created on Mar 31, 2014

@author: ajr
'''

from ...etree import etree
from ...models import Sym
from ..config import DROSOFT_CDBASE

class DVoid(Sym):
    _symbolCdbase = DROSOFT_CDBASE
    _symbolCd = 'prog2'
    _symbolName = 'void'
    url = _symbolCdbase + '/' + _symbolCd + '#' + _symbolName
    
    def __init__(self):
        Sym.__init__(self, DVoid.url)

    def __call__(self, *args):
        return self
        
    def __eval__(self):
        return self
    
#     def __tree__(self):
#         return self.cmathml_element
#         #return self # etree.Comment(" void ")
