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
    """Verifică dacă toate parantezele sunt folosite corespunzător."""
    squ = 0
    rou = 0
    for index in enumerate(expresie):
        item = expresie[index]

        if item == "[":
            squ += 1
        elif item == "]":
            squ -= 1
        elif item == "(":
            rou += 1
        elif item == ")":
            rou -= 1

        if squ < 0 or rou < 0:
            print expresie, "is wrong because of -1 on either squ or rou!"
            return False
        # from index 1 onwards, check mismatched parantheses
        if index > 0:
            last_item = expresie[index - 1]
            if item == ")" and last_item == "[":
                print expresie, "is wrong because [)"
                return False
            if item == "]" and last_item == "(":
                print item, last_item
                print expresie, "is wrong because (]"
                return False

    print expresie, "is okay."
    return True


if __name__ == "__main__":
    assert este_corect("[()[]]"), "Probleme la expresia 1"
    assert este_corect("()()[][]"), "Probleme la expresia 2"
    assert este_corect("([([])])"), "Probleme la expresia 3"
    assert not este_corect("[)()()()"), "Probleme la expresia 4"
    assert not este_corect("][[()][]"), "Probleme la expresia 5"
    assert not este_corect("([()]))"), "Probleme la expresia 6"
    assert not este_corect("([)]"), "Probleme la expresia 7"
