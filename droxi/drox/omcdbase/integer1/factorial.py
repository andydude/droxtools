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
from ...models import Number
from ..models import OMSym

# http://www.w3.org/TR/MathML3/chapter4.html#contm.factorial
class Factorial(OMSym):
    _symbolCd = 'integer1'
    _symbolName = 'factorial'
    url = OMSym._symbolCdbase + '/' + _symbolCd + '#' + _symbolName
    
    def __call__(self, arg):
        cls = type(arg)
        terms = [num + 1 for num in range(arg.num)]
        return cls(reduce(lambda x, y: x*y, terms, 1))


