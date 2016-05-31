ICAO = {
    'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
    'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett',
    'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar',
    'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray', 'y': 'yankee',
    'z': 'zulu'
}


def din_icao(forDecode, decoded):
    try:
        fisier= open(forDecode,'r')
        toDecode=fisier.read()
        fisier.close()
    except IOError:
        print "File does not exist"
        return

    decoded=open(decoded,"w")
    for linie in toDecode.splitlines():
        for cuvant in linie.split():
            decoded.write(cuvant[0])
        decoded.write('\n')
    decoded.close()

if __name__ == "__main__":
    din_icao("mesaj.icao","decodat.icao")
