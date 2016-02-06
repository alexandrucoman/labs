#!/usr/bin/env python
# *-* coding: UTF-8 *-*

"""Solutia problemei TO_ICAO"""
ICAO = {
    'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
    'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett',
    'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar',
    'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray', 'y': 'yankee',
    'z': 'zulu'
}
def traducere(string):
    """Traducerea mesajului TO_ICAO"""
    lista = list()
    for i in string:
        if i in ICAO:
            lista.append(ICAO[i])
            lista.append(" ")
    return "".join(lista)


def main():
    """Apelarea functiei"""
    try:
        fisier = open("mesaj.icao", "r")
        mesaje = fisier.read()
        fisier.close()
    except IOError:
        print "Nu am putut obtine mesajele."
        return

    for linie in mesaje.splitlines():
        print traducere(linie)


if __name__ == "__main__":
    main()


