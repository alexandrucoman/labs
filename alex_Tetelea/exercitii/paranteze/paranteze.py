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
    n = len(expresie)
    while True:
        for i in xrange(len(expresie) - 1):
            if expresie[i] == '[' and expresie[i + 1] == ']' or expresie[i] == '{' and expresie[i + 1] == '}' or \
                                    expresie[i] == '(' and expresie[i + 1] == ')':
                expresie = expresie[:i] + expresie[(i+2):]
                break
        if len(expresie)<1:
            break
        if n == len(expresie):
            return False
        n = len(expresie)

    if len(expresie)>0:
        return False
    else:
        return True


if __name__ == "__main__":
    assert este_corect("[()[]]"), "Probleme la expresia 1"
    assert este_corect("()()[][]"), "Probleme la expresia 2"
    assert este_corect("([([])])"), "Probleme la expresia 3"
    assert not este_corect("[)()()()"), "Probleme la expresia 4"
    assert not este_corect("][[()][]"), "Probleme la expresia 5"
    assert not este_corect("([()]))"), "Probleme la expresia 6"
    assert not este_corect("([)]"), "Probleme la expresia 7"
