"""from_icao problem"""
import os

ICAO = {
    'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
    'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett',
    'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar',
    'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray', 'y': 'yankee',
    'z': 'zulu'
}


def din_icao(fisier_intrare):
    """tRANSLARE DIN ICAO IN NORMAL
    :param fisier_intrare:
    """
    if not os.path.exists(fisier_intrare):
        print "Fisier inexistent"
        return
    result = []
    readfile = open(fisier_intrare, 'r')
    mesaj = readfile.read()
    for litera in mesaj:
        for abr, word in ICAO.iteritems():
            if litera.lower() == abr:
                result.append(word)
                result.append(' ')
                continue
    file_to_write = open("mesajfrom.icao", 'w')
    file_to_write.write(''.join(result))


if __name__ == "__main__":
    din_icao("mesajto.icao")
