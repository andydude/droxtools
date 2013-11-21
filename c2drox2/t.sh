#!/bin/bash

for T in t/*.t; do
    perl6 -Ilib $T
done
