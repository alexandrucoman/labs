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
import operator

def gaseste2(istoric):
    for i in xrange(len(istoric)-1):
        istoric[i+1] ^= istoric[i]
    return istoric[len(istoric)-1]
def gaseste(istoric):
    return reduce(operator.xor,istoric)

if __name__ == "__main__":
    assert gaseste2([1, 2, 3, 2, 1]) == 3
    assert gaseste2([1, 1, 1, 2, 2]) == 1
