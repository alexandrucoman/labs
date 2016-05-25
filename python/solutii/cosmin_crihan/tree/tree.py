# -*- coding: utf-8 -*-

"""
    Aplicatie care functioneaza asemanator comenzii "tree" din Linux
"""

import os

def tree(fisier, nivel):
    if nivel == 0:
        print(fisier)  # afisam directorul de pe nivelul 0

    fisiere = os.listdir(fisier)  # preluam lista de fisiere / foldere din directorul curent
    fisiere.sort()  # o sortam alfabetic

    for fisier_intern in fisiere:  # pentru fiecare fisier / folder din directorul curent

        # afisam atatea tab-uri cat e valoarea nivelului pe care suntem in arborele de fisiere
        for i in range(0, nivel):
            print("\t"),

        print(unicode(u"├── ")),  # afisam un simbol special pentru a marca "directorul contine"
        print(fisier_intern)  # afisam numele fisierului / folderului

        fisier_urmator=os.path.join(fisier, fisier_intern)  # construim calea completa a urmatorului fisier din arbore

        if os.path.isdir(fisier_urmator):  # daca fisierul urmator este un director
            tree(fisier_urmator, nivel + 1)  # atunci continuam parcurgerea in adancime, pe nivelul urmator

if __name__ == '__main__':
    tree(".", 0)