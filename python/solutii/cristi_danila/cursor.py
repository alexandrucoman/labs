#!/usr/bin/env python
# *-* coding: UTF-8 *-*

from math import sqrt

def distanta():
    pos = [0, 0]
    try:
        file = open("istoric.tuxy", "r")
        
        for line in file:
            components = line.split(" ")

            if components[0] == "STANGA":
                pos[0] -= int(components[1])
            elif components[0] == "DREAPTA":
                pos[0] += int(components[1])
            elif components[0] == "SUS":
                pos[1] += int(components[1])
            elif components[0] == "JOS":
                pos[1] -= int(components[1])

        return int(sqrt(pos[0] ** 2 + pos[1] ** 2))

        file.close()
    except IOError:
        print("Couldn't open istoric.tuxy")
        return


if __name__ == "__main__":
    distanta()
