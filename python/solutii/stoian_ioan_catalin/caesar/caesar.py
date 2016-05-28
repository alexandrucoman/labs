#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""Împăratul a primit serie de mesaje importante pe care este
important să le descifreze cât mai repede.

Din păcate mesagerul nu a apucat să îi spună împăratul care au fost
cheile alese pentru fiecare mesaj și tu ai fost ales să descifrezi
misterul.

Informații:
    În criptografie, cifrul lui Caesar este o metodă simplă de a cripta
un mesaj prin înlocuirea fiecărei litere cu litera de pe poziția aflată
la un n pași de ea în alfabet (unde este n este un număr întreg cunoscut
"""
# pylint: disable=unused-argument


from __future__ import print_function


def getLit(lit, cifru):
    """
    this function return lit after decrypt
    :param lit:
    :param cifru:
    :return:
    """
    if lit.isalpha():
        litera = ord(lit) + cifru
        if litera > ord('z'):
            character = (ord('a') - 1) + (litera - ord('z'))
        else:
            character = litera
        return chr(character)
    else:
        return lit


def match_cifru(a, b, c, cifru):
    """
    function that check if cifru match with convention
    :param a:
    :param b:
    :param c:
    :param cifru:
    :return:
    """
    if getLit(a, cifru) == "a" and getLit(b, cifru) == "v" and getLit(c, cifru) == "e":
        return True
    return False


def decripteaza_mesajul(mesaj):
    """Funcția va primi un mesaj criptat folosind cifrul lui Caesar și
    va încearca să îl decripteze.
    """
    key = 0
    string = ""
    for cifru in range(1, 26):
        if match_cifru(mesaj[0], mesaj[1], mesaj[2], cifru):
            key = cifru
    for lit in mesaj:
        c = getLit(lit, key)
        string += c
    print(string)


def main():
    """ Main function docstring """
    try:
        fisier = open("../../../date_intrare/mesaje.secret", "r")
        mesaje = fisier.read()
        fisier.close()
    except IOError:
        print("Nu am putut obține mesajele.")
        return

    for mesaj in mesaje.splitlines():
        decripteaza_mesajul(mesaj)


if __name__ == "__main__":
    main()
