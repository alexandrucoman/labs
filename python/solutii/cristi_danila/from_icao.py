#!/usr/bin/env python
# *-* coding: UTF-8 *-*
# pylint: disable=unused-argument

ICAO = {
    'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
    'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett',
    'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar',
    'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray', 'y': 'yankee',
    'z': 'zulu'
}

def din_icao(mesaj):
    output = open("icao_intrare", "w")
    file = open(mesaj, "r")
    
    for line in file:
        for encrypted_letter in line.split(","):
            matches = [key for key, value in ICAO.items() \
                                if value == encrypted_letter]
           
            if len(matches) > 0:
                output.write(matches[0] + ",")
        
        output.write("\n")
    
    file.close()
    output.close()

if __name__ == "__main__":
    din_icao("mesaj.icao_intrare")
