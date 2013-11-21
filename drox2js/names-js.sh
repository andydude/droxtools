#!/bin/bash
FILE="../js2drox/JavaScriptRead.js"
grep emitSym $FILE | cut -d'(' -f2- | sort -u | cut -d"'" -f2,4 | tr "'" ':'
