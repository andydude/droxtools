'''
Created on Mar 31, 2014

@author: ajr
'''

from ..models import OMSym

@OMSym.called("set1", "cartesian_product")
class CartesianProduct(OMSym):
    pass

@OMSym.called("set1", "in")
class In(OMSym):
    pass

@OMSym.called("set1", "intersect")
class Intersect(OMSym):
    pass

@OMSym.called("set1", "notin")
class NotIn(OMSym):
    pass

@OMSym.called("set1", "notprsubset")
class NotPrSubSet(OMSym):
    pass

@OMSym.called("set1", "notsubset")
class NotSubSet(OMSym):
    pass

@OMSym.called("set1", "prsubset")
class PrSubSet(OMSym):
    pass

@OMSym.called("set1", "set")
class Set(OMSym):
    pass

@OMSym.called("set1", "setdiff")
class SetDiff(OMSym):
    pass

@OMSym.called("set1", "size")
class Size(OMSym):
    pass

@OMSym.called("set1", "subset")
class SubSet(OMSym):
    pass

@OMSym.called("set1", "union")
class Union(OMSym):
    pass

@OMSym.called("set1", "emptyset")
class EmptySet(OMSym):
    pass

@OMSym.called("set1", "map")
class Map(OMSym):
    pass

@OMSym.called("set1", "suchthat")
class SuchThat(OMSym):
    pass
