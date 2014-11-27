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

# http://www.openmath.org/cd/integer1.xhtml#quotient
class Quotient(OMSym):
    _symbolCd = 'integer1'
    _symbolName = 'quotient'
    url = OMSym._symbolCdbase + '/' + _symbolCd + '#' + _symbolName
    
    def __call__(self, *args):
        cls = Number.result_type(*args)
        return cls(sum([it.num for it in args]))

# http://www.openmath.org/cd/integer1.xhtml#remainder
class Remainder(OMSym):
    _symbolCd = 'integer1'
    _symbolName = 'remainder'
    url = OMSym._symbolCdbase + '/' + _symbolCd + '#' + _symbolName
    
    def __call__(self, *args):
        cls = Number.result_type(*args)
        return cls(sum([it.num for it in args]))
