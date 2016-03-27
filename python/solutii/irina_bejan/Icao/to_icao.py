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
    ce trebuie transmis și generează un fișier numit mesaj.icao ce
    va conține mesajul scris folosin alfabetul ICAO.
Mai jos găsiți un dicționar ce conține o versiune a alfabetului ICAO:
"""
# pylint: disable=unused-argument

ICAO = {
    'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
    'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett',
    'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar',
    'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray', 'y': 'yankee',
    'z': 'zulu'
}


def icao(mesaj):
    """Genereaza fisierul de iesire."""

    fisier = open("icao.intrare", "w")
    for linie in mesaj.splitlines():
        for cuvant in linie.split():
            for caracter in cuvant:
                fisier.write(ICAO[caracter])
                fisier.writelines(" ")
        fisier.write('\n')
    fisier.close()


def procesare_fisier(nume):
    """Citeste datele din fisier"""
    try:
        fisier = open(nume, "r")
        mesaj = fisier.read()
        fisier.close()

        icao(mesaj)
    except IOError:
        print "Nu am putut obtine mesajele."


if __name__ == "__main__":
    procesare_fisier("icao.mesaj")
