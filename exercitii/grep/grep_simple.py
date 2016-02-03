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


"""
import os

"""
Stiind limbajul de programare python si fiind un fan al liniei de comanda,
el doreste sa implementeze un utilitar inteligent de cautat formule.
Functionalitatile care doreste sa le implementeze sunt:
    [1] cautare indiferent de caz (ex. 'a'=='A' ) [-i]
    [2] cautare exacta ( nu ia in considere parti ale cuvintelor) [-e]
    [3] cautare si schimbare a sirurilor de caractere [-s]
    [4] numararea aparitiilor unui sir de caractere [-n]
    [5] cautare recursiva a fisierelor prin director [-r]
    [6] introducerea parametrilor din linia de comanda:
    ex: python utilitar.py -in "CARD" teoreme1.txt
    sirul "CARD" (insensitiv) apare de 44 de ori in teoreme1.txt
    [7] afisarea unui mesaj de ajutor daca parametrii introdusi sunt gresiti

P.S. Prin inteligent se refera ca v-a returna tot ce stie despre teorema(nume,
nume scurt siteorema). Daca sirul de caractere cautat apare in mai multe
teoreme, utilitarul returneaza doar numele complet si cel scurt al teoremelor.
"""

"""

Oare cum a implementat Tuxy acest utilitar?

Posibila documentatie:
    - http://linux.die.net/man/1/grep
    - http://git.savannah.gnu.org/cgit/grep.git/snapshot/grep-2.22.tar.gz
    - din cadrul arhivei amintite anterior, folderul "src"
    - https://github.com/heyhuyen/python-grep
"""
import re

import sys, getopt


def search2(message, caseSensitive, Exact=False, find_str="", shouldReplace=False, replaceable="", count=False):
    allTeorems = []
    message.split()
    lista = re.split('\d+\.  ', message)
    lista.pop(0)
    for teorema in lista:
        seaparator = teorema.split("  |- ")
        iTeorema = {"Nume_complet": seaparator[0].strip().split('\n')[0],
                    "Nume_scurt": seaparator[0].strip().split('\n')[1], "Descriere": seaparator[1::],
                    "Tot_mesajul": teorema}
        allTeorems.append(iTeorema)
    good_Theorems = []
    count = 0
    for teorema in allTeorems:
        if caseSensitive:
            if Exact:
                a = re.findall("\s" + find_str + "\s", teorema["Tot_mesajul"])
            else:
                a = re.findall(".+" + find_str + ".+", teorema["Tot_mesajul"])
        else:
            if Exact:
                a = re.findall("\s" + find_str + "\s", teorema["Tot_mesajul"], re.IGNORECASE)
            else:
                a = re.findall(".+" + find_str + ".+", teorema["Tot_mesajul"], re.IGNORECASE)
        if len(a) > 0:
            count += len(a)
            good_Theorems.append(teorema)
    if Exact or not caseSensitive:
        if len(good_Theorems) < 2:
            for teorema in good_Theorems:
                print teorema["Tot_mesajul"]
        else:
            for teorema in good_Theorems:
                print teorema["Nume_complet"], teorema["Nume_scurt"]
    message = message.replace(find_str, replaceable)
    if shouldReplace:
        if not caseSensitive:
            insensitive_hippo = re.compile(re.escape(find_str))
            insensitive_hippo.sub(replaceable, message)
        else:
            insensitive_hippo = re.compile(re.escape(find_str), re.IGNORECASE)
            insensitive_hippo.sub(replaceable, message)
    if count:
        print count
    pass


def main(argv):
    try:
        opts = ' '.join(argv).split(' ')[0]
    except getopt.GetoptError:
        print "Eraore"
    i = False
    e = False
    s = False
    n = False
    r = False
    o = False
    for opt in opts:
        if opt[0] == '-h':
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt[0] in ("i"):
            i = True
        elif opt in ("o"):
            o = True
        elif opt in ("e"):
            e = True
        elif opt in ("s"):
            s = True
        elif opt in ("n"):
            n = True
        elif opt in ("r"):
            r = True
        elif opt in ("-h"):
            print 'test.py -i <inputfile> -o <outputfile>'
    phrase = ""
    replace = ""

    if not r:
        if not n:
            phrase = argv[-2]
        else:
            replace = argv[-2]
            phrase = argv[-3]
        read_file = open(argv[-1], 'r')
        message = read_file.read()
        phrase = phrase.translate(None, ''.join(['.', '\'', '"']))
        search2(message, not i, e, phrase, s, replace, n)
    else:
        if not n:
            phrase = argv[-2]
        else:
            replace = argv[-2]
            phrase = argv[-3]
        for folder, subs, files in os.walk(argv[-1]):
            for filename in files:
                with open(os.path.join(folder, filename), 'r') as src:
                    print filename
                    message = src.read()
                    phrase = phrase.translate(None, ''.join(['.', '\'', '"']))
                    search2(message, not i, e, phrase, s, replace, n)
    sys.exit(2)


if __name__ == "__main__":
    main(sys.argv[1:])
