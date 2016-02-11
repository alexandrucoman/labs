#!/usr/bin/env python
# *-* coding: UTF-8 *-*

"""
Tuxy nu dorește să uite de nici un eveniment important pentru el
sau pentru cineva apropiat lui așa că își dorește un sistem care
să îi permită gestiunea acestor evenimente.

Script-ul `manager` îi oferă lui Tuxy posibilitatea de a adăuga
modifica sau șterge un eveniment.
"""
import time
import os


def check_date(string):
    if string.split('/')[0].isdigit() and string.split('/')[1].isdigit():
        if int(string.split('/')[0]) <= 31 and int(string.split('/')[1]) <= 12:
            return True
    return False


def check_dollar(string):
    if '$' in string:
        return False
    return True


class Person:
    def __init__(self):
        self.name = input("Numele persoanei: ")
        while not check_dollar(self.name):
            print('Caracter invalid! - $')
            self.name = input("Numele persoanei: ")
        self.dob = input("Data nasterii dd/mm: ")
        while not check_date(self.dob):
            print('Data nasterii invalida!')
            self.dob = input("Data nasterii dd/mm: ")
        self.contact = input("Contact: ")
        while not check_dollar(self.contact):
            print('Caracter invalid! - $')
            self.contact = input("Contact: ")

    def ammend(self):
        file = open('data.dat', 'a')
        file.write(self.name + '$' + self.dob + '$' + self.contact + '\n')
        file.close()

    def edit(self, line):
        with open('data.dat') as file:
            info = file.readlines()
        file.close()
        info[line] = self.name + '$' + self.dob + '$' + self.contact + '\n'
        file = open('data.dat', 'w')
        for i in info:
            file.write(i)
        file.close()


def adauga():
    print("Adauga o persoana noua in baza ta de date")
    persoana = Person()
    persoana.ammend()


def sterge():
    file = open('data.dat', 'r')
    linecounter = 0
    print("Alege ce persoana vrei sa stergi introducand numarul din lista: ")
    for i in file.read().splitlines():
        if linecounter != 0:
            print("%s. %s" % (linecounter, (i.split('$')[0])))
        linecounter += 1
    file.close()
    stergere = input("Ce persoana vrei sa stergi?: ")
    stergere = int(stergere)
    while stergere > linecounter - 1 or stergere < 0:
        print("Optiune invalida!")
        stergere = input("Ce persoana vrei sa stergi?: ")
        stergere = int(stergere)
    file = open('data.dat', 'r')
    content = file.readlines()
    del content[stergere]
    file.close()
    file = open('data.dat', 'w')
    for linie in content:
        file.write(linie)
    file.close()
    print("Persoana numarul %s a fost stearsa" % stergere)
    time.sleep(2)


def editeaza():
    print("Editeaza o persoana din baza de date")
    file = open('data.dat', 'r')
    linecounter = 0
    print("Alege ce persoana vrei sa editezi introducand numarul din lista: ")
    for i in file.read().splitlines():
        if linecounter != 0:
            print("%s. %s" % (linecounter, (i.split('$')[0])))
        linecounter += 1
    file.close()
    editare = input("Ce persoana vrei sa editezi?: ")
    editare = int(editare)
    while editare > linecounter - 1 or editare < 0:
        print("Optiune invalida!")
        editare = input("Ce persoana vrei sa stergi?: ")
        editare = int(editare)
    persoana = Person()
    persoana.edit(editare)


def manager():
    """Aplicație ce permite gestiunea evenimentelor."""

    optiune = input("   +++Baza de date+++ \n \n"
                    "Alege optiunea pe care o doresti:\n"
                    "1 - Adauga o persoana\n"
                    "2 - Sterge o persoana\n"
                    "3 - Editeaza o persoana\n")
    if optiune == '1':
        os.system('cls')
        adauga()
    elif optiune == '2':
        os.system('cls')
        sterge()
    elif optiune == '3':
        os.system('cls')
        editeaza()
    else:
        print("Optiune invalida!")
        time.sleep(1)
        os.system('cls')
        manager()


if __name__ == "__main__":
    manager()
