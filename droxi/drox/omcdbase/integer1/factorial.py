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
    '''
    <drox:dl>
        <m:csymbol cd="prog1">function_definition</m:csymbol>
        <drox:dt>
            <m:csymbol cd="integer1">factorial</m:csymbol>
        </drox:dt>
        <m:bvar>
            <m:semantics>
                <m:ci>a</m:ci>
                <drox:btype>
                    <m:integers/>
                </drox:btype>
            </m:semantics>
        </m:bvar>
        <drox:rv>
            <m:semantics>
                <m:ci>_</m:ci>
                <drox:btype>
                    <m:integers/>
                </drox:btype>
            </m:semantics>
        </drox:rv>
        <m:apply>
            <m:csymbol cd="arith1">product</m:csymbol>
            <m:apply>
                <m:csymbol cd="integer1">integer_interval</m:csymbol>
                <m:cn>1</m:cn>
                <m:ci>a</m:ci>
            </m:apply>
            <m:bind>
                <m:csymbol cd="fns1">lambda</m:csymbol>
                <m:bvar>
                    <m:semantics>
                        <m:ci>b</m:ci>
                        <drox:btype>
                            <m:integers/>
                        </drox:btype>
                    <m:semantics>
                </m:bvar>
                <drox:rv>
                    <m:semantics>
                        <m:ci>_</m:ci>
                        <drox:btype>
                            <m:integers/>
                        </drox:btype>
                    </m:semantics>
                </drox:rv>
                <m:ci>b</m:ci>
            </m:bind>
        </m:apply>
    </drox:dl>
    '''
    _symbolCd = 'integer1'
    _symbolName = 'factorial'
    url = OMSym._symbolCdbase + '/' + _symbolCd + '#' + _symbolName
    
    def __call__(self, arg):
        cls = type(arg)
        terms = [num + 1 for num in range(arg.num)]
        return cls(reduce(lambda x, y: x*y, terms, 1))


