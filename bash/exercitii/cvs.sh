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
echo "Nu ma executa"