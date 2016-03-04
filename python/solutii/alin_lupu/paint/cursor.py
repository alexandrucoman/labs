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

from __future__ import print_function
from math import sqrt


def distanta():
    """
    Calculează distanța dintre origine și poziția curentă.
    Funcția citește conținutul fișierului istoric.tuxy și
    calculează distanța dintre punctul de origine și poziția
    curentă a cursorului.
    """
    try:
        f_in = open("../../../date_intrare/istoric.tuxy", "r")
        instrs = f_in.read().splitlines()
        f_in.close()

        x_pos, y_pos = 0, 0
        for instr in instrs:
            direc = instr.split(' ')
            if direc[0] and direc[0] in ["SUS", "JOS", "STANGA", "DREAPTA"]:
                if direc[0] == "SUS":
                    y_pos += int(direc[1])
                if direc[0] == "JOS":
                    y_pos -= int(direc[1])
                if direc[0] == "STANGA":
                    x_pos -= int(direc[1])
                if direc[0] == "DREAPTA":
                    x_pos += int(direc[1])
            else:
                return 0
    except IOError:
        print("FileNotFound")
        return
    return sqrt(pow(0 - x_pos, 2) + pow(0 - y_pos, 2))


if __name__ == "__main__":
    print(distanta())
