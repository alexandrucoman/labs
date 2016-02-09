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


def c_ind(mes):
    fis = open("teoreme1.txt", "r")
    if num_ap(mes) == 1:
        ok = 0
        counter = 0
        for line in fis:
            line = line.rstrip()
            if mes.lower() in line.lower():
                ok = 1
                counter = 0
            r_obj = re.search('\d+\.  ', line)
            if r_obj:
                counter += 1
            if counter == 2:
                ok = 0
            if counter < 2 and ok:
                print line
    else:
        ok = 0
        counter = 0
        for line in fis:
            line = line.rstrip()
            if mes.lower() in line.lower():
                ok = 1
                counter = 0
            counter += 1
            if counter == 3:
                ok = 0
            if counter < 3 and ok:
                print line


def c_ex(mes):
    fis = open("teoreme1.txt", "r")
    mes = " " + mes + " "
    if num_ap(mes) == 1:
        ok = 0
        counter = 0
        for line in fis:
            line = line.rstrip()
            if mes.lower() in line.lower():
                ok = 1
                counter = 0
            r_obj = re.search('\d+\.  ', line)
            if r_obj:
                counter += 1
            if counter == 2:
                ok = 0
            if counter < 2 and ok:
                print line
    else:
        ok = 0
        counter = 0
        for line in fis:
            line = line.rstrip()
            if mes.lower() in line.lower():
                ok = 1
                counter = 0
            counter += 1
            if counter == 3:
                ok = 0
            if counter < 3 and ok:
                print line


def c_inl(mes, inl):
    fis = open("teoreme1.txt", "r")
    for line in fis:
        if mes in line:
            print line.replace(mes, inl)


def num_ap(mes):
    fis = open("teoreme1.txt", "r")
    l = [item for item in fis]
    p = str(l).count(mes)
    return p

c_inl("Law", "hector")
# print numarare_aparitii("th")
