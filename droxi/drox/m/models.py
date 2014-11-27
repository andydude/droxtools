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

from ..models import Sym
from .config import MATHML_NS

class CSym(Sym):
    _contentNs = MATHML_NS

    @classmethod
    def called(cls, name):
        def decorator(obj):
            obj._contentName = name
            obj.url = CSym._contentNs + '::' + name
            return obj
        return decorator
