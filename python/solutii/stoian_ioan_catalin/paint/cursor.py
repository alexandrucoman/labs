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
import math

def distanta():
    """
    Calculează distanța dintre origine și poziția curentă.

    Funcția citește conținutul fișierului istoric.tuxy și
    calculează distanța dintre punctul de origine și poziția
    curentă a cursorului.
    """
    fisier = open("../../../date_intrare/istoric.tuxy", "r")
    istoric = fisier.read()
    cursor = [0, 0]
    istoric = istoric.split("\n")
    for command in istoric:
        attr = command.split(" ")
        if attr[0] == "SUS":
            cursor[0] += int(attr[1])
        if attr[0] == "JOS":
            cursor[0] -= int(attr[1])
        if attr[0] == "DREAPTA":
            cursor[1] += int(attr[1])
        if attr[0] == "STANGA":
            cursor[1] -= int(attr[1])
    distance = math.sqrt(cursor[0] * cursor[0] + cursor[1] * cursor[1])
    print(distance)
    pass


if __name__ == "__main__":
    distanta()
