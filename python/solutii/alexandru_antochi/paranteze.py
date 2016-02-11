#!/usr/bin/env python
# *-* coding: UTF-8 *-*

"""Tuxy scrie în fiecare zi foarte multe formule matematice.

Pentru că formulele sunt din ce în ce mai complicate trebuie
să folosească o serie de paranteze și a descoperit că cea
mai frecventă problemă a lui este că nu toate parantezele
sunt folosite cum trebuie.

Pentru acest lucru a apelat la ajutorul tău.

Câteva exemple:
    - []        este bine
    - []()      este bine
    - [()()]    este bine
    - ][        nu este bine
    - (][][)    nu este bine
    - [)]()[(]  nu este bine
"""


def este_corect(expresie):
    """Verifică dacă toate parantezele sunt folosite corespunzător,
    prin expresie.
    """
    stiva = []
    stiva.append(expresie[0])
    for i in range(1, len(expresie)):
        stiva.append(expresie[i])
        if stiva[len(stiva) - 2] == '(' and stiva[len(stiva) - 1] == ')':
            stiva.pop()
            stiva.pop()
        elif stiva[len(stiva) - 2] == '[' and stiva[len(stiva) - 1] == ']':
            stiva.pop()
            stiva.pop()
    return not stiva


if __name__ == "__main__":
    assert este_corect("[()[]]"), "Probleme la expresia 1"
    assert este_corect("()()[][]"), "Probleme la expresia 2"
    assert este_corect("([([])])"), "Probleme la expresia 3"
    assert not este_corect("[)()()()"), "Probleme la expresia 4"
    assert not este_corect("][[()][]"), "Probleme la expresia 5"
    assert not este_corect("([()]))"), "Probleme la expresia 6"
    assert not este_corect("([)]"), "Probleme la expresia 7"
