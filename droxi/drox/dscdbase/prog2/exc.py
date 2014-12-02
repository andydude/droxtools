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

class DBreak(Sym):
    _symbolCdbase = DROSOFT_CDBASE
    _symbolCd = 'prog2'
    _symbolName = 'break'
    url = _symbolCdbase + '/' + _symbolCd + '#' + _symbolName
    
    def __init__(self, *args):
        Sym.__init__(self, DBreak.url)
        
    def __call__(self, *args):
        return self

    def __eval__(self, env):
        return self
    
    def __tree__(self):
        return self.cmathml_symbol

class DContinue(Sym):
    _symbolCdbase = DROSOFT_CDBASE
    _symbolCd = 'prog2'
    _symbolName = 'continue'
    url = _symbolCdbase + '/' + _symbolCd + '#' + _symbolName
    
    def __init__(self, *args):
        Sym.__init__(self, DContinue.url)
        
    def __call__(self, *args):
        return self

    def __eval__(self, env):
        return self
    
    def __tree__(self):
        return self.cmathml_symbol

class DFallthrough(Sym):
    _symbolCdbase = DROSOFT_CDBASE
    _symbolCd = 'prog2'
    _symbolName = 'fallthrough'
    url = _symbolCdbase + '/' + _symbolCd + '#' + _symbolName
    
    def __init__(self, *args):
        Sym.__init__(self, DFallthrough.url)
        
    def __call__(self, *args):
        return self

    def __eval__(self, env):
        return self
    
    def __tree__(self):
        return self.cmathml_symbol

class DGoto(Sym):
    _symbolCdbase = DROSOFT_CDBASE
    _symbolCd = 'prog2'
    _symbolName = 'goto'
    url = _symbolCdbase + '/' + _symbolCd + '#' + _symbolName
    
    def __init__(self, *args):
        Sym.__init__(self, DGoto.url)
        
    def __call__(self, *args):
        return self

    def __eval__(self, env):
        return self
    
    def __tree__(self):
        return self.cmathml_symbol

class DLabel(Sym):
    _symbolCdbase = DROSOFT_CDBASE
    _symbolCd = 'prog2'
    _symbolName = 'label'
    url = _symbolCdbase + '/' + _symbolCd + '#' + _symbolName
    
    def __init__(self, *args):
        Sym.__init__(self, DLabel.url)
        
    def __call__(self, *args):
        return self

    def __eval__(self, env):
        return self
    
    def __tree__(self):
        return self.cmathml_symbol

class DYield(Sym):
    _symbolCdbase = DROSOFT_CDBASE
    _symbolCd = 'prog2'
    _symbolName = 'yield'
    url = _symbolCdbase + '/' + _symbolCd + '#' + _symbolName
    
    def __init__(self, *args):
        Sym.__init__(self, DYield.url)
        
    def __call__(self, *args):
        return self

    def __eval__(self, env):
        return self
    
    def __tree__(self):
        return self.cmathml_symbol
