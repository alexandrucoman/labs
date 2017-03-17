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


def determina_cheia1(mesaj):
    for cesar_key in range(0, 26):
        new_mesaj = []

        for litera in mesaj:
            if litera.isalpha():
                new_mesaj.append((chr(97 +
                                      ((ord(litera) + cesar_key) - 97) % 26)))
            else:
                new_mesaj.append(litera)
        text = "".join(new_mesaj)
        print(text)
        response = raw_input("E buna decriptarea y/n \n")
        if response == "y":
            word = text.split(" ", 2)[0]
            return word
    return -1


# After determinaton of a first word we search for each key #

def determina_cheia2(mesaj, word):
    for cesarKey in range(0, 26):
        new_mesaj = []
        for litera in mesaj:
            if litera.isalpha():
                new_mesaj.append((chr(97 +
                                      ((ord(litera) + cesarKey) - 97) % 26)))
            else:
                new_mesaj.append(litera)
        text = "".join(new_mesaj)

        if text.__contains__(word):
            print("Mesajul decodificat este:", text)
            return cesarKey
    return -1


def decripteaza_mesajul(mesaj, word):
    print("mesajul inital este", mesaj)
    currentKey = determina_cheia2(mesaj, word)
    print("Key=", currentKey)


def main():
    """ Main function docstring """
    try:
        fisier = open("mesaje.secret", "r")
        mesaje = fisier.read()
        fisier.close()
    except IOError:
        print("Nu am putut obține mesajele.")
        return

    word = determina_cheia1(mesaje.splitlines()[0])
    print(word)
    print("INCEPEM DECRIPTAREA!!!!")
    for mesaj in mesaje.splitlines():
        decripteaza_mesajul(mesaj, word)


if __name__ == "__main__":
    main()
