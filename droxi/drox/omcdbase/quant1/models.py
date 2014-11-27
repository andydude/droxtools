'''
Created on Mar 31, 2014

@author: ajr
'''

from ..models import OMSym

@OMSym.called("quant1", "exists")
class Exists(OMSym):
    pass

@OMSym.called("quant1", "forall")
class ForAll(OMSym):
    pass
