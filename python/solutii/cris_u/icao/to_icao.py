#!/usr/bin/env python
# *-* coding: UTF-8 *-*


ICAO = {
    'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
    'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett',
    'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar',
    'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray', 'y': 'yankee',
    'z': 'zulu'
}


def extrage_litere(cuvant):
    icao_litere = []
    for litera in cuvant:
        icao_litere.append(ICAO[litera])
    return icao_litere


def icao(mesaj):
    fisier = raw_input("Cale mesaj: ")
    fisin = open(fisier, "r")
    fsicao = open("mesaj.icao_intrare", "w")
    linii = fisin.read().strip().splitlines()
    for linie in linii:
        for cv in linie.split(' '):
            fsicao.write(' '.join(extrage_litere(cv)))
        fsicao.write('\n')
    fisin.close()
    fsicao.close()


if __name__ == "__main__":
    icao("Mesajul ce trebuie transmis")

