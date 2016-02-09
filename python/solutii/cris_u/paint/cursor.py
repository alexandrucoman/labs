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


def este_instructiune(instr):
    if (instr == 'STANGA' or instr == 'SUS' or
       instr == 'DREAPTA' or instr == 'JOS'):
        return True
    else:
        return False


def distanta():
    fisier = open("istoric.tuxy", "r")
    istoric = fisier.read()
    x = 0
    y = 0
    for linie in istoric.splitlines():
        instructiune = linie.split(' ')
        if (len(instructiune) < 2 or
           not este_instructiune(instructiune[0]) or
           not instructiune[1].isdigit()):
            print "Fisier INVALID!"
            fisier.close()
            return -1
        else:
            if instructiune[0] == "STANGA":
                x -= int(instructiune[1])
            if instructiune[0] == "SUS":
                y += int(instructiune[1])
            if instructiune[0] == "DREAPTA":
                x += int(instructiune[1])
            if instructiune[0] == "JOS":
                y -= int(instructiune[1])
    fisier.close()
    print "Pozitie: ", x, y
    return math.sqrt(x**2+y**2)


if __name__ == "__main__":
    print distanta()

