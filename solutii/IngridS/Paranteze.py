"""Rezolvarea problemei Paranteze"""

#!/usr/bin/env python
# *-* coding: UTF-8 *-*
def este_corect(expresie):
    """Determinarea validitatii expresiei"""
    stiva = list()
    for caracter in expresie:
        if caracter in "([":
            stiva.append(caracter)
        else:
            if caracter == ")":
                if not stiva or stiva.pop() == "[":
                    print "Nu este corect"
                    return 0
            if caracter == "]":
                if not stiva or stiva.pop() == "(":
                    print "Nu este corect"
                    return 0
    if not stiva:
        print "Este corect"
        return 1
    else:
        return 0

if __name__ == "__main__":
    print este_corect("[(())]")


