#!/bin/bash

# Sa se crie un script care prelucreaza un fisier cu extensia .csv (comma-
# separated values) primit ca argument in linia de comanda. Fisierul contine, pe
# coloane, urmatoarele informatii: adresa ip, adresa MAC, nume computer,
# comentarii.
# Exemplu linie fisier .csv:
#   a.b.c.d,aabbccddeeff,computer_x,sala_x
# Pentru fiecare linie din fisierul initial, scriptul va scrie intr-un fisier de iesire (al
# doilea argument din linia de comanda) o intrare de forma urmatoare:
#   host computer_x {
#   option host-name "computer_x";
#   hardware ethernet AA:BB:CC:DD:EE:FF;
#   fixed-address a.b.c.d;
#   }
# Exemplu de rulare:
#   ./<nume_script>
#   <fisier_intrare>.csv
#   <fisier_iesire>.txt

if [[ $# -ne 2 ]]; then
    echo "Nu avem destui parametri !";
    exit;
fi

while IFS=',' read -r line || [[ -n "$line" ]]; do
    ip="$(echo "$line" | cut -f1 -d ',')";
    mac="$(echo "$line" | cut -f2 -d ',')";
    server="$(echo "$line" | cut -f3 -d ',')";
    echo "host $server {" >> "$2";
    echo "option host-name $server" >> "$2";
    echo "hardware ethernet $mac" >> "$2";
    echo "fixed-adress $ip" >> "$2";
    echo '}' >> "$2";
done < $1;
