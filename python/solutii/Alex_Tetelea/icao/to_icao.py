"""to icao problem"""
import os

ICAO = {
    'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
    'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett',
    'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar',
    'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray', 'y': 'yankee',
    'z': 'zulu'
}


def icao(mesaj):
    """Translarea din cuvinte in alfabetul ICAO
    :param mesaj:
    """
    lista = mesaj.lower().replace('\n', ' ').strip().split(" ")
    result = []
    for cuvant in lista:
        for abr, word in ICAO.iteritems():
            if cuvant.strip().lower() == word:
                result.append(abr)
                continue
    fin = open("mesajto.icao", 'w')
    fin.write(''.join(result))


if __name__ == "__main__":
    FILE_NAME = "mesaj.icao"
    if os.path.exists(FILE_NAME):
        print "Fisier inexistent"
    else:
        PARAM = open(FILE_NAME, 'r')
        icao(PARAM.read())
