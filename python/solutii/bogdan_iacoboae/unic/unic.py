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

def gaseste_unic(istoric):
    unic = istoric.pop(0)
    for index in istoric:
        unic ^= index
    return unic


if __name__ == "__main__":
    # lista = [1, 2, 3, 2, 1]
    lista = [1, 1, 1, 2, 2]
    print "Lista id-uri cercetatori: ",
    for index in lista :
        print index,
    print""
    print "Cercetatorul cu id-ul %s este cercetatorul care sta peste program" % (gaseste_unic(lista))

