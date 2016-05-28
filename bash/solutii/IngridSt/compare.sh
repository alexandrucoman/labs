#!/bin/bash -x


NUMBER_DIFFERENCES=$(diff -rq "$1" "$2")
if [ "$NUMBER_DIFFERENCES" = '' ]; then
echo "Sunt egale"
fi


