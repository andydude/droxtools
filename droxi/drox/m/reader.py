#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# droxi
# Copyright (c) 2014, Andrew Robbins, All rights reserved.
# 
# This library ("it") is free software; it is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; you can redistribute it and/or modify it under the terms of the
# GNU Lesser General Public License ("LGPLv3") <https://www.gnu.org/licenses/lgpl.html>.
from __future__ import absolute_import

from ..etree import etree
from ..models import Sym
from .config import MATHML_NS
from .elements import cmathml

class Reader(object):
    def __init__(self):
        pass

    def __call__(self, sym, tree):
        if not etree.iselement(tree):
            raise ValueError, tree
        
        ns, name = Sym.from_etree(tree.tag).xmlns
        if ns != MATHML_NS:
            raise ValueError, ns
    
        ElemCls = getattr(cmathml, name)
        ast = ElemCls.from_cmathml(tree)
        return ast
