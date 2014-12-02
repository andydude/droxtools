#!/bin/bash

#PREFIX=$(pwd)/../..
PREFIX=/Users/ajr/db/local
CLANG_PREFIX="${PREFIX}"

autoreconf

./configure \
--prefix="${PREFIX}" \
CFLAGS="-I${CLANG_PREFIX}/include" \
CXXFLAGS="-I${CLANG_PREFIX}/include" \
LDFLAGS="-L${CLANG_PREFIX}/lib" \
CC="${CLANG_PREFIX}/bin/clang" \
CXX="${CLANG_PREFIX}/bin/clang++" \
CPP="${CLANG_PREFIX}/bin/clang -E"
