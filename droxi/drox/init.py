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

from .etree import etree
from .m.config import MATHML_NS
from .drox.config import DROX_NS
from .omcdbase.config import OPENMATH_CDBASE, OPENMATH_CDS
from .dscdbase.config import DROSOFT_CDBASE, DROSOFT_CDS

def drox_init():
    etree.register_namespace('m', MATHML_NS)
    etree.register_namespace('drox', DROX_NS)

    for cd in OPENMATH_CDS:
        etree.register_namespace(cd, OPENMATH_CDBASE + '/' + cd + '#')
        
    for cd in DROSOFT_CDS:
        etree.register_namespace(cd, DROSOFT_CDBASE + '/' + cd + '#')
