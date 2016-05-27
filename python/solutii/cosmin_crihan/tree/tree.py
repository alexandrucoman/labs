# -*- coding: utf-8 -*-

"""
    Aplicatie care functioneaza asemanator comenzii "tree" din Linux
"""

from __future__ import print_function
import os


def tree(fisier, nivel):
    """
        Afiseaza fisierele si folderele existente in directorul curent
        sub forma de arbore
    """
    if nivel == 0:
        print(fisier)  # afisam directorul de pe nivelul 0

    # preluam lista de fisiere / foldere din directorul curent
    fisiere_continute = os.listdir(fisier)
    fisiere_continute.sort()  # o sortam alfabetic

    # parcurgem fisierele / folderele de pe nivelul curent
    for fisier_intern in fisiere_continute:

        # afisam atatea tab-uri cat e valoarea nivelului
        # pe care suntem in arborele de fisiere
        print("\t" * nivel, end='')

        # afisam un simbol special pentru a marca "directorul contine"
        print(unicode(u"├── "), end='')
        print(fisier_intern)  # afisam numele fisierului / folderului

        # construim calea completa a fisierului
        fisier_intern_cu_cale = os.path.join(fisier, fisier_intern)

        # daca fisierul este un director
        if os.path.isdir(fisier_intern_cu_cale):
            # atunci continuam parcurgerea in adancime, pe nivelul urmator
            tree(fisier_intern_cu_cale, nivel + 1)

if __name__ == '__main__':
    tree(".", 0)
