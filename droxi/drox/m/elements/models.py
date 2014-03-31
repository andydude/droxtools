'''
Created on Mar 30, 2014

@author: ajr
'''

from ...models import Apply, Sym
from ...read import drox_read_tree
from ...write import drox_write_tree
from ...etree import etree
from ..config import MATHML_NS

class CApply(Apply):
    _contentName = 'apply'
    url = MATHML_NS + '::' + _contentName
    
    @classmethod
    def from_cmathml(cls, tree):
        args = map(drox_read_tree, list(tree))
        return cls(*args)

    @property
    def cmathml(self):
        tag = Sym(self.url).etree
        tree = etree.Element(tag)
        tree.append(drox_write_tree(self.applier))
        for arg in self.args:
            tree.append(drox_write_tree(arg))
        return tree

class Math(Apply):
    _contentName = 'math'
    url = MATHML_NS + '::' + _contentName
    
    @classmethod
    def from_cmathml(cls, tree):
        args = map(drox_read_tree, list(tree))
        return cls(Sym.from_etree(tree.tag), *args)

    @property
    def cmathml(self):
        tag = Sym(self.url).etree
        tree = etree.Element(tag)
        for arg in self.args:
            tree.append(drox_write_tree(arg))
        return tree
