#!/usr/bin/env python
# *-* coding: UTF-8 *-*

"""În laboratorul lui Tuxy to?i cercetatorii au asignat un id
de utilizator.

Pentru fiecare cercetator se salveaza într-o lista de fiecare
data când a deschis u?a (fie pentru a intra, fie pentru a ie?i).

Tuxy suspecteaza ca cineva ramâne tot timpul dupa program ?i
ar dori sa scrie un script care sa îi verifice teoria, dar
nu a reu?it pentru ca algoritmul sau era prea costisitor pentru
sistem.

Cerin?e:
    I. Gase?te cercetatorul ce sta peste program dupa o singura
    parcurgere a listei
    II. Gase?te cercetatorul ce sta peste program dupa o singura
    parcurgere a listei ?i fara a aloca memorie suplimentara.
"""
"""Func?ia prime?te o lista cu elemente numerice ?i trebuie
    sa returneze elementul care nu este duplicat.

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
    for i in xrange(1, len(istoric)):
        unic ^= istoric[i]
    return unic


if __name__ == "__main__":
    gaseste([1, 2, 3, 2, 1]) == 3
    gaseste([1, 1, 1, 2, 2]) == 1
