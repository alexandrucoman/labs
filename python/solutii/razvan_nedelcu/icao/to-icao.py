#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""
Organizatia Internationala a Aviatiei Civile propune un alfabet în care
fiecarei litere îi este asignat un cuvânt pentru a evita problemele în
în?elegerea mesajelor critice.
Pentru a se pastra un istoric al conversa?iilor s-a decis transcrierea lor
conform urmatoarelor reguli:
    - fiecare cuvânt este scris pe o singura linie
    - literele din alfabet sunt separate de o virgula
Urmatoarea sarcina ?i-a fost asignata:
    Scrie un program care sa primeasca un fi?ier ce con?ine mesajul
    ce trebuie transmis ?i genereaza un fi?ier numit mesaj.icao ce
    va con?ine mesajul scris folosin alfabetul ICAO.
Mai jos gasi?i un dic?ionar ce con?ine o versiune a alfabetului ICAO:
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
    """Func?ia va primi calea mesajul ce trebuie transmis ?i
    va genera un fi?ier numit mesaj.icao_intrare ce va con?ine
    mesajul scris folosind alfabetul ICAO.
    """
    out = open("mesaj.icao", "w")
    for word in mesaj.split():
        for char in word:
            out.write(ICAO[char])
            out.write(" ")
        out.write("\n")
if __name__ == "__main__":
    mesaj = raw_input("Introduceti mesajul: ")
    icao(mesaj)