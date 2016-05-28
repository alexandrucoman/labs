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
  |-----*---*-x|          |-----*---*-x|         |-----*---***|

"""
# pylint: disable=unused-argument


def checkifpointisokay(imagine, punct):
    "Verifica daca punctul primit ca paramestru este valid"
    if punct[0] >= len(imagine) or punct[0] < 0:
        return False
    if punct[1] >= len(imagine[0]) or punct[1] < 0:
        return False
    if imagine[punct[0]][punct[1]] == "*":
        return False
    return True

def umple_forma(imagine, punct):
    """Funcția primește reprezentarea imaginii și coordonatele unui
    punct.

    În cazul în care punctul se află într-o formă închisă trebuie să
    umple forma respectivă cu caracterul "*"
    """
    if not checkifpointisokay(imagine, punct):
        return False
    imagine[punct[0]][punct[1]] = "*"
    umple_forma(imagine, (punct[0]+1, punct[1]))
    umple_forma(imagine, (punct[0]-1, punct[1]))
    umple_forma(imagine, (punct[0], punct[1]+1))
    umple_forma(imagine, (punct[0], punct[1]-1))
    return True


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
    umple_forma(imaginea, (5, 11))
    for linie in imaginea:
        print(''.join(linie))


if __name__ == "__main__":
    main()
