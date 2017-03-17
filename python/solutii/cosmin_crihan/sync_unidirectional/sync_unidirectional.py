"""
    Aplicatie care sincronizeaza 2 foldere, unidirectional
    (folder1 -> folder 2)
"""

from os import listdir
from os import path
from shutil import copy
from shutil import copytree


def sync_uni(fisier1, fisier2):
    """
    Sincronizeaza 2 foldere recursiv, cei 2 parametri sunt folderele de pe
    nivelul curent al recursiei.
    Sincronizarea este facuta intr-o singura directie: fisier1 -> fisier2
    :param fisier1:
    :param fisier2:
    :return:
    """

    # obtinem listele de fisiere din ambele directoare
    lista_f1 = listdir(fisier1)
    lista_f2 = listdir(fisier2)

    for fis in lista_f1:  # parcurgem lista de fisiere din directorul 1
        # construim calea completa a fisierului curent din parcurgere
        f_cu_cale = path.join(fisier1, fis)

        if path.isfile(f_cu_cale):  # daca este fisier
            if fis not in lista_f2:  # si nu este in directorul al doilea
                # il copiem in folderul dat de al doilea parametru
                # (din nivelul curent de parcurgere)
                copy(f_cu_cale, fisier2)

        elif path.isdir(f_cu_cale):  # daca este folder
            if fis not in lista_f2:  # si nu este in directorul al doilea
                # construim folderul destinatie cu cale completa
                folder_dest = path.join(fisier2, fis)
                # il copiem recursiv in folderul dat de al doilea parametru
                # (din nivelul curent de parcurgere)
                copytree(f_cu_cale, folder_dest)
            else:
                # daca exista in ambele directoare,
                # continuam parcurgerea in adancime
                sync_uni(f_cu_cale, f_cu_cale)


if __name__ == '__main__':
    sync_uni("dir1", "dir2")
