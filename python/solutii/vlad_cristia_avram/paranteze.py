"""Rezolvarea pentru problema paranteze"""
from __future__ import print_function


def verifica_expresia(paranteze):
    """Functia de verificare"""
    mesaj = []
    try:
        for element in paranteze:
            if element == "[" or element == "(":
                mesaj.append(element)
            elif element == "]" or element == ")":
                try:
                    test = mesaj.pop(len(mesaj)-1)
                except IndexError:
                    return False
                if abs(ord(test)-ord(element)) == 1 or\
                   abs(ord(test)-ord(element)) == 2:
                    pass
                else:
                    return False
            else:
                print("Ati introdus un text gresit")
                return
    except TypeError:
        print("Nu ati introdus niciun text")
        return
    if mesaj:
        return False
    else:
        return True


if __name__ == "__main__":
    verifica_expresia("[()[]]")
    verifica_expresia("()()[][]")
    verifica_expresia("([([])])")
    verifica_expresia("[)()()()")
    verifica_expresia("][[()][]")
    verifica_expresia("([()]))")
    verifica_expresia("([)]")
