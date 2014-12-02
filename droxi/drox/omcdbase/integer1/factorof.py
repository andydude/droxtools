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
from ...models import Boolean

# http://www.openmath.org/cd/integer1.xhtml#factorof
class FactorOf(OMSym):
    '''
    <drox:dl>
        <m:csymbol cd="prog1">function_definition</m:csymbol>
        <drox:dt>
            <m:csymbol cd="integer1">factorof</m:csymbol>
        </drox:dt>
        <m:bvar>
            <m:semantics>
                <m:ci>a</m:ci>
                <drox:btype>
                    <m:integers/>
                </drox:btype>
            </m:semantics>
        </m:bvar>
        <m:bvar>
            <m:semantics>
                <m:ci>b</m:ci>
                <drox:btype>
                    <m:integers/>
                </drox:btype>
            </m:semantics>
        </m:bvar>
        <drox:rv>
            <m:semantics>
                <m:ci>_</m:ci>
                <drox:btype>
                    <m:csymbol cd="setname2">Boolean</m:csymbol>
                </drox:btype>
            </m:semantics>
        </drox:rv>
        <m:apply>
            <m:csymbol cd="relation1">eq</m:csymbol>
            <m:apply>
                <m:csymbol cd="integer1">remainder</m:csymbol>
                <m:ci>a</m:ci>
                <m:ci>b</m:ci>
            </m:apply>
            <m:cn>0</m:cn>
        </m:apply>
    </drox:dl>
    '''
    _symbolCd = 'integer1'
    _symbolName = 'factorof'
    url = OMSym._symbolCdbase + '/' + _symbolCd + '#' + _symbolName
    
    def __call__(self, a_obj, b_obj):
        a_num, b_num = a_obj.num, b_obj.num
        return Boolean(a_num % b_num == 0)

