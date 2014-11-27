'''
Created on Mar 31, 2014

@author: ajr
'''

from ..models import OMSym

@OMSym.called("minmax1", "max")
class Max(OMSym):
    pass

@OMSym.called("minmax1", "min")
class Min(OMSym):
    pass
