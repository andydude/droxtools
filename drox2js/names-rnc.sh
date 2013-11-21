#!/bin/bash
grep 'm:csymbol' JavaScriptValid.rnc | cut -d'{' -f3- | sort -u | cut -d'"' -f2,4 | tr '"' ':' | grep ':'
