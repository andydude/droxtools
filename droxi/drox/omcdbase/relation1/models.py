'''
Created on Mar 31, 2014

@author: ajr
'''

from ..models import OMSym

@OMSym.called("relation1", "approx")
class Approx(OMSym):
    pass

@OMSym.called("relation1", "eq")
class Eq(OMSym):
    pass

@OMSym.called("relation1", "geq")
class Geq(OMSym):
    pass

@OMSym.called("relation1", "gt")
class Gt(OMSym):
    pass

@OMSym.called("relation1", "leq")
class Leq(OMSym):
    pass

@OMSym.called("relation1", "lt")
class Lt(OMSym):
    pass

@OMSym.called("relation1", "neq")
class Neq(OMSym):
    pass
