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


def cauta_in_teorema(opt, teorema, patt):

    """Face match pe cuvant intr-o teorema (i si e)"""

    if 'i' in opt:
        if 'e' in opt:
            matchObj = re.match(r'.*\b(%s)\b.*' % patt, teorema, re.S | re.I)
        else:
            matchObj = re.match(r'.*(%s).*' % patt, teorema, re.S | re.I)
    else:
        matchObj = re.match(r'.*(%s).*' % patt, teorema, re.S)
    if matchObj:
        return True
    else:
        return False


def numara_aparitii(opt, patt, teorema):

    """Contorizeaza aparitiile cuvantului in teorema"""

    contor = 0
    i = 0
    while i+len(patt) <= len(teorema):
        if 'i' in opt:
            if teorema[i:i+len(patt)].lower() == patt.lower():
                contor += 1
        else:
            if teorema[i:i+len(patt)] == patt:
                contor += 1
        i += 1
    return contor


def extrage_bloc_formula_din_fisier(*args):

    """Analizeaza fisier si urmareste cuvant per teorema"""

    if not os.path.isfile(args[len(args)-1]):
        print "Not a file!"
    else:
        print os.path.abspath(args[len(args)-1])+":"
        if len(args) < 5:
            opt = args[1]
            patt = args[2]
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
        for i in range(len(linii)):
            matchObj = re.match(r'[ ]\d+[.][ ]{2}', linii[i], re.X)
            if matchObj:
                if start != -1:
                    if 'c' in opt:
                        contor += numara_aparitii(opt, patt, teorema)
                    else:
                        if cauta_in_teorema(opt, teorema, patt):
                            if 's' in opt:
                                print re.sub(r'(%s)' % patt, repw, teorema)
                            else:
                                print teorema
                    teorema = linii[i]+'\n'
                    start = i
                else:
                    start = i
                    teorema = linii[i]+'\n'
            else:
                teorema += linii[i]+'\n'
        if 'c' in opt:
            print contor, "aparitii"
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

