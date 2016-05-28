#!/bin/bash

if [[ `diff -r $1 $2 | wc -c` -gt 0 ]]
then
    echo "Sunt diferite"
else
    echo "Nu sunt diferite"
fi

