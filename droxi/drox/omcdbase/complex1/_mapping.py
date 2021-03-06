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
    'argument': models.Argument,
    'complex_cartesian': models.Complex,
    'complex_polar': models.ComplexPolar,
    'conjugate': models.Conjugate,
    'imaginary': models.Imag,
    'real': models.Real,
})
