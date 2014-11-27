'''
Created on Mar 30, 2014

@author: ajr
'''

from ...etree import etree
from ...read import drox_read_tree
from ...write import drox_write_tree
from ...omcdbase.models import OMSym
from ...models import Apply, Sym
from ..models import CSym

@CSym.called("math")
class Math(Apply):
    
    @classmethod
    def from_cmathml(cls, tree):
        args = map(drox_read_tree, list(tree))
        applier = Sym.from_etree(tree.tag)
        return cls(applier, *args)

    @property
    def cmathml(self):
        tree = etree.Element(self.etree)
        for arg in self.args:
            tree.append(drox_write_tree(arg))
        return tree

@CSym.called("apply")
class CApply(Math):
    
    @classmethod
    def from_cmathml(cls, tree):
        args = map(drox_read_tree, list(tree))
        return cls(*args)

    @property
    def cmathml(self):
        tree = etree.Element(self.etree)
        tree.append(drox_write_tree(self.applier)) # this is the only difference
        for arg in self.args:
            tree.append(drox_write_tree(arg))
        return tree

@CSym.called("set")
@OMSym.called("set1", "set")
class CSet(Math):
    def __call__(self, *args):
        pass
    
    @classmethod
    def from_cmathml(cls, tree):
        args = map(drox_read_tree, list(tree))
        applier = Sym.from_omsym(cls._symbolCdbase, cls._symbolCd, cls._symbolName)
        return cls(applier, *args)

@CSym.called("list")
@OMSym.called("list1", "list")
class CList(Math):
    def __call__(self, *args):
        pass
    
    @classmethod
    def from_cmathml(cls, tree):
        args = map(drox_read_tree, list(tree))
        applier = Sym.from_omsym(cls._symbolCdbase, cls._symbolCd, cls._symbolName)
        return cls(applier, *args)
