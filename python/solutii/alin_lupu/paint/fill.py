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

def print_forme(imagine, punct):
    """Funcţia afişează matricea imagine împreună cu punctul din
    parametrul 'punct', notat cu x
    """

    for i in range(len(imagine)):
        for j in range(len(imagine[0])):
            if punct:
                if i == punct[0] and j == punct[1]:
                    imagine[i][j] = 'x'
            print(imagine[i][j], " ", end="")
        print("\n")
    print("\n\n")

def umple_forma(imagine, punct):
    """Funcția primește reprezentarea imaginii și coordonatele unui
    punct.

    În cazul în care punctul se află într-o formă închisă trebuie să
    umple forma respectivă cu caracterul "*"
    """

    if imagine[punct[0]][punct[1]] == '*':
        return
    imagine[punct[0]][punct[1]] = '*'

    if punct[1] < (len(imagine[0]) - 1):
        umple_forma(imagine, (punct[0], punct[1] + 1))
    if punct[1] >= 1:
        umple_forma(imagine, (punct[0], punct[1] - 1))
    if punct[0] < (len(imagine) - 1):
        umple_forma(imagine, (punct[0] + 1, punct[1]))
    if punct[0] >= 1:
        umple_forma(imagine, (punct[0] - 1, punct[1]))
    return imagine



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

    print_forme(imaginea, (1, 3))
    umple_forma(imaginea, (1, 3))
    print_forme(imaginea, (1, 3))

    print_forme(imaginea, (5, 11))
    umple_forma(imaginea, (5, 11))
    print_forme(imaginea, (5, 11))

if __name__ == "__main__":
    main()