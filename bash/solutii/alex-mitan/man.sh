#!/bin/bash

# Scrieti un script pentru cauta informatii in manualul unei comenzi
# ./man.sh nume_script informatie

if [[ $# -eq 2 ]]; then
    man "$1" | grep "\ $2"
else
    echo "./man.sh [command] [argument]"
    echo "for example: "
    echo "./man.sh ls -l "
fi
