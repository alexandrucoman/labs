#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""Împăratul a primit o serie de mesaje importante pe care este
important să le descifreze cât mai repede.

Din păcate mesagerul nu a apucat să îi spună împăratului care au fost
cheile alese pentru fiecare mesaj și tu ai fost ales să descifrezi
misterul.

Informații:
    În criptografie, cifrul lui Caesar este o metodă simplă de a cripta
un mesaj prin înlocuirea fiecărei litere cu litera de pe poziția aflată
la n pași de ea în alfabet (unde este n este un număr întreg cunoscut)
"""
# pylint: disable=unused-argument

from __future__ import print_function


def decripteaza_mesajul(mesaj):
    """Funcția va primi un mesaj criptat folosind cifrul lui Caesar și
    va încerca să îl decripteze.
    """

    decriptat = ""  # mesajul decriptat

    for n in range(1, 26):  # 26 de litere (mici) posibile in alfabetul englez

        for litera in mesaj:  # decriptam fiecare litera in parte
            if litera in "., ":  # cu exceptia semnelor de punctuatie
                litera_decriptata = litera
            else:
                index_litera = (ord(litera) - ord('a') + n) % 26
                litera_decriptata = chr(index_litera + ord('a'))
            decriptat += litera_decriptata

        print("\nIncercare n=%d:" % n)

        print("%s\n" % decriptat)

        plauzibil = input('Plauzibil? (da=1/nu=0) ')  # intrebam utilizatorul daca mesajul e lizibil
        if plauzibil == 1:
            break
        else:
            decriptat = ""

    return decriptat

def decripteaza_mesajul_n(mesaj, n):
    """Funcția va primi un mesaj criptat folosind cifrul lui Caesar și
    îl va decripta folosind cheia n trimisa ca parametru
    """

    decriptat = ""

    for litera in mesaj:  # decriptam fiecare litera in parte
        if litera in "., ":  # cu exceptia semnelor de punctuatie
            litera_decriptata = litera
        else:
            # indicele literei in alfabet = ord(litera) - ord('a')
            index_litera = (ord(litera) - ord('a') + n) % 26
            litera_decriptata = chr(index_litera + ord('a'))
        decriptat += litera_decriptata

    return decriptat

def main():


    """ Main function docstring """
    try:
        fisier = open("mesaje.secret", "r")
        mesaje = fisier.read()
        fisier.close()
    except IOError:
        print("Nu am putut obține mesajele.")
        return

    try:
        mesaje_decriptate = open("mesaje.decriptate", "a")
    except IOError:
        print("Nu pot deschide fisierul de scriere a mesajelor decriptate.")

    i=1
    for mesaj in mesaje.splitlines():
        if i == 1:  # primul mesaj il decriptam prin incercari
            mesaje_decriptate.write("%s\n" % decripteaza_mesajul(mesaj))
        else:  # urmatoarele mesaje le decriptam prin formula: n=26-indice_prima_litera
            cheie = 26 - (ord(mesaj[0]) - ord('a'))
            mesaje_decriptate.write("%s\n" % decripteaza_mesajul_n(mesaj, cheie))
        i = i + 1

    mesaje_decriptate.close()

    print("\nMesajele au fost decriptate si plasate in fisierul \"mesaje.decriptate\"!")

if __name__ == "__main__":
    main()
