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
from ..models import OMSym
from ...models import Number

# http://www.openmath.org/cd/integer1.xhtml#factorof
class FactorOf(OMSym):
    _symbolCd = 'integer1'
    _symbolName = 'factorial'
    url = OMSym._symbolCdbase + '/' + _symbolCd + '#' + _symbolName
    
    def __call__(self, *args):
        cls = Number.result_type(*args)
        return cls(sum([it.num for it in args]))


