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
visited = []


def umple(imagine, punct):
    to_visit = []
    global visited
    if visited is None:
        visited = []
    if punct in visited:
        return
    visited.append(punct)
    imagine[punct[0]][punct[1]] = '*'
    if punct[0] < 0 or punct[0] > len(imagine):
        return
    # jos
    if punct[1] + 1 < len(imagine) - 1 and imagine[punct[0] + 1][punct[1]] == '-':
        to_visit.append((punct[0] + 1, punct[1]))
    if punct[1] + 1 < len(imagine[punct[0]]) - 1 and imagine[punct[0]][punct[1] + 1] == '-':
        to_visit.append((punct[0], punct[1] + 1))
    if punct[0] > 0 and imagine[punct[0] - 1][punct[1]] == '-':
        to_visit.append((punct[0] - 1, punct[1]))
    if punct[1] > 0 and imagine[punct[0]][punct[1] - 1] == '-':
        to_visit.append((punct[0], punct[1] - 1))
    for each in [x for x in to_visit if x not in visited]:
        umple(imagine, each)


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
    pass


if __name__ == "__main__":
    main()
