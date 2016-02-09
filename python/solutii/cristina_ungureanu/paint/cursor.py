#!/usr/bin/env python
# *-* coding: UTF-8 *-*

"""Stabileste distanta si pozitia fata de origine."""

import math


def este_instructiune(instr):
    """Stabileste daca este instructiune."""
    dictionar = {'STANGA', 'DREAPTA', 'SUS', 'JOS'}
    if instr in dictionar:
        return True
    else:
        return False


def distanta():
    """Calculeaza distanta fata de origine dupa mutari."""
    fisier = open("istoric.tuxy", "r")
    istoric = fisier.read()
    x_coord = 0
    y_coord = 0
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
                x_coord -= int(instructiune[1])
            if instructiune[0] == "SUS":
                y_coord += int(instructiune[1])
            if instructiune[0] == "DREAPTA":
                x_coord += int(instructiune[1])
            if instructiune[0] == "JOS":
                y_coord -= int(instructiune[1])
    fisier.close()
    print "Pozitie: ", x_coord, y_coord
    return math.sqrt(x_coord ** 2+y_coord ** 2)


if __name__ == "__main__":
    print distanta()

