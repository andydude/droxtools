'''
Created on Mar 31, 2014

@author: ajr
'''

from ..models import OMSym

@OMSym.called("list1", "list")
class OMList(OMSym):
    pass
