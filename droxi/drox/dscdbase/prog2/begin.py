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
from ...models import Sym
from ..config import DROSOFT_CDBASE

class DBegin(Sym):
    _symbolCdbase = DROSOFT_CDBASE
    _symbolCd = 'prog2'
    _symbolName = 'begin'
    url = _symbolCdbase + '/' + _symbolCd + '#' + _symbolName
    
    def __init__(self, *args):
        Sym.__init__(self, DBegin.url)
        
    def __call__(self, *args):
        return args[-1]

    def __eval__(self, env):
        return self
    
    def __tree__(self):
        return self.cmathml_symbol

class DValue(Sym):
    _symbolCdbase = DROSOFT_CDBASE
    _symbolCd = 'prog2'
    _symbolName = 'value'
    url = _symbolCdbase + '/' + _symbolCd + '#' + _symbolName
    
    def __init__(self, *args):
        Sym.__init__(self, DBegin.url)
        
    def __call__(self, *args):
        return args[0]

    def __eval__(self, env):
        return self
    
    def __tree__(self):
        return self.cmathml_symbol
