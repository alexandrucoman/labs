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


def cb_este_corect(_):
    """Verifică dacă toate parantezele din expresie
    sunt folosite corespunzător."""
    pass


if __name__ == "__main__":
    assert cb_este_corect("[()[]]"), "Probleme la expresia 1"
    assert cb_este_corect("()()[][]"), "Probleme la expresia 2"
    assert cb_este_corect("([([])])"), "Probleme la expresia 3"
    assert not cb_este_corect("[)()()()"), "Probleme la expresia 4"
    assert not cb_este_corect("][[()][]"), "Probleme la expresia 5"
    assert not cb_este_corect("([()]))"), "Probleme la expresia 6"
    assert not cb_este_corect("([)]"), "Probleme la expresia 7"
