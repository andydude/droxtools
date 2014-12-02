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
from .null import DNull

class DIncrement(Sym):
    def __transform__(self, _, var, **kwargs):
        env = kwargs.get('env')
        value = env[var.name]
        env[var.name] = type(value)(value.num + 1)
        return DNull()
    
class DDecrement(Sym):
    def __transform__(self, _, var, **kwargs):
        env = kwargs.get('env')
        value = env[var.name]
        env[var.name] = type(value)(value.num - 1)
        return DNull()

class DPreIncrement(Sym):
    def __transform__(self, _, var, **kwargs):
        
        return DNull()
    
class DPreDecrement(Sym):
    def __transform__(self, _, var, **kwargs):
        return DNull()

class DPostIncrement(Sym):
    def __transform__(self, _, var, **kwargs):
        return DNull()
    
class DPostDecrement(Sym):
    def __transform__(self, _, var, **kwargs):
        return DNull()
