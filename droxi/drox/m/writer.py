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
from .config import MATHML_NS

class Writer(object):
    def __init__(self):
        pass
    
    def __call__(self, ast):
        if hasattr(ast, 'cmathml'):
            try:
                tree =  ast.cmathml
            except Exception as err:
                print("cought exception in Writer" + repr(err))
                raise
            return tree
        
        raise NotImplementedError
