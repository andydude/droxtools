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

__all__ = [
    '_namespace_mapping',
]

from . import models
from . import literals
from . import symbols

import argparse

_namespace_mapping = argparse.Namespace()
_namespace_mapping.__dict__.update({
    'cn': literals.CNumber,
    'cs': literals.CString,
    'cbytes': literals.CBinary,
    'emptyset': literals.CConstant,
    'pi': literals.CConstant,
    'eulergamma': literals.CConstant,
    'infinity': literals.CConstant,
    'integers': literals.CConstant,
    'reals': literals.CConstant,
    'rationals': literals.CConstant,
    'naturalnumbers': literals.CConstant,
    'complexes': literals.CConstant,
    'primes': literals.CConstant,
    'exponentiale': literals.CConstant,
    'imaginaryi': literals.CConstant,
    'notanumber': literals.CConstant,
    'true': literals.CBoolean,
    'false': literals.CBoolean,
    'csymbol': symbols.CSym,
    'ci': symbols.CVar,
    'math': models.Math,
    'apply': models.CApply,

    
    #'bind': models.CBind,
    'set': models.CSet,
    'list': models.CList,
})
