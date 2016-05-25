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
        file= open(forDecode,'r')
        toDecode=file.read()
        file.close()
    except IOError:
        print "File does not exist"
        return

    file=open(decoded,"w")
    for linie in toDecode.splitlines():
        for cuvant in linie.split():
            file.write(cuvant[0])
        file.write('\n')
    file.close()

if __name__ == "__main__":
    din_icao("mesaj.icao","decodat.icao")
