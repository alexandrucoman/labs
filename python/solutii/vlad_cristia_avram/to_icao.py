"""Solutie la problema to_icao"""

import sys


ICAO = {
    'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
    'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett',
    'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar',
    'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray', 'y': 'yankee',
    'z': 'zulu'
}


def icao(mesaj):
    """Functia de tradus"""
    fisier = open("mesaj.icao_intrare", "w")
    try:

        for i in range(1, len(mesaj)):
            for j in range(0, len(mesaj[i])):
                fisier.write(ICAO[mesaj[i][j]])
                fisier.write(' ')
            fisier.write('\n')
        fisier.close()
        try:
            if mesaj[1]:
                pass
        except IndexError:
            print("Nu ati introdus niciun mesaj pentru codificare")
    except KeyError:

        fisier.close()
        with open("mesaj.icao_intrare", "w"):
            pass
        print("Nu am putut coda mesajul in alfabetul ICAO")
        return


if __name__ == "__main__":
    icao(sys.argv)
