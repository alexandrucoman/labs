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


def decripteaza_mesajul(mesaj):
    """Funcția va primi un mesaj criptat folosind cifrul lui Caesar și
    va încearca să îl decripteze.
    """
    key = 0;
    decodedMessage = ""
    dictionary = "abcdefghijklmnopqrstuvwxyz"
    keyPhrase  = "ave caesar"
    for displacement in range(1,13):
        """print("Line for displacement %d" % displacement)"""
        tempPhrasePos = ""
        tempPharseNeg = ""
        messageHead = list(mesaj[0:len(keyPhrase)]);
        for character in messageHead:
            if dictionary.find(character) > 0:
                if chr(ord(character) + displacement) == keyPhrase[messageHead.index(character)]:
                    key = displacement
                elif chr(ord(character)-displacement) == keyPhrase[messageHead.index(character)]:
                    key = -displacement
    print(key)
    for character in mesaj:
        index = dictionary.find(character)
        if index > 0:
            decodedMessage += dictionary[index + key]
        else:
            decodedMessage += character
    print(decodedMessage)


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
        print("Line to be deciphred: ", mesaj)
        decripteaza_mesajul(mesaj)
        print()

if __name__ == "__main__":
    main()
