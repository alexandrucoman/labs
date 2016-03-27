ICAO = {
    'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
    'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett',
    'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar',
    'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray', 'y': 'yankee',
    'z': 'zulu'
}

def din_icao():
    """Func?ia va primi calea mesajul ce trebuie transmis ?i
    va genera un fi?ier numit mesaj.icao_intrare ce va con?ine
    mesajul scris folosind alfabetul ICAO.
    """
    file_to_read = open("mesaj.icao_intrare", 'r')
    mesaj = file_to_read.read()
    file_to_write = open('mesaj.icao_iesire', 'w+')
    for i in mesaj.splitlines():
        if i.strip():
            words = [x for x in i.split()]
            for j in words:
                file_to_write.write(j[0])
    pass


if __name__ == "__main__":
    din_icao()
