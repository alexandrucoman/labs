#!/bin/bash
function rec {
    if [[ "$(diff -r "$1" "$2" | grep -c "Only")" -eq 0 ]]; then
        echo "Egale"
    else
        echo "Diferite"
    fi
}
if test "$#" -eq 2; then
    rec "$1" "$2"
else
    echo "tb 2 parametri!"
fi

