#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# droxi
# Copyright (c) 2014, Andrew Robbins, All rights reserved.
# 
# This library ("it") is free software; it is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; you can redistribute it and/or modify it under the terms of the
# GNU Lesser General Public License ("LGPLv3") <https://www.gnu.org/licenses/lgpl.html>.

__all__ = [
    '_namespace_mapping',
]

from . import models
import argparse
_namespace_mapping = argparse.Namespace()
_namespace_mapping.__dict__.update({
    'arccos':  models.ArcCos,
    'arccosh': models.ArcCosh,
    'arccot':  models.ArcCot,
    'arccoth': models.ArcCoth,
    'arccsc':  models.ArcCsc,
    'arccsch': models.ArcCsch,
    'arcsec':  models.ArcSec,
    'arcsech': models.ArcSech,
    'arcsin':  models.ArcSin,
    'arcsinh': models.ArcSinh,

    'cos':  models.Cos,
    'cosh': models.Cosh,
    'cot':  models.Cot,
    'coth': models.Coth,
    'csc':  models.Csc,
    'csch': models.Csch,
    'sec':  models.Sec,
    'sech': models.Sech,
    'sin':  models.Sin,
    'sinh': models.Sinh,
    
    'exp': models.Exp,
    'log': models.Log,
    'ln': models.Ln,
})
