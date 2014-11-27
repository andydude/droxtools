'''
Created on Mar 31, 2014

@author: ajr
'''

from ..models import OMSym

# RTP rounding
@OMSym.called("rounding1", "ceiling")
class Ceiling(OMSym):
    pass

# RTN rounding
@OMSym.called("rounding1", "floor")
class Floor(OMSym):
    pass

# RTE rounding
@OMSym.called("rounding1", "round")
class RoundRTE(OMSym):
    pass

# RTZ rounding
@OMSym.called("rounding1", "trunc")
class RoundRTZ(OMSym):
    pass
