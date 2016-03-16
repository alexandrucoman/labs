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


def icao(cale):
    """Funcția va primi calea mesajul ce trebuie transmis și
    va genera un fișier numit mesaj.icao_intrare ce va conține
    mesajul scris folosind alfabetul ICAO.
    """
    try:
        fisier_in = open(cale, "r")
        mesaj = fisier_in.read()
        fisier_in.close()
        fisier_out = open("../../date_intrare/mesaj.icao_intrare", "w")
    except IOError:
        print "Nu am putut obține mesajul."
        return
    mesaj_codat = ""
    for litera in mesaj:
        if litera == " ":
            mesaj_codat += '\n'
        else:
            if litera.isalpha():
                mesaj_codat += ICAO[litera] + ' '
            else:
                mesaj_codat += litera
    fisier_out.write(mesaj_codat)
    fisier_out.close()


def main():
    """ Main function docstring """
    icao("../../date_intrare/mesaj.icao.necodat")

if __name__ == "__main__":
    main()
