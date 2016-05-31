ICAO = {
    'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
    'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett',
    'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar',
    'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray', 'y': 'yankee',
    'z': 'zulu'
}


def icao(mesaj):
    file=open('mesaj.icao','w')
    mesaj = mesaj.lower()
    for cuvant in mesaj.split() :
        for litera in cuvant :
            word=ICAO[litera]
            file.write(word,)
            file.write(" ")
        file.write("\n")
    file.close()


if __name__ == "__main__":
    icao("Long live python")
