#!/usr/bin/env python
# *-* coding: UTF-8 *-*

"""Solutia problemei Cursor"""
DIRECTIONS = {" stanga " : [-1, 0], " dreapta " :[1, 0],
" jos " :[0, -1], " sus " :[0, 1]}

def distanta(string, pozitie):
    """Determinarea distantei"""
    directie, valoare = string.split()
    directie = directie.lower()
    if directie in DIRECTIONS:
        directie = DIRECTIONS[directie]
        pozitie[0] = pozitie[0]+directie[0]*int(valoare)
        pozitie[1] = pozitie[1]+directie[1]*int(valoare)

def main():
    """Apelarea functiei"""
    try:
        fisier = open("Cursor_Date", "r")
        mesaje = fisier.read()
        fisier.close()
    except IOError:
        print "Nu am putut obține coordonatele."
        return
    pozitie = [0, 0]
    for linie in mesaje.splitlines():
        if linie:
            distanta(linie, pozitie)
            print pozitie
    rezultat = (pozitie[0]**2 + pozitie[1]**2) ** 0.5
    print rezultat

if __name__ == "__main__":
    main()

