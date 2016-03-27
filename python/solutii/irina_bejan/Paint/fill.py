#!/usr/bin/env python
# *-* coding: UTF-8 *-*

"""Tuxy dorește să împlementeze un nou paint pentru consolă.
În timpul dezvoltării proiectului s-a izbit de o problemă
pe care nu o poate rezolva singur și a apelat la ajutorul tău.
El dorește să adauge o unealtă care să permită umplerea unei
forme închise.
Exemplu:
Pornim de la imaginea inițială reprezentată mai jos, trebuie să
umplem formele în care se află "x":
  |-----*------|          |******------|         |************|
  |--x--*------|          |******------|         |************|
  |******------|  ----->  |******------|  -----> |************|
  |-----******-|          |-----******-|         |-----*******|
  |-----*---*--|          |-----*---*--|         |-----*---***|
  |-----*---*-x|          |-----*---*--|         |-----*---***|
"""
from __future__ import print_function

DLIN = [-1, 1, 0, 0]
DCOL = [0, 0, -1, 1]


def verifica_punct(punct, linii, coloane):
    """Verifica daca un anumit punct se afla in interiorul imaginii
    """
    return 0 <= punct[0] < linii and 0 <= punct[1] < coloane


def afisare_matrice(imagine):
    """Afiseaza matricea rezultata."""

    for linie in imagine:
        for caracter in linie:
            print (caracter, end="")
        print ()
    print('\n')


def umple_forma(imagine, punct):
    """Funcția primește reprezentarea imaginii și coordonatele unui
    punct.
    În cazul în care punctul se află într-o formă închisă trebuie să
    umple forma respectivă cu caracterul "*"
    """

    linii = len(imagine)
    if linii:
        coloane = len(imagine[0])
    else:
        raise ValueError('Imaginea nu contine linii si coloane.')

    if verifica_punct(punct, linii, coloane):
        lpunct = punct[0]
        cpunct = punct[1]

        if imagine[lpunct][cpunct] == '-':
            imagine[lpunct][cpunct] = '*'
            for index in range(0, 4):
                lnou = lpunct + DLIN[index]
                cnou = cpunct + DCOL[index]
                umple_forma(imagine, (lnou, cnou))


def main():
    """  Main function docstring """
    imaginea = [
        ["-", "-", "-", "-", "-", "*", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "-", "-", "-", "-", "-"],
        ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "*", "-", "-", "*", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "*", "-", "-", "*", "-"],
    ]
    umple_forma(imaginea, (1, 3))
    afisare_matrice(imaginea)
    umple_forma(imaginea, (5, 11))
    afisare_matrice(imaginea)

if __name__ == "__main__":
    main()
