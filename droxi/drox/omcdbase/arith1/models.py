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

# http://www.openmath.org/cd/arith1.xhtml#abs
# http://www.w3.org/TR/MathML3/chapter4.html#contm.abs
@OMSym.called("arith1", "abs")
class Abs(OMSym):
    def __call__(self, *args):
        cls = Number.result_type(*args)
        return cls(sum([it.num for it in args]))

# http://www.openmath.org/cd/arith1.xhtml#divide
# http://www.w3.org/TR/MathML3/chapter4.html#contm.divide
@OMSym.called("arith1", "divide")
class Divide(OMSym):
    def __call__(self, *args):
        cls = Number.result_type(*args)
        return cls(sum([it.num for it in args]))

# http://www.openmath.org/cd/arith1.xhtml#gcd
# http://www.w3.org/TR/MathML3/chapter4.html#contm.gcd
@OMSym.called("arith1", "gcd")
class GCD(OMSym):
    def __call__(self, *args):
        cls = Number.result_type(*args)
        return cls(sum([it.num for it in args]))

# http://www.openmath.org/cd/arith1.xhtml#lcm
# http://www.w3.org/TR/MathML3/chapter4.html#contm.lcm
@OMSym.called("arith1", "lcm")
class LCM(OMSym):
    def __call__(self, *args):
        cls = Number.result_type(*args)
        return cls(sum([it.num for it in args]))

# http://www.openmath.org/cd/arith1.xhtml#minus
# http://www.w3.org/TR/MathML3/chapter4.html#contm.minus
@OMSym.called("arith1", "minus")
class Minus(OMSym):
    def __call__(self, arg, *args):
        cls = Number.result_type(*args)
        return cls(arg.num - sum([it.num for it in args]))

# http://www.openmath.org/cd/arith1.xhtml#plus
# http://www.w3.org/TR/MathML3/chapter4.html#contm.plus
@OMSym.called("arith1", "plus")
class Plus(OMSym):
    def __call__(self, *args):
        cls = Number.result_type(*args)
        return cls(sum([it.num for it in args]))

# http://www.openmath.org/cd/arith1.xhtml#power
# http://www.w3.org/TR/MathML3/chapter4.html#contm.power
@OMSym.called("arith1", "power")
class Power(OMSym):
    def __call__(self, *args):
        cls = Number.result_type(*args)
        return cls(sum([it.num for it in args]))

# http://www.openmath.org/cd/arith1.xhtml#product
# http://www.w3.org/TR/MathML3/chapter4.html#contm.product
@OMSym.called("arith1", "product")
class Product(OMSym):
    def __call__(self, *args):
        cls = Number.result_type(*args)
        return cls(sum([it.num for it in args]))

# http://www.openmath.org/cd/arith1.xhtml#root
# http://www.w3.org/TR/MathML3/chapter4.html#contm.root
@OMSym.called("arith1", "root")
class Root(OMSym):
    def __call__(self, *args):
        cls = Number.result_type(*args)
        return cls(sum([it.num for it in args]))

# http://www.openmath.org/cd/arith1.xhtml#sum
# http://www.w3.org/TR/MathML3/chapter4.html#contm.sum
@OMSym.called("arith1", "sum")
class Sum(OMSym):
    def __call__(self, *args):
        cls = Number.result_type(*args)
        return cls(sum([it.num for it in args]))

# http://www.openmath.org/cd/arith1.xhtml#times
# http://www.w3.org/TR/MathML3/chapter4.html#contm.times
@OMSym.called("arith1", "times")
class Times(OMSym):
    def __call__(self, *args):
        cls = Number.result_type(*args)
        return cls(reduce(lambda x, y: x*y, [it.num for it in args], 1))

# http://www.openmath.org/cd/arith1.xhtml#unary_minus
# http://www.w3.org/TR/MathML3/chapter4.html#contm.minus
@OMSym.called("arith1", "unary_minus")
class UnaryMinus(OMSym):
    def __call__(self, arg):
        cls = type(arg)
        return cls(-arg.num)
