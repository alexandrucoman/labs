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


def gaseste_unic_1(istoric):
    """Găsește elementul unic.

    Funcția primește o listă cu elemente numerice și trebuie
    să returneze elementul care nu este duplicat.

    Exemple:
        1 2 3 2 1 - 3
        1 1 1 2 2 - 1
    """

    dfreq = {}  # dictionar de frecvente
    for element in istoric:
        # incercam sa gasim indexul elementului in dictionarul de frecventa
        if element-1 in dfreq:
            # elementul exista, deci incrementam numarul de aparitii
            dfreq[element - 1] += 1
        else:  # cand elementul nu este gasit, il adaugam
            # adaugam 1 in pozitia corespunzatoare din dictionarul de frecventa
            dfreq[element - 1] = 1

    for element in istoric:
        # daca elementul apare de un numar impar de ori
        if dfreq[element - 1] % 2 != 0:
            return element  # acela este elementul unic


def gaseste_unic_2(istoric):
    """Găsește elementul unic.

    Funcția primește o listă cu elemente numerice și trebuie
    să returneze elementul care nu este duplicat.

    Exemple:
        1 2 3 2 1 - 3
        1 1 1 2 2 - 1
    """

    unic = istoric.pop()
    while istoric:  # cat timp nu s-a terminat lista
        unic ^= istoric.pop()  # XOR intre toate elementele

    return unic  # ramane elementul unic

if __name__ == "__main__":
    assert gaseste_unic_1([1, 2, 3, 2, 1]) == 3
    assert gaseste_unic_1([1, 1, 1, 2, 2]) == 1

    assert gaseste_unic_2([1, 2, 3, 2, 1]) == 3
    assert gaseste_unic_2([1, 1, 1, 2, 2]) == 1
