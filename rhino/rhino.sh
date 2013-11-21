#!/bin/bash
DIR=$(dirname $0)
java -jar $DIR/js.jar -require "$@"
