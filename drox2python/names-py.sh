#!/bin/bash
FILE="../python2drox/PythonRead.py"
grep emit_symbol $FILE | cut -d'(' -f2- | sort -u | cut -d"'" -f2,4 | tr "'" ':'
