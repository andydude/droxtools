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

import six
import base64
from ...etree import etree
from ...models import Constant, Boolean, Number, Integer, Real
from ..config import MATHML_NS

class CNumber(Number):
    pass

class CInt(Integer):
    pass

class CFlo(Real):
    pass


class CConstant(Constant):
    pass

class CBoolean(Boolean):
    pass

class CData(object):
    def __init__(self):
        raise NotImplementedError

class CBinary(CData):
    _contentName = 'cbytes'
    _presentName = 'mb'
    _openmathName = 'OMB'
    
    def __init__(self, data):
        self.data = data

    @classmethod
    def from_cmathml(cls, tree):
        data = base64.b64decode(tree.text)
        if not isinstance(data, six.binary_type):
            data = six.binary_type(data)
        return cls(data)

    @property
    def cmathml(self):
        tag = '{' + MATHML_NS + '}' + self._contentName
        tree = etree.Element(tag)
        tree.text = base64.b64encode(self.data)
        return tree
    
class CString(CData):
    _contentName = 'cs'
    _presentName = 'ms'
    _openmathName = 'OMSTR'

    def __init__(self, text):
        self.text = text

    @classmethod
    def from_cmathml(cls, tree):
        text = tree.text
        if not isinstance(text, six.text_type):
            text = six.text_type(text)
        return cls(text)

    @property
    def cmathml(self):
        tag = '{' + MATHML_NS + '}' + self._contentName
        tree = etree.Element(tag)
        tree.text = self.text
        return tree

class CGlyph(CData):
    presentName = 'mglyph'

    def __init__(self, tree):
        self.tree = tree

class CComment(CData):
    presentName = 'mtext'

    def __init__(self, tree):
        self.tree = tree

class CSpace(CData):
    presentName = 'mspace'

    def __init__(self, tree):
        self.tree = tree
