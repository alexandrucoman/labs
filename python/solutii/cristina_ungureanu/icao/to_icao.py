#!/usr/bin/env python
# *-* coding: UTF-8 *-*

"""Transforma un mesaj in limbaj natural in mesaj icao."""

ICAO = {
    'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
    'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett',
    'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar',
    'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray', 'y': 'yankee',
    'z': 'zulu'
}


def extrage_litere(cuvant):
    """Intoarce un cuvant conform alfabetului icao."""
    icao_litere = []
    for litera in cuvant:
        icao_litere.append(ICAO[litera])
    return icao_litere


def icao(mesaj):
    """Transforma mesajul natural in mesaj icao."""
    fsicao = open("mesaj.icao_intrare", "w")
    for cuvant in mesaj.split(' '):
        for litera in cuvant:
            fsicao.write(' '.join(extrage_litere(litera.lower())))
            fsicao.write(' ')
        fsicao.write('\n')
    fsicao.close()


if __name__ == "__main__":
    icao("Mesajul ce trebuie transmis")

