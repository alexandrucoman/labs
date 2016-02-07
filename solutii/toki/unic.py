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
from collections import Counter


def gaseste(istoric):
    """Funcția primește o listă cu elemente numerice și trebuie
    să returneze elementul care nu este duplicat.

    Exemple:
        1 2 3 2 1 - 3
        1 1 1 2 2 - 1
    """

    for i in range(0, 10):
        if istoric.count(i) % 2 == 1:
            print("Cercatatorul numarul %i sta peste program! \n" %i)
            return i
    pass


if __name__ == "__main__":
    assert gaseste([1, 2, 3, 2, 1]) == 3
    assert gaseste([1, 1, 1, 2, 2]) == 1
