#!/bin/bash

# Sa se scrie un fisier de comenzi, care verifica daca doua directoare sunt egale.
# Numele celor doua directoare se transmit ca argumente in linia de comanda. Doua
# directoare se considera ca sunt egale daca contin aceleasi subdirectoare si fisiere.
# Se utilizeaza comanda diff.

if [[ $# -ne 2 ]]; then
    echo "Not enough params !";
    exit;
fi

rezult="$(diff -r "$1" "$2")";

if [[ "$rezult" == "" ]]; then
    echo "Directoarele sunt la fel";
else
    echo "Directoarele nu sunt la fel";
fi
