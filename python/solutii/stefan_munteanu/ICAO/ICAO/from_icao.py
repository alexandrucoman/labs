<<<<<<< fb9f1b711dd83947ca8d071746fe22677b266648:python/solutii/stefan_munteanu/ICAO/ICAO/from_icao.py
"""Rezolv icao"""
=======
<<<<<<< HEAD
"""Icao"""
=======
"""Rezolv icao"""
>>>>>>> a9b5cf5... Fix7
>>>>>>> caesar:python/solutii/stefan_munteanu/ICAO/ICAO/from_icao.py


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


if __name__ == "__main__":
<<<<<<< fb9f1b711dd83947ca8d071746fe22677b266648:python/solutii/stefan_munteanu/ICAO/ICAO/from_icao.py
=======
<<<<<<< HEAD:python/solutii/stefan_munteanu/ICAO/ICAO/from_icao.py
    """main"""
=======
>>>>>>> a9714af... Fix7:python/solutii/stefan_munteanu/ICAO/ICAO/from_icao.py.py
>>>>>>> caesar:python/solutii/stefan_munteanu/ICAO/ICAO/from_icao.py
    din_icao()
