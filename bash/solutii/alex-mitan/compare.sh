#!/bin/bash

DIFFERENCES=$(diff "$1" "$2")

if [[ -z $DIFFERENCES ]]; then
    echo "There are no differences"
else
    echo "There are differences."
fi