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


def decripteaza_mesajul(mesaj):
    """Funcția va primi un mesaj criptat folosind cifrul lui Caesar și
    va încearca să îl decripteze.
    """
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    key = ord(mesaj[0]) - 97
    decodif = ""
    for lit in mesaj:
        if lit in alfabet:
            decodif = "".join([decodif, alfabet[alfabet.find(lit) - key]])
        else:
            decodif = "".join([decodif, lit])
    print decodif


def main():
    """ Main function docstring """
    try:
        fisier = open("../../../date_intrare/mesaje.secret", "r")
        mesaje = fisier.read()
        fisier.close()
    except IOError:
        print "Nu am putut obține mesajele."
        return

    for mesaj in mesaje.splitlines():
        decripteaza_mesajul(mesaj)

if __name__ == "__main__":
    main()
