#!/bin/bash  
function up2 {
    limit=$1
    P=$PWD
    for ((i=1; i<=limit; i++)); do
        P=$P/..
        ((i++))
        ((--i))
    done
    cd "$P" || exit
    export MYPATH=$P
}

