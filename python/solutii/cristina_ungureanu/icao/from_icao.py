#!/usr/bin/env python
# *-* coding: UTF-8 *-*

"""Transforma un mesajul icao in limbaj natural."""

ICAO = {
    'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
    'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett',
    'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar',
    'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray', 'y': 'yankee',
    'z': 'zulu'
}


def din_icao(fisier_intrare):
    """Extrage cuvintele din mesajul icao in mesaj.icao_intrare."""
    try:
        fisin = open(fisier_intrare, "r")
        fsicao = open("mesaj.icao_intrare", "w")
    except IOError:
        print "Eroare la deschidere fisier!"
    else:
        linii = fisin.read().strip().splitlines()
        for linie in linii:
            for cuvant in linie.split(' '):
                fsicao.write(cuvant[0])
            fsicao.write('\n')
        fisin.close()
        fsicao.close()


if __name__ == "__main__":
    din_icao("mesaj.icao")

