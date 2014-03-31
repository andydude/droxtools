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
from __future__ import print_function

from ...models import Sym
from .void import DVoid

class DPrint(Sym):
    def __call__(self, *args):
        print(*args, end='')
        return DVoid()
    
class DPrintLine(Sym):
    def __call__(self, *args):
        print(*args)
        return DVoid()
        