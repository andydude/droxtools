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

class Opt(object):
    
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value
        
    def to_property(self):
        return property(self.get_value, self.set_value)

class BoolOpt(Opt):
    def __init__(self, default):
        self.default = default
        self.value = default

class EnumOpt(Opt):
    def __init__(self, default, enum):
        self.default = default
        self.value = default
        self.enum = enum

class OptionsMixin(object):
    
    def __getattr__(self, name):
        return self.__dict__[name].value
    
    def __setattr__(self, name, value):
        self.__dict__[name].value = value

class Options(OptionsMixin):
    
    # laziness evaluation
    # False = eager
    # True  = lazy
    laziness = BoolOpt(False).to_property()

    # symbolic evaluation
    # False = strict
    # True  = symbolic
    symbolic = BoolOpt(False).to_property()
    
