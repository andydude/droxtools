#!/bin/bash
DIR=$(dirname $0)
for FILE in "$@"; do
    head -c 435 "$FILE" | cmp $DIR/header.txt - | sed -e "s| - | $FILE |g"
done
