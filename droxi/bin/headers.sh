#!/bin/bash
DIR=$(dirname $0)
find . -name '*.py' | xargs bash $DIR/header.sh
