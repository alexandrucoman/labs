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
import operator

INSTRUCTIUNI = {
    "STANGA": (operator.sub, 0),
    "DREAPTA": (operator.add, 0),
    "JOS": (operator.add, 1),
    "SUS": (operator.sub, 1)
}


def distanta():
    """Funcția citește conținutul fișierului istoric.tuxy și
    calculează distanța dintre punctul de origine și poziția
    curentă a cursorului.
    """
    coordonate = [0, 0]
    instructiuni = []

    with open("istoric.tuxy") as fisier:
        instructiuni = fisier.readlines()

    for linie in instructiuni:
        instructiune, valoare = linie.split()
        operatie, index = INSTRUCTIUNI[instructiune.upper()]
        coordonate[index] = operatie(coordonate[index], int(valoare))

    return (coordonate[0] ** 2 + coordonate[1] ** 2) ** 0.5


if __name__ == "__main__":
    distanta()
