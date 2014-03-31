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

import argparse
import json
import sys
import os.path

from drox.read import drox_read
from drox.eval import drox_eval
from drox.write import drox_write
from drox.init import drox_init

def parse_args():
    """
    droxi - Drosera Object XML Interpreter
    ---
    Copyright (c) 2014, Andrew Robbins, All rights reserved.
    """

    filename = os.path.join(os.path.dirname(__file__), "arguments.json")
    with open(filename) as f:
        arguments = json.load(f)

    description, epilog = parse_args.__doc__.split("---", 1)
    parser = argparse.ArgumentParser(description=description, epilog=epilog)
    for kwargs in arguments:
        args = kwargs['name']; del kwargs['name']
        parser.add_argument(*args, **kwargs)

    return parser.parse_args()

def dump_expr(exp):
    for x in dir(exp):
        y = repr(getattr(exp, x))
        if x.startswith('_'): continue
        if y.startswith('<'): continue
        print(x + ' = ' + y)

def main(args):
    drox_init()
    
    env = {}
    exp = drox_read()
    #            dump_expr(exp)
    print("--- # read")
    drox_write(exp)
    print("--- # eval")
    exp = drox_eval(exp, env)
    print("--- # write")
    drox_write(exp)
    

if __name__ == '__main__':
    sys.exit(main(parse_args()))
