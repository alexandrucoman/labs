#!/usr/bin/env python
# *-* coding: UTF-8 *-*
from __future__ import print_function
"""
Organizaţia Internaţională a Aviaţiei Civile propune un alfabet în care
fiecărei litere îi este asignat un cuvânt pentru a evita problemele în
înțelegerea mesajelor critice.

Pentru a se păstra un istoric al conversațiilor s-a decis transcrierea lor
conform următoarelor reguli:
    - fiecare cuvânt este scris pe o singură linie
    - literele din alfabet sunt separate de o virgulă

Următoarea sarcină ți-a fost asignată:
    Scrie un program care să primească un fișier ce conține mesajul
    brut (scris folosind alfabetul ICAO) și generează un fișier
    numit icao_intrare ce va conține mesajul inițial.

Mai jos găsiți un dicționar ce conține o versiune a alfabetului ICAO:
"""

ICAO = {
    'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
    'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett',
    'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar',
    'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray', 'y': 'yankee',
    'z': 'zulu'
}


def din_icao(fisier_intrare, fisier_iesire):
    '''
    Funcția va primi calea către fișierul ce conține mesajul brut și
    va genera un fișier numit icao_intrare ce va conține mesajul inițial.
    :param fisier_intrare: File containing a message encrypted with ICAO
    :param fisier_iesire: The file containing the decrypted message
    :return: A file containing the decrypted message
    '''
    words = [x for x in fisier_intrare.split()]
    for i in words:
        fisier_iesire.write(i[0])
    fisier_iesire.write(' ')


def main():
    try:
        fisier = open("mesaj.icao", "r")
        mesaj_icao = fisier.read()
        fisier.close()
    except IOError:
        print("Nu am putut ob?ine mesajele.")
        return
    fisier_iesire = open('./mesajul.txt', 'w+')
    for mesaj in mesaj_icao.splitlines():
        if mesaj.strip():
            din_icao(mesaj, fisier_iesire)

if __name__ == "__main__":
    main()
