"""Rezolvarea problemei from_icao"""
from __future__ import print_function

import os


ICAO = {
    'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
    'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett',
    'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar',
    'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray', 'y': 'yankee',
    'z': 'zulu'
}


def din_icao(mesaj):
    """Functia de traducere"""
    try:
        fisier = open(mesaj, "r")
        mesaj = fisier.read()
        fisier.close()
    except IOError:
        print("Nu exista fisierul din care doriti sa faceti traducerea.")
        return
    if mesaj == "":
        print("Nu exista niciun text de tradus in fisierul dorit.")
    for linie in mesaj.splitlines():
        for i in linie.split():
            if ICAO[i[0]] == i:
                print(i[0], end="")
            else:
                print()
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Fisierul contine cuvinte ce nu sunt codate ICAO")
                return
        print()

if __name__ == "__main__":
    din_icao("mesaj.icao")
