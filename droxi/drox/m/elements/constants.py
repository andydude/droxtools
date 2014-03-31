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

from ...etree import etree
from ...models import Sym
from ..config import MATHML_NS

class CConstantSym(Sym):
    
    @classmethod
    def from_cmathml(cls, tree):
        url = tree.tag
        return cls(url)

    @property
    def cmathml(self):
        tag = self.url
        return etree.Element(tag)

class CBoolean(object):

    def __init__(self, flag):
        self.flag = flag
    
    @classmethod
    def from_cmathml(cls, tree):
        name = tree.tag[1:].split('}')[1]
        flag = True if name == 'true' else False if name == 'false' else None
        return cls(flag)
    
    @property
    def cmathml(self):
        tag = '{' + MATHML_NS + '}' + str(self.flag).lower()
        return etree.Element(tag)
