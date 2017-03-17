#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""Tuxy dorește să împlementeze un nou paint pentru consolă.

În timpul dezvoltării proiectului s-a izbit de o problemă
pe care nu o poate rezolva singur și a apelat la ajutorul tău.

Aplicația ține un istoric al tuturor mișcărilor pe care le-a
făcut utlizatorul în fișierul istoric.tuxy

Exemplu de istoric.tuxy:

    STÂNGA 2
    JOS 2
    DREAPTA 5

Fișierul de mai sus ne spune că utilizatorul a mutat cursorul
2 căsuțe la stânga după care 2 căsuțe in jos iar ultima acțiune
a fost să poziționeze cursorul cu 5 căsuțe în dreapta față de
ultima poziție.

El dorește un utilitar care să îi spună care este distanța dintre
punctul de origine (0, 0) și poziția curentă a cursorului.
"""

from math import sqrt


def distanta():
    """
    Calculează distanța dintre origine și poziția curentă.

    Funcția citește conținutul fișierului istoric.tuxy și
    calculează distanța dintre punctul de origine și poziția
    curentă a cursorului.
    """
    try:
        fisier = open("istoric.tuxy", "r")
        comenzi = fisier.read().splitlines()
    except IOError:
        print "Nu am putut deschide fisierul cu comenzi!"
        return
    fisier.close()

    pozitie_finala = [0, 0]

    for linie in comenzi:
        comm = linie.split(" ")

        # validare comanda citita din fisier
        if len(comm) != 2 \
                or comm[0] not in ("STANGA", "DREAPTA", "SUS", "JOS") \
                or not comm[1].isdigit():
            print "Comanda invalida: %s" % comm
            return

        if comm[0] == "STANGA":
            pozitie_finala[0] -= int(comm[1])
        elif comm[0] == "DREAPTA":
            pozitie_finala[0] += int(comm[1])
        elif comm[0] == "SUS":
            pozitie_finala[1] += int(comm[1])
        elif comm[0] == "JOS":
            pozitie_finala[1] -= int(comm[1])

    return sqrt(pozitie_finala[0] ** 2 + pozitie_finala[1] ** 2)

if __name__ == "__main__":
    print "\nDistanta dintre punctul initial (0, 0) si punctul final este: %f"\
          % distanta()
