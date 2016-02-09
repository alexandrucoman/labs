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
    memo = []
    for i in range(len(expresie)):
        if expresie[i] not in '([)]':
            return False
        else:
            if expresie[i] == '(' or expresie[i] == '[':
                memo.append(expresie[i])
            else:
                if expresie[i] == ')':
                    if len(memo) > 0 and memo[len(memo)-1] == '(':
                        a = memo.pop()
                        if '(' != a:
                            print "Elimin altceva!? ~( :", a
                    else:
                        return False
                else:
                    if expresie[i] == ']':
                        if len(memo) > 0 and memo[len(memo)-1] == '[':
                            a = memo.pop()
                            if '[' != a:
                                print "Elimin altceva!? ~[ :", a
                        else:
                            return False
    else:
        if len(memo) == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    assert not este_corect("[9]")
    assert not este_corect("[")
    assert este_corect("[()[]]"), "Probleme la expresia 1"
    assert este_corect("()()[][]"), "Probleme la expresia 2"
    assert este_corect("([([])])"), "Probleme la expresia 3"
    assert not este_corect("[)()()()"), "Probleme la expresia 4"
    assert not este_corect("][[()][]"), "Probleme la expresia 5"
    assert not este_corect("([()]))"), "Probleme la expresia 6"
    assert not este_corect("([)]"), "Probleme la expresia 7"

