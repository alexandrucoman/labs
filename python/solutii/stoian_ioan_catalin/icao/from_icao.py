#!/usr/bin/env python
# *-* coding: UTF-8 *-*
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


def get_list_of_line(mesaj):
    "Imparte fisierul in linii"
    rezultat = mesaj.split("\n")
    return rezultat


def get_list_of_words(line):
    "Imparte linia in cuvinte"
    rezultat = line.split(" ")
    return rezultat


def get_word_from_icao(word):
    "Traduce cuvantul din ICAO in litera"
    for lit in ICAO:
        if ICAO[lit] == word:
            return lit


def din_icao(mesaj):
    """Funcția va primi calea către fișierul ce conține mesajul brut și
    va genera un fișier numit icao_intrare ce va conține mesajul inițial.
    """
    fisier = open(mesaj, 'r')
    lines = get_list_of_line(fisier.read())
    fisier.close()
    mesajdec = ""
    for line in lines:
        words = get_list_of_words(line)
        for word in words:
            lit = get_word_from_icao(word)
            if lit:
                mesajdec += lit
        mesajdec += " "
    print(mesajdec)
    pass


if __name__ == "__main__":
    din_icao("../../../date_intrare/mesaj.icao")
