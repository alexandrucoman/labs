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
LETTERS = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"


# tot timpul se va gasi litera in string-ul "LETTERS"
# deci circularitatea e suficient
# reprezentata prin a-z de doua ori
def shift_letter(let, number):
    """Shifts a letter by number places in LETTERS"""
    if let.isalpha():
        # procesam doar literele
        return LETTERS[ord(let) - 97 + number]
        # returnam litera de peste n locuri in LETTERS

    else:
        return let
        # daca nu e litera, returnam caracterul original


def decripteaza(mesaj, number):
    """Decrypts every line in <mesaj>"""
    new_msg = ""
    for i in enumerate(mesaj):
        new_msg += shift_letter(mesaj[i], number)
    if "ave" in new_msg:
        print(new_msg)


def main():
    """Have a main docstring, pylint"""
    try:
        fisier = open("mesaje.secret", "r")
        mesaje = fisier.read()
        fisier.close()
    except IOError:
        print("Nu am putut obține mesajele.")
        return

    for mesaj in mesaje.splitlines():
        for i in range(26):
            decripteaza(mesaj, i)


if __name__ == "__main__":
    main()
