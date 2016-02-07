#!/usr/bin/env python
# *-* coding: UTF-8 *-*

"""
Organizaţia Internaţională a Aviaţiei Civile propune un alfabet în care
fiecărei litere îi este asignat un cuvânt pentru a evita problemele în
înțelegerea mesajelor critice.

Pentru a se păstra un istoric al conversațiilor s-a decis transcrierea lor
conform următoarelor reguli:
    - fiecare cuvânt este scris pe o singură linie
    - literele din alfabet sunt separate de o virgulă

Următoarea sarcină ți-a fost asignată:
    Scrie un program care să primească un fișier ce conține mesajul
    brut (scris folosind alfabetul ICAO) și generează un fișier
    numit icao_intrare ce va conține mesajul inițial.
"""

from __future__ import print_function
from to_icao import ICAO


def din_icao(fisier_intrare):
    """Funcția va primi calea către fișierul ce conține mesajul brut și
    va genera un fișier numit icao_intrare ce va conține mesajul inițial.
    """
    continut = []
    mesaj = []
    with open(fisier_intrare) as fisier:
        continut = fisier.readlines()

    for linie in continut:
        for cuvant in linie.split():
            if cuvant != ICAO[cuvant[0]]:
                print("[x] A fost detectat un cuvant invalid: %s" % cuvant)
                return False
            else:
                mesaj.append(cuvant[0])
        mesaj.append(" ")

    with open("icao_intrare", "w") as fisier_iesire:
        fisier_iesire.write("".join(mesaj))

if __name__ == "__main__":
    din_icao("mesaj.icao")
