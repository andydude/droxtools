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

from .m.config import MATHML_NS
from .om.config import OPENMATH_NS, OPENMATHCD_NS, OPENMATHCDG_NS, OPENMATHCDS_NS
from .drox.config import DROX_NS
from .omcdbase.config import OPENMATH_CDBASE
from .dscdbase.config import DROSOFT_CDBASE

DEBUG = False

BUILTIN_CD = {
    'omcdbase': OPENMATH_CDBASE,
    'dscdbase': DROSOFT_CDBASE,
}

BUILTIN_NS = {
    'm': MATHML_NS,  # 90% of DROX
    'drox': DROX_NS, # 10% of DROX
    'om': OPENMATH_NS,
    'omcd': OPENMATHCD_NS,
    'omcdg': OPENMATHCDG_NS,
    'omcds': OPENMATHCDS_NS,
}

CURRENT_CD = {}
CURRENT_NS = {}