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

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decrypt_by_cipher(message, cipher):
    decrypted = ""
    for charachter in message:
        if charachter in letters:
            index = (ord(charachter) - ord('A') + cipher) % len(letters)
            decrypted += letters[index - 1]
        else:
            decrypted += charachter
    return decrypted

def decripteaza_mesajul(mesaj):
    working_copy = mesaj.upper();
    cipher = -1
    
    for n in range(1, len(letters) + 1):
        sample = decrypt_by_cipher(working_copy, n)[:3:] 
        if sample == "AVE":
            cipher = n
            break
    
    if cipher != -1:
        return decrypt_by_cipher(working_copy, cipher).lower()
    else:
        raise Exception("Can't decrypt the message")

def main():
    """ Main function docstring """
    try:
        fisier = open("mesaje.secret", "r")
        mesaje = fisier.read()
        fisier.close()
    except IOError:
        print("Nu am putut obține mesajele.")
        return

    for mesaj in mesaje.splitlines():
        print(decripteaza_mesajul(mesaj))

if __name__ == "__main__":
    main()
