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
import collections
import six
#import types
#import numbers
from .models import Apply
from .config import DEBUG

def drox_iscallable(exp):
    return isinstance(exp, Apply)
    #return six.callable(exp)
    

def drox_eval_literal(exp, env):
    
    
    if isinstance(exp, collections.Mapping):
        return drox_eval_mapping(exp, env)
    
    if isinstance(exp, collections.Iterable):
        return drox_eval_sequence(exp, env)
    
    if hasattr(exp, '__eval__'):
        ret = exp.__eval__(env)
        if ret == NotImplemented:
            return exp
        return ret

    return exp

def drox_eval_mapping(exp, env):
    return dict(map(lambda exp: drox_eval(exp, env), six.iteritems(exp)))
    
def drox_eval_sequence(exp, env):
    return list(map(lambda exp: drox_eval(exp, env), iter(exp)))

def drox_eval(exp, env):

    if not drox_iscallable(exp):
        return drox_eval_literal(exp, env)
    
    # TODO: transformers
    if hasattr(exp.applier, '__transform__'):
        ret = exp.applier.__transform__(exp.applier, *exp.args, env=env)
        return ret
    
    applier = drox_eval_literal(exp.applier, env)
    args    = drox_eval_literal(exp.args, env)
    if DEBUG: print("eval <= " + repr(applier))
    if DEBUG: print("eval <= " + repr(applier.url))
    if DEBUG: print("eval () " + repr(args))
    if DEBUG: print(repr(applier.__call__))
    
    if hasattr(applier, '__call__'):
        ret = applier.__call__(*args)
    else:
        print("Called a non-callable!")
        
    if DEBUG: print("eval => " + repr(ret))
    if ret == NotImplemented:
        exp = exp.__class__(applier, *args)
        return exp
    
    return ret
    