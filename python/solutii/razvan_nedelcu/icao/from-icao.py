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
    brut (scris folosind alfabetul ICAO) ?i genereaza un fi?ier
    numit icao_intrare ce va con?ine mesajul ini?ial.
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


def din_icao(mesaj):
    """Func?ia va primi calea catre fi?ierul ce con?ine mesajul brut ?i
    va genera un fi?ier numit icao_intrare ce va con?ine mesajul ini?ial.
    """
    fisier = open(mesaj, "r") 
    out = open("icao_intrare", "w")
    for line in fisier:
        for word in line.split():
            out.write(word[0])
        out.write("\n")


if __name__ == "__main__":
    din_icao("mesaj.icao")