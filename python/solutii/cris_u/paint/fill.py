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
  |-----*----*-|          |-----*----*-|         |-----*----**|
  |-----*----*x|          |-----*----*-|         |-----*----**|

"""


def umple(imagine, punct):
    if punct[0] >= 0 and punct[1] >= 0 and punct[0] < len(imagine)
    and punct[1] < len(imagine[0]) and imagine[punct[0]][punct[1]] != "*":
        imagine[punct[0]][punct[1]] = "*"
        umple(imagine, (punct[0]-1, punct[1]))
        umple(imagine, (punct[0]+1, punct[1]))
        umple(imagine, (punct[0], punct[1]-1))
        umple(imagine, (punct[0], punct[1]+1))


def main():
    imaginea = [
        ["-", "-", "-", "-", "-", "*", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "-", "-", "-", "-", "-"],
        ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "*", "-", "-", "*", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "*", "-", "-", "*", "-"],
    ]

    umple(imaginea, (1, 3))
    umple(imaginea, (5, 11))
    for i in range(0, len(imaginea)):
        for j in range(0, len(imaginea[0])):
            print imaginea[i][j],
        print '\n'


if __name__ == "__main__":
    main()

