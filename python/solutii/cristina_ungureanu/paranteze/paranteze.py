#!/usr/bin/env python
# *-* coding: UTF-8 *-*

"""Stabileste daca o expresie de paranteze este corecta."""


def este_corect(expresie):
    """Apreciaza corectitudinea expresiei."""
    memo = []
    for i in range(len(expresie)):
        if expresie[i] not in '([)]':
            return False
        if expresie[i] == '(' or expresie[i] == '[':
            memo.append(expresie[i])
        if expresie[i] == ')':
            if memo and memo[len(memo)-1] == '(':
                memo.pop()
            else:
                return False
        if expresie[i] == ']':
            if memo and memo[len(memo)-1] == '[':
                memo.pop()
            else:
                return False
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

