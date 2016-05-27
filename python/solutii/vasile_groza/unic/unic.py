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
from array import array


def gaseste_unic(istoric):
    """Găsește elementul unic.

    Funcția primește o listă cu elemente numerice și trebuie
    să returneze elementul care nu este duplicat.

    Exemple:
        1 2 3 2 1 - 3
        1 1 1 2 2 - 1
    """
    accesari = array('i', (0 for i in range(0, 10)))
    id_hardworker = -1
    for index in istoric:
        accesari[index] = accesari[index] + 1

    for index in range(0, len(accesari)):
        if accesari[index] % 2 == 1:
            id_hardworker = index
    print (id_hardworker)
    return id_hardworker


def gaseste_unic_2(istoric):
    """Găsește elementul unic.

    Funcția primește o listă cu elemente numerice și trebuie
    să returneze elementul care nu este duplicat.

    Exemple:
        1 2 3 2 1 - 3
        1 1 1 2 2 - 1
        :type istoric: object
    """

    """
    print type(istoric)
    pass
    """
    id_hardworker = istoric.pop()
    while istoric:
        id_hardworker ^= istoric.pop();
    print (id_hardworker)
    return id_hardworker


if __name__ == "__main__":
    assert gaseste_unic_2([1, 2, 3, 2, 1]) == 3
    assert gaseste_unic_2([1, 1, 1, 2, 2]) == 1
