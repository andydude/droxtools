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

class DIf(Sym):
    def __transform__(self, _, var, **kwargs):
        env = kwargs.get('env')
        value = env[var.name]
        env[var.name] = type(value)(value.num + 1)
        return DNull()

class DIfNot(Sym):
    def __transform__(self, _, var, **kwargs):
        env = kwargs.get('env')
        value = env[var.name]
        env[var.name] = type(value)(value.num + 1)
        return DNull()

class DIfExp(Sym):
    def __transform__(self, _, var, **kwargs):
        env = kwargs.get('env')
        value = env[var.name]
        env[var.name] = type(value)(value.num + 1)
        return DNull()

class DDoIf(Sym):
    def __transform__(self, _, var, **kwargs):
        env = kwargs.get('env')
        value = env[var.name]
        env[var.name] = type(value)(value.num + 1)
        return DNull()

class DDoIfNot(Sym):
    def __transform__(self, _, var, **kwargs):
        env = kwargs.get('env')
        value = env[var.name]
        env[var.name] = type(value)(value.num + 1)
        return DNull()

class DDoIfExp(Sym):
    def __transform__(self, _, var, **kwargs):
        env = kwargs.get('env')
        value = env[var.name]
        env[var.name] = type(value)(value.num + 1)
        return DNull()

class DWhile(Sym):
    def __transform__(self, _, var, **kwargs):
        env = kwargs.get('env')
        value = env[var.name]
        env[var.name] = type(value)(value.num + 1)
        return DNull()

class DWhileNot(Sym):
    def __transform__(self, _, var, **kwargs):
        env = kwargs.get('env')
        value = env[var.name]
        env[var.name] = type(value)(value.num + 1)
        return DNull()

class DDoWhile(Sym):
    def __transform__(self, _, var, **kwargs):
        env = kwargs.get('env')
        value = env[var.name]
        env[var.name] = type(value)(value.num + 1)
        return DNull()

class DDoWhileNot(Sym):
    def __transform__(self, _, var, **kwargs):
        env = kwargs.get('env')
        value = env[var.name]
        env[var.name] = type(value)(value.num + 1)
        return DNull()

class DElse(Sym):
    def __transform__(self, _, var, **kwargs):
        env = kwargs.get('env')
        value = env[var.name]
        env[var.name] = type(value)(value.num + 1)
        return DNull()
