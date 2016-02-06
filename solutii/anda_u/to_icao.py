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


def icao(mesaj):
    """Func?ia va primi calea mesajul ce trebuie transmis ?i
    va genera un fi?ier numit mesaj.icao_intrare ce va con?ine
    mesajul scris folosind alfabetul ICAO.
    """
    fisier=open("mesaj.icao_intrare","w+")
    for cuvant in mesaj.split():
        for litera in cuvant:
            for key,value in ICAO.items():
                if litera==key:
                    fisier.write(value)
                    fisier.writelines(" ")
        fisier.write("\n")
    fisier.close()


if __name__ == "__main__":
    icao("Mesajul ce trebuie transmis")
