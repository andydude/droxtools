#!/usr/bin/env python

if __name__ == '__main__':
    from sys import argv
    from ast import parse
    from PythonRead import DroVisitor

    # read file
    filename = argv[1]
    with open(filename) as f:
        tree = parse(f.read(), filename)

    # compile
    visitor = DroVisitor()
    visitor.visit(tree)
