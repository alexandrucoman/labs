<<<<<<< fb9f1b711dd83947ca8d071746fe22677b266648:python/solutii/stefan_munteanu/ICAO/ICAO/to_icao.py
"""Rezolv icao """
=======
<<<<<<< HEAD
<<<<<<< HEAD
"""Icao"""
=======
>>>>>>> 2cd989b... Fix7
=======
"""Rezolv icao """
>>>>>>> a9b5cf5... Fix7
>>>>>>> caesar:python/solutii/stefan_munteanu/ICAO/ICAO/to_icao.py


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
    file_to_write = open('mesaj.icao_intrare', 'w+')
    for i in mesaj.lower():
        if i.isalpha():
            file_to_write.write(ICAO[i] + ' ')
        elif i.isspace():
            file_to_write.write(' ')
<<<<<<< fb9f1b711dd83947ca8d071746fe22677b266648:python/solutii/stefan_munteanu/ICAO/ICAO/to_icao.py
=======


if __name__ == "__main__":
    """main"""
    unique = raw_input('Enter your input:')
    icao(unique)

>>>>>>> caesar:python/solutii/stefan_munteanu/ICAO/ICAO/to_icao.py
