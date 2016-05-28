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


def icao(message_path):
    output = open("mesaj.icao_intrare", "w")
    fil = open(message_path, "r")
    
    for line in fil:
        clear_line = line.strip()
        if clear_line[-1] == ",":
            clear_line = clear_line[:-1:]
        
        for letter in clear_line.split(","):
            output.write(ICAO[letter] + ",")
        output.write("\n")

    fil.close()
    output.close()

if __name__ == "__main__":
    icao("icao_intrare")
