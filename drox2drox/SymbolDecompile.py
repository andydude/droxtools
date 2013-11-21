#!/usr/bin/env python

from __future__ import print_function
from __future__ import with_statement
from xml.etree import ElementTree

def register(prefix, ns):
    ElementTree.register_namespace(prefix, ns)

def decompile(doc):
    for child in doc.getiterator('{http://www.w3.org/1998/Math/MathML}csymbol'):
        cd = child.get('cd')
        ln = child.text
        ns = 'http://drosoft.org/cd/%s#' % (cd)
        register(cd, ns)

        # Replace symbol
        child.tag = '{%s}%s' % (ns, ln)
        child.attrib = {}
        child.text = None
    return doc

if __name__ == '__main__':
    from sys import argv, stdout
    with open(argv[1], 'r') as f:
        node = ElementTree.parse(f)
    register('drox', 'http://drosoft.org/ns/drosera')
    register('m', 'http://www.w3.org/1998/Math/MathML')

    # Decompile
    node = decompile(node)
    node.write(stdout)

