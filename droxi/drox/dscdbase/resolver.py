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

from .config import DROSOFT_CDBASE
from ..resolver import BuiltinResolver

class Resolver(BuiltinResolver):
    def __init__(self):
        BuiltinResolver.__init__(self, cdbase = DROSOFT_CDBASE, package = __package__)
