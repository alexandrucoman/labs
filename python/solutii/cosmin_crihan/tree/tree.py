# -*- coding: utf-8 -*-

"""
    Aplicatie care functioneaza asemanator comenzii "tree" din Linux
"""

import os


def tree(fisier, nivel):
    if nivel == 0:
        print(fisier)  # afisam directorul de pe nivelul 0

    fisiere_continute = os.listdir(fisier)  # preluam lista de fisiere / foldere din directorul curent
    fisiere_continute.sort()  # o sortam alfabetic

    # parcurgem fisierele / folderele de pe nivelul curent
    for fisier_intern in fisiere_continute:

        # afisam atatea tab-uri cat e valoarea nivelului pe care suntem in arborele de fisiere
        for i in range(0, nivel):
            print("\t"),

        print(unicode(u"├── ")),  # afisam un simbol special pentru a marca "directorul contine"
        print(fisier_intern)  # afisam numele fisierului / folderului

        fisier_intern_cu_cale=os.path.join(fisier, fisier_intern)  # construim calea completa a fisierului

        if os.path.isdir(fisier_intern_cu_cale):  # daca fisierul este un director
            tree(fisier_intern_cu_cale, nivel + 1)  # atunci continuam parcurgerea in adancime, pe nivelul urmator

if __name__ == '__main__':
    tree(".", 0)
