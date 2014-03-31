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
import importlib
from .etree import etree
from .config import DEBUG

def drox_write(exp, fp=sys.stdout):
    fp.write(drox_write_string(exp) + '\n')

def drox_write_tree(exp):
    if DEBUG: print("write <= " + repr(exp))
    if hasattr(exp, '__tree__'):
        tree = exp.__tree__()
    else:
        name = '.'.join(type(exp).__module__.split('.')[:2])
        modulename = name + '.writer'
        #print("modulename = " + modulename)
        lib = importlib.import_module(modulename)
        tree = lib.Writer()(exp)
    if DEBUG: print("write => " + repr(tree))
    return tree

def drox_write_string(exp):
    tree = drox_write_tree(exp)
    return etree.tostring(tree)