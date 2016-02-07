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

from __future__ import print_function

ALFABET = list('abcdefghijklmnopqrstuvwxyz')


def _caesar(mesaj, cheie):
    """Folosim cifrul lui Caesar pentru a descifra mesajul."""
    cifru = []
    for litera in mesaj.lower():
        if litera not in ALFABET:
            cifru.append(litera)
        else:
            # (ALFABET.index(litera) + cheie) % 26
            # Poate fi înlocuit cu `ord(litera) - 97` unde 97 este
            # valoare ascii a caracterului `a`.
            cifru.append(ALFABET[(ALFABET.index(litera) + cheie) % 26])

    return "".join(cifru)


def decripteaza(mesaj):
    """Funcția va primi un mesaj criptat folosind cifrul lui Caesar și
    va încearca să îl decripteze.
    """
    for cheie in range(0, 27):
        mesaj_decriptat = _caesar(mesaj, cheie)
        if "ave" in mesaj_decriptat:
            print("[i] Mesajul este: %s" % mesaj_decriptat)
            return
    print("[x] Nu am reusit sa descifrez mesajul: %s" % mesaj)


def main():
    """Incercam sa decriptam mesajele primite."""
    try:
        fisier = open("mesaje.secret", "r")
        mesaje = fisier.read()
        fisier.close()
    except IOError:
        print("Nu am putut obține mesajele.")
        return

    for mesaj in mesaje.splitlines():
        decripteaza(mesaj)

if __name__ == "__main__":
    main()
