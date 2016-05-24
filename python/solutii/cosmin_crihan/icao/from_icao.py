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
# pylint: disable=unused-argument

ICAO = {
    'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
    'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett',
    'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar',
    'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray', 'y': 'yankee',
    'z': 'zulu'
}


def din_icao(mesaj):
    """Funcția va primi calea către fișierul ce conține mesajul brut și
    va genera un fișier numit icao_intrare ce va conține mesajul inițial.
    """

    try:
        fisier = open("mesaj.icao", "r")  # deschidem fisierul pentru citirea mesajului criptat ICAO
        mesaj = fisier.read().splitlines()  # punem liniile din fisier intr-o lista de string-uri
        fisier.close()
    except IOError:
        print("Nu s-a putut deschide fisierul cu mesajul ICAO!")
        exit()

    try:
        fisier_initial = open("icao_intrare", "w")  # deschidem fisierul pentru scrierea mesajului initial
    except IOError:
        print("Nu s-a putut deschide fisierul de scriere!")

    for linie in mesaj:  # parcurgem fiecare din liniile din fisier
        if not linie:  # linie fara niciun caracter = interlinie
            fisier_initial.write("\n")
        elif linie[0] in " .,;:?!":  # caracter special
            fisier_initial.write(linie[0])
        else:  # altfel, decriptam intreaga linie conform alfabetului ICAO
            cuvinte_icao = linie.split(", ")  # preluam cuvintele criptate

            for cheie in cuvinte_icao:
                if cheie:  # pentru siguranta: ultimul element dupa split e null
                    fisier_initial.write(cheie[0])  # punem caracterul decriptat in fisierul de iesire
                    # caracterul decriptat va fi prima litera din cheie

    fisier_initial.close()

if __name__ == "__main__":
    din_icao("mesaj.icao")
