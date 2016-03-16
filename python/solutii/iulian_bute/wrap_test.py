#!/usr/bin/env python
''' Test wrapper '''


def conversie(paramet):
    ''' aici se face conversia din parametru text in integer '''
    if isinstance(paramet, int):
        return paramet
    return 0


CACHE = {}


def retine(functie):
    ''' decidem daca a fost anterior calculat sau returnam din cache '''
    def verifica(parametru):
        ''' decidem daca a fost anterior calculat sau returnam din cache '''
        if parametru in CACHE:
            print " Anterior calculat, ", parametru
            return CACHE[parametru]
        print " Cerem calcularea parametrului ", parametru
        CACHE[parametru] = functie(parametru)
        return CACHE[parametru]
    return verifica


@retine
def evalueaza_int(param):
    ''' functia a carei valori o punem in cache '''
    print "Prelucram in functie", param
    return param + 1


def evalueaza(param):
    ''' functia primeste ca parametru un string '''
    print evalueaza_int(conversie(param))
    print


def main():
    ''' rulam teste '''
    evalueaza(2)
    evalueaza(2)
    evalueaza(3)
    evalueaza("123")
    evalueaza("123abc")
    evalueaza("2+2*3")
    evalueaza("abc")


if __name__ == "__main__":
    main()
