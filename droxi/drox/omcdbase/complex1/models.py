'''
Created on Mar 31, 2014

@author: ajr
'''

from ..models import OMSym

@OMSym.called("complex1", "argument")
class Argument(OMSym):
    pass

@OMSym.called("complex1", "conjugate")
class Conjugate(OMSym):
    pass

@OMSym.called("complex1", "complex_cartesian")
class Complex(OMSym):
    pass

@OMSym.called("complex1", "complex_polar")
class ComplexPolar(OMSym):
    pass

@OMSym.called("complex1", "imaginary")
class Imag(OMSym):
    pass

@OMSym.called("complex1", "real")
class Real(OMSym):
    pass
