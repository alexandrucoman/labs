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
# pylint: disable=unused-argument


def sxor(s1, s2):
    """
    Aceasta functie este xor.
    :param s1:
    :param s2:
    :return:
    """
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))


def gaseste_unic(istoric):
    """Găsește elementul unic.

    Funcția primește o listă cu elemente numerice și trebuie
    să returneze elementul care nu este duplicat.

    Exemple:
        1 2 3 2 1 - 3
        1 1 1 2 2 - 1
    :param istoric:
    """
    rezultat = istoric[0]
    for number in istoric[1:]:
        rezultat = rezultat ^ number

    return rezultat
    pass


if __name__ == "__main__":
    assert gaseste_unic([1, 2, 3, 2, 1]) == 3
    assert gaseste_unic([1, 1, 1, 2, 2]) == 1
