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
    """Funcția va primi mesajul ce trebuie transmis și
    va genera un fișier numit mesaj.icao_intrare ce va conține
    mesajul scris folosind alfabetul ICAO.
    """

    iesire=open("icao_iesire.icao",'w')
    for i in range(0,len(mesaj)):
        if mesaj[i]==' ':
            iesire.write('\n')
        else:
            iesire.write(ICAO[mesaj.lower()[i]])
            iesire.write(' ')
    iesire.close()
    pass


if __name__ == "__main__":
    icao("Mesajul ce trebuie transmis")
