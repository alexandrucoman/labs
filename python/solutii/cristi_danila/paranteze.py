#!/usr/bin/env python
# *-* coding: UTF-8 *-*
# pylint: disable=unused-argument

def reverse(bracket):
    if bracket == "(":
        return ")"
    elif bracket == ")":
        return "("
    elif bracket == "]":
        return "["
    elif bracket == "[":
        return "]"
    elif bracket == "{":
        return "}"
    else:
        return "{"

def verifica_expresia(paranteze):
    bracket_stack = []

    for bracket in paranteze:
        if bracket == "(" or bracket == "[" or bracket == "{":
            bracket_stack.append(bracket)
        else:
            if len(bracket_stack) == 0:
                return False

            if bracket != reverse(bracket_stack[-1]):
                return False
            bracket_stack.pop(-1)
    return True

if __name__ == "__main__":
    assert verifica_expresia("[()[]]"), "Probleme la expresia 1"
    assert verifica_expresia("()()[][]"), "Probleme la expresia 2"
    assert verifica_expresia("([([])])"), "Probleme la expresia 3"
    assert not verifica_expresia("[)()()()"), "Probleme la expresia 4"
    assert not verifica_expresia("][[()][]"), "Probleme la expresia 5"
    assert not verifica_expresia("([()]))"), "Probleme la expresia 6"
    assert not verifica_expresia("([)]"), "Probleme la expresia 7"
