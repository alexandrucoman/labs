#!/bin/bash

DIR1=`ls -r $1`
DIR2=`ls -r $2`

if [[ $DIR1 = $DIR2 ]]; then
    echo "There are no differences"
else
    echo "There are differences."
fi