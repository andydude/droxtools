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

from ...models import Boolean
from ..models import OMSym

# http://www.openmath.org/cd/logic1.xhtml#and
@OMSym.called("logic1", "and")
class And(OMSym):
    def __call__(self, *args):
        args = map(lambda it: it.flag, args)
        result = reduce(lambda x, y: x and y, args, True)
        return Boolean(result)

# http://www.openmath.org/cd/logic1.xhtml#or
@OMSym.called("logic1", "or")
class Or(OMSym):
    def __call__(self, *args):
        args = map(lambda it: it.flag, args)
        result = reduce(lambda x, y: x or y, args, False)
        return Boolean(result)

# http://www.openmath.org/cd/logic1.xhtml#xor
@OMSym.called("logic1", "xor")
class Xor(OMSym):
    def __call__(self, *args):
        args = map(lambda it: it.flag, args)
        result = reduce(lambda x, y: bool(x) ^ bool(y), args, False)
        return Boolean(result)

# http://www.openmath.org/cd/logic1.xhtml#equivalent
@OMSym.called("logic1", "equivalent")
class Equivalent(OMSym):
    def __call__(self, *args):
        args = map(lambda it: it.flag, args)
        result = reduce(lambda x, y: not (bool(x) ^ bool(y)), args, False)
        return Boolean(result)

# http://www.openmath.org/cd/logic1.xhtml#implies
@OMSym.called("logic1", "implies")
class Implies(OMSym):
    def __call__(self, *args):
        args = map(lambda it: it.flag, args)
        result = reduce(lambda x, y: (not bool(x)) or bool(y), args, False)
        return Boolean(result)

# http://www.openmath.org/cd/logic1.xhtml#not
@OMSym.called("logic1", "not")
class Not(OMSym):
    def __call__(self, arg):
        return Boolean(not arg.flag)


# http://www.openmath.org/cd/logic1.xhtml#false
@OMSym.called("logic1", "false")
class OMFalse(OMSym):
    def __call__(self):
        return Boolean(False)

# http://www.openmath.org/cd/logic1.xhtml#true
@OMSym.called("logic1", "true")
class OMTrue(OMSym):
    def __call__(self):
        return Boolean(True)
