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
# pylint: disable=unused-argument


def verifica_expresia(paranteze):
    """Verifică validitatea expresiei primite.

    Verifică dacă toate parantezele din expresie
    sunt folosite corespunzător.
    """
    lista = []
    for paranteza in paranteze:
        if paranteza == "[" or paranteza == "(":
            lista.append(paranteza)
        else:
            if (paranteza == ")" or paranteza == "]") and not lista:
                return False
            if paranteza == ")" and lista[-1] != "(":
                return False
            else:
                if paranteza == "]" and lista[-1] != "[":
                    return False
                else:
                    lista.pop()
    return True


if __name__ == "__main__":
    assert verifica_expresia("[()[]]"), "Probleme la expresia 1"
    assert verifica_expresia("()()[][]"), "Probleme la expresia 2"
    assert verifica_expresia("([([])])"), "Probleme la expresia 3"
    assert not verifica_expresia("[)()()()"), "Probleme la expresia 4"
    assert not verifica_expresia("][[()][]"), "Probleme la expresia 5"
    assert not verifica_expresia("([()]))"), "Probleme la expresia 6"
    assert not verifica_expresia("([)]"), "Probleme la expresia 7"
