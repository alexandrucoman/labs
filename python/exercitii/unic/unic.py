#!/usr/bin/env python
# *-* coding: UTF-8 *-*

"""În laboratorul lui Tuxy toți cercetătorii au asignat un id
de utilizator.

Pentru fiecare cercetător se salvează într-o listă de fiecare
dată când a deschis ușa (fie pentru a intra, fie pentru a ieși).

Tuxy suspectează că cineva rămâne tot timpul după program și
ar dori să scrie un script care să îi verifice teoria, dar
nu a reușit pentru că algoritmul său era prea costisitor pentru
sistem.

Cerințe:
    I. Găsește cercetătorul ce stă peste program după o singură
    parcurgere a listei
    II. Găsește cercetătorul ce stă peste program după o singură
    parcurgere a listei și fără a aloca memorie suplimentară.
"""
"""Funcția primește o listă cu elemente numerice și trebuie
    să returneze elementul care nu este duplicat.

    Exemple:
        1 2 3 2 1 - 3
        1 1 1 2 2 - 1
"""


def gaseste(istoric):
    '''
    :param istoric: istoric is the list of elements
    :return: the unique element from the list
    '''
    unic = istoric[0]
    for i in xrange(1,len(istoric)):
        unic ^= istoric[i]
    return unic


if __name__ == "__main__":
     gaseste([1, 2, 3, 2, 1]) == 3
     gaseste([1, 1, 1, 2, 2]) == 1
