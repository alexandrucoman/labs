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


def icao():
    """Funcția va primi calea mesajului ce trebuie transmis și
    va genera un fișier numit mesaj.icao_intrare ce va conține
    mesajul scris folosind alfabetul ICAO.
    """

    try:
        fisier = open("mesaj", "r")  # deschidem fisierul pentru citirea mesajului
        mesaj = fisier.read()  # punem mesajul din fisier intr-o variabila
        fisier.close()
    except IOError:
        print("Nu s-a putut deschide fisierul cu mesajul!")
        exit()

    try:
        fisier_icao = open("mesaj.icao", "w")  # deschidem fisierul pentru scrierea mesajului criptat
    except IOError:
        print("Nu s-a putut deschide fisierul de iesire!")

    chr_vechi = mesaj[0]
    for chr in mesaj:  # parcurgem caracter cu caracter
        if chr in " .,;:?!":  # semnele de punctuatie nu le luam in considerare
            if chr_vechi in " .,;:?!":
                fisier_icao.write(chr + "\n") # daca s-a intalnit un astfel de caracter special, il scriem pe o linie separata
                # cazul cand exista cel putin 2 caractere speciale unul dupa altul
            else:
                fisier_icao.write("\n" + chr + "\n")
                # cazul cand exista doar un caracter special intre 2 cuvinte
        elif chr == '\n':  # trecem la linie noua
            fisier_icao.write("\n")

        if chr <= 'z' and chr >= 'a':  # caracterul este litera
            fisier_icao.write(ICAO[chr] + ", ")  # scriem codificarea ICAO si separam litera de urmatoarea prin virgula

        chr_vechi = chr

    fisier_icao.close()

if __name__ == "__main__":
    icao()
