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
        miscari = fisier.read()
        fisier.close()
    except IOError:
        print "Fisierul nu a putut fi citit."
        return

    xpoint = 0
    ypoint = 0
    for miscare in miscari.splitlines():
        mutare = miscare.split()
        casute = int(mutare[1])
        if mutare[0] == "SUS":
            ypoint -= casute
        elif mutare[0] == "JOS":
            ypoint += casute
        elif mutare[0] == "DREAPTA":
            xpoint += casute
        elif mutare[0] == "STANGA":
            xpoint -= casute
    print sqrt(xpoint**2 + ypoint**2)


if __name__ == "__main__":
    distanta()
