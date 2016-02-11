#!/bin/bash

# 8.1. Scrieti un script care sa va ajute la scrierea programelor in C, care sa
# automatizeze ciclul: modificare-sursa -> compilare -> testare(executie). Scriptul trebuie se
# afiseze un meniu cu o serie de optiuni pentru utilizator. Pentru fiecare optiune trebuie
# scrisa o functie ( toate functiile trebuie scrise intr-un singur fisier).
# Optiuni meniu:
#   a) sa lanseze editorul de texte pentru fisierul fisier.c specificat ca parametru
# sau cerut de la linia de comanda;
#   b) sa lanseze compilatorul (fisierul executabil sa aiba numele fisier , deci fara
# sufixul .c); daca sunt erori de compilare (lucru observabil prin erorile de compilare afisate
# de compilator) sau warning-uri si sa le salveze intr-un fisier (fisier.err); fisierul de erori
# si executabilul se sterg la fiecare compilare;
#   c) sa afiseze continutul fisierului fisier.err daca sunt erori (exista fisierul si are
# dimensiunea > 0);
#   d) sa lanseze in executie programul ( afisare mesaj de eroare daca nu exista
# executabilul);
#   e) iesire din script.
echo "Nu ma executa"