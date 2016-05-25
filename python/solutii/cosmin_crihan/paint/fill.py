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
# pylint: disable=unused-argument


def umple_forma(imagine, punct):
    """Funcția primește reprezentarea imaginii și coordonatele unui
    punct.

    În cazul în care punctul se află într-o formă închisă trebuie să
    umple forma respectivă cu caracterul "*"
    """

    # validam coordonatele punctului curent (sa nu depaseasca dimensiunile imaginii)
    if punct[0] >= 0 and punct[0] <= len(imagine) - 1 and punct[1] >= 0 and punct[1] <= len(imagine[0]) - 1 \
        and imagine[punct[0]][punct[1]] != "*":  # si sa nu fie "perete" acolo
        imagine[punct[0]][punct[1]] = "*"  # adaugam steluta
        # si apelam recursiv functia de umplere in cele 4 directii
        umple_forma(imagine, (punct[0] - 1, punct[1]))  # STANGA
        umple_forma(imagine, (punct[0] + 1, punct[1]))  # DREAPTA
        umple_forma(imagine, (punct[0], punct[1] + 1))  # SUS
        umple_forma(imagine, (punct[0], punct[1] - 1))  # JOS

def afisare_imagine(imaginea):
    for linie in imaginea:
        for element in linie:
            print(element),
        print("\n")

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

    print("Imaginea inainte de umplere: \n")
    afisare_imagine(imaginea)

    umple_forma(imaginea, (1, 3))

    print("Imaginea dupa prima umplere: \n")
    afisare_imagine(imaginea)

    umple_forma(imaginea, (5, 11))

    print("Imaginea dupa a doua umplere: \n")
    afisare_imagine(imaginea)


if __name__ == "__main__":
    main()
