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

TESTING = 1
# pentru afisari intermediare in scop de testare


def umple_forma(imagine, punct):
    """Funcția primește reprezentarea imaginii și coordonatele unui
    punct.

    În cazul în care punctul se află într-o formă închisă trebuie să
    umple forma respectivă cu caracterul "*"
    """
    stiva = list()
    stiva.append(punct)
    imag_x = len(imagine)
    imag_y = len(imagine[0])
    comp_x = 0
    comp_y = 1
    while len(stiva):
        pct = stiva.pop()
        if imagine[pct[comp_x]][pct[comp_y]] == "-":
            imagine[pct[comp_x]][pct[comp_y]] = "*"
            if pct[comp_x] + 1 < imag_x:
                stiva.append((pct[comp_x] + 1, pct[comp_y]))
            if pct[comp_x] - 1 >= 0:
                stiva.append((pct[comp_x] - 1, pct[comp_y]))
            if pct[comp_y] + 1 < imag_y:
                stiva.append((pct[comp_x], pct[comp_y] + 1))
            if pct[comp_y] - 1 >= 0:
                stiva.append((pct[comp_x], pct[comp_y] - 1))


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

    def afiseaza():
        ''' functie pentru afisarea imaginii - pentru test '''
        for linie in imaginea:
            for punct in linie:
                print punct,
            print
        print
    if TESTING:
        afiseaza()
    umple_forma(imaginea, (1, 3))
    if TESTING:
        afiseaza()
    umple_forma(imaginea, (5, 11))
    if TESTING:
        afiseaza()


if __name__ == "__main__":
    main()
