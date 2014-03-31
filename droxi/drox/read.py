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

import sys
#import hashlib
import importlib
from .etree import etree
from .models import Sym
from .config import DEBUG

def drox_read(fp=sys.stdin):
    s = fp.read()
    return drox_read_string(s)

def drox_read_string(s):
    tree = etree.fromstring(s)
    return drox_read_tree(tree)

def drox_read_tree(tree):
    if DEBUG: print("read <= " + repr(tree))
    exp = Sym.resolve(Sym.from_etree(tree.tag), tree)
    if DEBUG: print("read => " + repr(exp))
    return exp

