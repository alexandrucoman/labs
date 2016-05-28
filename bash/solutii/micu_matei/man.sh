#!/bin/bash

# Scrieti un script pentru cauta informatii in manualul unei comenzi
# ./man.sh nume_script informatie
if [[ $# -lt 2 ]]; then
    echo "Insuficienti parametri "
    exit
fi

man "$1" | grep "$2" | less
