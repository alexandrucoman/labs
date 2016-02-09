#!/usr/bin/env python
# *-* coding: UTF-8 *-*

"""
    [Index].[Spatiu][Spatiu][Numele Teoremei]
    [Numele scurt]
    [Rand nou]
    [Rand nou]
    [Teorema]
    [Rand nou]
    [Rand nou]

Exemplu:
    1.  The Irrationality of the Square Root of 2
        SQRT_2_IRRATIONAL


     |- ~rational(sqrt(&2))


"""


import os
import re
from sys import argv


def numara_aparitii(opt, patt, repw, teorema):

    """Calculeaza de toate in functie de parametri"""

    contor = 0
    i = 0
    copie = str(teorema)
    while i+len(patt) <= len(copie):
        turn = 0
        if 'i' in opt:
            if copie[i:i+len(patt)].lower() == patt.lower():
                if 'e' in opt:
                    if ((i-1 < 0 or not copie[i-1].isalnum()) and
                        (i+len(patt) > len(copie) or
                         not copie[i+len(patt)].isalnum())):
                        turn += 1
                else:
                    turn += 1
                if 's' in opt and turn > 0:
                    copie = copie[:i]+repw+copie[i+len(patt):]
                    i = i+len(repw)-1
                contor += turn
        else:
            if copie[i:i+len(patt)] == patt:
                if 'e' in opt:
                    if ((i-1 < 0 or not copie[i-1].isalnum()) and
                        (i+len(patt) > len(copie) or
                         not copie[i+len(patt)].isalnum())):
                        turn += 1
                else:
                    turn += 1
                if 's' in opt and turn > 0:
                    copie = copie[:i]+repw+copie[i+len(patt):]
                    i = i+len(repw)-1
                contor += turn
        i += 1
    return (contor, copie)


def extrage_bloc_formula_din_fisier(*args):

    """Analizeaza fisier pentru fiecare teorema"""

    if not os.path.isfile(args[len(args)-1]):
        print "Not a file!"
    else:
        if len(args) < 5:
            opt = args[1]
            patt = args[2]
            repw = patt
            nume = args[3]
        else:
            if len(args) < 6:
                opt = args[1]
                patt = args[2]
                repw = args[3]
                nume = args[4]
        fisier = open(nume, "r")
        continut = fisier.read()
        linii = continut.splitlines()
        start = -1
        teorema = ""
        contor = 0
        continutmodificat = ""
        for i in range(len(linii)):
            matchObj = re.match(r'[ ]\d+[.][ ]{2}', linii[i], re.X)
            if matchObj:
                if start != -1:
                    pereche = numara_aparitii(opt, patt, repw, teorema)
                    contor += pereche[0]
                    continutmodificat += pereche[1]
                    if pereche[0] > 0 and 'c' not in opt:
                        print '\n', os.path.abspath(args[len(args)-1])+":"
                        print pereche[1]
                    teorema = linii[i]+'\n'
                    start = i
                else:
                    start = i
                    teorema = linii[i]+'\n'
            else:
                teorema += linii[i]+'\n'
        if 'c' in opt:
            print os.path.abspath(args[len(args)-1])+":",
            print contor, "aparitii"
        fisier.close()
        fisier = open(nume, "w")
        fisier.write(continutmodificat)
        fisier.close()


def afis_recursiv(*args):

    """Recursiv cauta in fiecare fisier avand argumentele"""

    argument = args[len(args)-1]
    if os.path.isdir(os.path.abspath(argument)):
        for fisier in os.listdir(argument):
            if os.path.isdir(os.path.join(argument, fisier)):
                afis_recursiv(list(args[:len(args)-1]) +
                              [os.path.join(argument, fisier)])
            else:
                argnoi = list(args[:len(args)-1]) + [
                                os.path.join(argument, fisier)]
                extrage_bloc_formula_din_fisier(*argnoi)
    else:
        print "Not a folder!"


if __name__ == "__main__":
    if len(argv) < 4:
        print "Argumente: [opt] [string] [file]"
        print "Argumente: [opt+s] [string] [repwith] [file]"
    else:
        if 'r' in argv[1]:
            afis_recursiv(*argv)
        else:
            extrage_bloc_formula_din_fisier(*argv)

