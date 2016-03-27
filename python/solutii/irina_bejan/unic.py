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


def gaseste_unic(istoric):
    """Găsește elementul unic.
    Funcția primește o listă cu elemente numerice și trebuie
    să returneze elementul care nu este duplicat.
    Exemple:
        1 2 3 2 1 - 3
        1 1 1 2 2 - 1
    """
    dic = {}
    for number in istoric:
        dic[number] = dic.setdefault(number, 0) + 1
    for key, value in dic.iteritems():
        if value % 2 == 1:
            return key


def gaseste_unic_versiune_trei(istoric):
    """Găsește elementul unic in o(n) timp si o(1) memorie suplimentara
    Funcția primește o listă cu elemente numerice și trebuie
    să returneze elementul care nu este duplicat.
    Exemple:
        1 2 3 2 1 - 3
        1 1 1 2 2 - 1
    """
    for element in istoric:
        istoric[abs(element)] *= (-1)
    for element in istoric:
        if istoric[abs(element)] < 0:
            return element


def gaseste_unic_versiune_doi(istoric):
    """Găsește elementul unic in o(nlgn) timp si o(1) memorie suplimentara
    Funcția primește o listă cu elemente numerice și trebuie
    să returneze elementul care nu este duplicat.
    Exemple:
        1 2 3 2 1 - 3
        1 1 1 2 2 - 1
    """
    istoric.sort()
    length = len(istoric)

    contor = 1
    index = 1

    while index < length:
        if istoric[index] == istoric[index-1]:
            contor += 1
        else:
            if contor % 2 == 1:
                return istoric[index-1]
            contor = 1
        index += 1

    if contor % 2 == 1:
        return istoric[length-1]


if __name__ == "__main__":
    assert gaseste_unic_versiune_trei([1, 2, 3, 2, 1]) == 3
    assert gaseste_unic_versiune_trei([1, 1, 1, 2, 2]) == 1
