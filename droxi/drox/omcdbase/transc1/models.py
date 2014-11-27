'''
Created on Mar 31, 2014

@author: ajr
'''

from ...models import Number
from ..models import OMSym
import math

# Inverse Trig

@OMSym.called("transc1", "arccos")
class ArcCos(OMSym):
    def __call__(self, arg):
        return None

@OMSym.called("transc1", "arccosh")
class ArcCosh(OMSym):
    def __call__(self, arg):
        return None

@OMSym.called("transc1", "arccot")
class ArcCot(OMSym):
    def __call__(self, arg):
        return None

@OMSym.called("transc1", "arccoth")
class ArcCoth(OMSym):
    def __call__(self, arg):
        return None

@OMSym.called("transc1", "arccsc")
class ArcCsc(OMSym):
    def __call__(self, arg):
        return None

@OMSym.called("transc1", "arccsch")
class ArcCsch(OMSym):
    def __call__(self, arg):
        return None

@OMSym.called("transc1", "arcsec")
class ArcSec(OMSym):
    def __call__(self, arg):
        return None

@OMSym.called("transc1", "arcsech")
class ArcSech(OMSym):
    def __call__(self, arg):
        return None

@OMSym.called("transc1", "arcsin")
class ArcSin(OMSym):
    def __call__(self, arg):
        return None

@OMSym.called("transc1", "arcsinh")
class ArcSinh(OMSym):
    def __call__(self, arg):
        return None

@OMSym.called("transc1", "arctan")
class ArcTan(OMSym):
    def __call__(self, arg):
        return None

@OMSym.called("transc1", "arctanh")
class ArcTanh(OMSym):
    def __call__(self, arg):
        return None

# Forward Trig

@OMSym.called("transc1", "cos")
class Cos(OMSym):
    def __call__(self, arg):
        return None

@OMSym.called("transc1", "cosh")
class Cosh(OMSym):
    def __call__(self, arg):
        return None

@OMSym.called("transc1", "cot")
class Cot(OMSym):
    def __call__(self, arg):
        return None

@OMSym.called("transc1", "coth")
class Coth(OMSym):
    def __call__(self, arg):
        return None

@OMSym.called("transc1", "csc")
class Csc(OMSym):
    def __call__(self, arg):
        return None

@OMSym.called("transc1", "csch")
class Csch(OMSym):
    def __call__(self, arg):
        return None

@OMSym.called("transc1", "sec")
class Sec(OMSym):
    def __call__(self, arg):
        return None

@OMSym.called("transc1", "sech")
class Sech(OMSym):
    def __call__(self, arg):
        return None

@OMSym.called("transc1", "sin")
class Sin(OMSym):
    def __call__(self, arg):
        return None

@OMSym.called("transc1", "sinh")
class Sinh(OMSym):
    def __call__(self, arg):
        return None

@OMSym.called("transc1", "tan")
class Tan(OMSym):
    def __call__(self, arg):
        return None

@OMSym.called("transc1", "tanh")
class Tanh(OMSym):
    def __call__(self, arg):
        return None

# Basic

@OMSym.called("transc1", "exp")
class Exp(OMSym):
    def __call__(self, arg):
        cls = type(arg)
        result = math.exp(arg.num)
        return cls(result)

@OMSym.called("transc1", "ln")
class Ln(OMSym):
    def __call__(self, arg):
        cls = type(arg)
        result = math.log(arg.num)
        return cls(result)

@OMSym.called("transc1", "Log")
class Log(OMSym):
    def __call__(self, base, arg):
        cls = Number.result_type(base, arg)
        result = math.log(arg.num, base.num)
        return cls(result)

