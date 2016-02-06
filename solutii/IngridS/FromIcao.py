"""Rezolvarea problemei From_Icao"""
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

def inversare_dictionar():
    """Inversarea dictionarului"""
    dictionary = dict()
    for key, value in ICAO.items():
        dictionary[value] = key
    return dictionary

def din_icao(mesaj):
    """Traducerea din Icao"""
    alfabet = inversare_dictionar()
    lista = list()
    for cuvant in mesaj.split():
        if cuvant in alfabet:
            lista.append(alfabet[cuvant])
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
        print din_icao(linie)


if __name__ == "__main__":
    main()
