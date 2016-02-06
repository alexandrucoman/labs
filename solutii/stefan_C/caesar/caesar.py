#!/usr/bin/env python
# *-* coding: UTF-8 *-*
from __future__ import print_function
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


def cipher(word):
    """
    :param word: the word to decipher to "ave"
    :return: the number used for encryption
    """
    word = word.lower()
    return ord(word[0]) % 97


def decripteaza(mesaj):
    '''
    :param mesaj: Mesajul pe care vrem sa il decriptam
    :return: va return cate un sir de cuvinte decriptat
    '''
    words = mesaj.split('.,')
    key = cipher(words[0])
    mesaj_decriptat = ' '
    for i in mesaj.lower():
        c = ord(' ')
        if i.isalpha():
            c = (ord(i) - key)
        if (not chr(c).isalpha() and chr(c) != ' ') or (chr(c).isupper()):
            c += 26
        mesaj_decriptat += chr(c)
    print (mesaj_decriptat)


def main():
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
