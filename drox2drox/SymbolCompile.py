#!/usr/bin/env python

from __future__ import print_function
from __future__ import with_statement
from xml.etree import ElementTree

def register(prefix, ns):
    ElementTree.register_namespace(prefix, ns)

def compile(doc):
    for child in doc.getiterator():
        ns, ln = child.tag[1:].split('}')
        if not ns[-1] == '#': continue
        cdbase, cd = ns[:-1].rsplit('/', 1)
        if not cdbase.endswith('/cd'): continue

        # Replace symbol
        child.tag = '{http://www.w3.org/1998/Math/MathML}csymbol'
        child.attrib = {'cd': cd}
        child.text = ln
    return doc

if __name__ == '__main__':
    from sys import argv, stdout
    with open(argv[1], 'r') as f:
        node = ElementTree.parse(f)
    register('drox', 'http://drosoft.org/ns/drosera')
    register('m', 'http://www.w3.org/1998/Math/MathML')

    # Compile
    node = compile(node)
    node.write(stdout)

