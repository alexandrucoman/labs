#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""
Tuxy cauta in fiecare zi cate o problema de matematica complet noua pentru el.

Rezolvand problema 101, a observat ca are nevoie de cateva formule mai vechi.
A revenit la fisierul lui de teoreme "teoreme1.txt" pentru ajutor. S-a bucurat
ca a reusit sa il gaseasca la timp ,fisierul fiind in /tmp/ciorne.
Uitandu-se prin el,a observat ca folosea o regula cand scria teoreme noi:

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

Stiind limbajul de programare python si fiind un fan al liniei de comanda,
el doreste sa implementeze un utilitar inteligent de cautat formule.
Functionalitatile care doreste sa le implementeze sunt:
    [1] cautare indiferent de caz (ex. 'a'=='A' ) [-i]
    [2] cautare exacta ( nu ia in considere parti ale cuvintelor) [-e]
    [3] cautare si inlocuire a sirurilor de caractere [-s]
    Ex: python utilitar.py -s "CARD" "CARDINAL"
    fiecare sir "CARD" a fost inlocuit cu "CARDINAL"
    [4] numararea aparitiilor unui sir de caractere [-n]
    [5] cautare recursiva a fisierelor prin director [-r]
    [6] introducerea parametrilor din linia de comanda:
    ex: python utilitar.py -in "CARD" teoreme1.txt
    sirul "CARD" (insensitiv) apare de 44 de ori in teoreme1.txt
    [7] afisarea unui mesaj de ajutor daca parametrii introdusi sunt gresiti

P.S. Prin inteligent se refera ca v-a returna tot ce stie despre teorema(nume,
nume scurt siteorema). Daca sirul de caractere cautat apare in mai multe
teoreme, utilitarul returneaza doar numele complet si cel scurt al teoremelor.

Oare cum a implementat Tuxy acest utilitar?

Posibila documentatie:
    - http://linux.die.net/man/1/grep
    - http://git.savannah.gnu.org/cgit/grep.git/snapshot/grep-2.22.tar.gz
    - din cadrul arhivei amintite anterior, folderul "src"
    - https://github.com/heyhuyen/python-grep
"""

from __future__ import print_function
import sys
import getopt
import re

# NETERMINATA

# case_sensitive = True
# exact_search = False


def parseopt(argv, options):
    """ Functie inlocuitor pentru geopt pt ca nu se pot pune 2
    argumente dupa o optiune, necesar pt -s "blabla" "blabla"
    """
    # end_opt = argv.find(' ', start_opt = argv.find('-'))
    # if end_opt:
    # input_options = argv[start_opt-end_opt]

    regexp = re.compile("[^"+options+"]")
    result = regexp.findall(''.join(argv))

    if result:
        print("invalid arguments/options:" + str(result))


def main(argv):
    """ Grep in python
    """
    try:
        opts, args = getopt.getopt(argv, 'ies:nr')
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    print(args, opts)
    print(args)
    for i in opts:
        if i[0] == '-i':
            # case_sensitive = False
            print("Case insensitive activated!")
            sys.exit()
        elif i[0] == "-e":
            print("Exact Search Activated")
            sys.exit()
        elif i == "-s":
            # print('Cautarea sirului {0} in {1}').format(o, argv)
            sys.exit()
        else:
            print(i)
            assert False, "unhandled option"


if __name__ == "__main__":
    parseopt(sys.argv[1:], "iesnr")
