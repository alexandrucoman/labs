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

ICAO = {
    'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
    'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett',
    'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar',
    'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray', 'y': 'yankee',
    'z': 'zulu'
}


def icao(mesaj):
    """Funcția va primi calea mesajului ce trebuie transmis și
    va genera un fișier numit mesaj.icao_intrare ce va conține
    mesajul scris folosind alfabetul ICAO.
    """

    try:
        # deschidem fisierul pentru citirea mesajului
        fisier = open(mesaj, "r")
        msg = fisier.read()  # punem mesajul din fisier intr-o variabila
        fisier.close()
    except IOError:
        print "Nu s-a putut deschide fisierul cu mesajul!"
        return

    try:
        # deschidem fisierul pentru scrierea mesajului criptat
        fisier_icao = open("mesaj.icao", "w")
    except IOError:
        print "Nu s-a putut deschide fisierul de iesire!"
        return

    caracter_vechi = msg[0]
    for caracter in msg:  # parcurgem caracter cu caracter
        # semnele de punctuatie nu le luam in considerare
        if caracter in " .,;:?!":
            if caracter_vechi in " .,;:?!":
                # daca s-a intalnit un astfel de caracter special,
                # il scriem pe o linie separata
                caractere_de_scris = [caracter, "\n"]
                fisier_icao.write("".join(caractere_de_scris))
                # cazul cand exista cel putin 2 caractere speciale
                # unul dupa altul
            else:
                caractere_de_scris = ["\n", caracter, "\n"]
                fisier_icao.write("".join(caractere_de_scris))
                # cazul cand exista doar un caracter special intre 2 cuvinte
        elif caracter == '\n':  # trecem la linie noua
            fisier_icao.write("\n")

        if 'a' <= caracter <= 'z':  # caracterul este litera
            # scriem codificarea ICAO
            # si separam litera de urmatoarea prin virgula
            caractere_de_scris = [ICAO[caracter], ", "]
            fisier_icao.write("".join(caractere_de_scris))

        caracter_vechi = caracter

    fisier_icao.close()

if __name__ == "__main__":
    icao("mesaj")
