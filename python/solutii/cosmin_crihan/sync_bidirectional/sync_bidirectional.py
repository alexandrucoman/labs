"""
    Aplicatie care sincronizeaza 2 foldere, bidirectional
    (folder1 <-> folder 2)
"""

from os import listdir
from os import path
from shutil import copy
from shutil import copytree


def sync_bi(fisier1, fisier2):
    """
    Sincronizeaza 2 foldere recursiv, cei 2 parametri sunt folderele de pe
    nivelul curent al recursiei.
    Sincronizarea este facuta in ambele directii: fisier1 <-> fisier2
    :param fisier1:
    :param fisier2:
    :return:
    """

    # obtinem listele de fisiere din ambele directoare
    lista_f1 = listdir(fisier1)
    lista_f2 = listdir(fisier2)

    # directia folder1 -> folder2
    for fis1 in lista_f1:  # parcurgem lista de fisiere din directorul 1
        # construim calea completa a fisierului curent din parcurgere
        fis1_cu_cale = path.join(fisier1, fis1)

        if path.isfile(fis1_cu_cale):  # daca este fisier
            if fis1 not in lista_f2:  # si nu este in directorul al doilea
                # il copiem in folderul dat de al doilea parametru
                # (din nivelul curent de parcurgere)
                copy(fis1_cu_cale, fisier2)

        elif path.isdir(fis1_cu_cale):  # daca este folder
            if fis1 not in lista_f2:  # si nu este in directorul al doilea
                # construim folderul destinatie cu cale completa
                folder_dest = path.join(fisier2, fis1)
                # il copiem recursiv in folderul dat de al doilea parametru
                # (din nivelul curent de parcurgere)
                copytree(fis1_cu_cale, folder_dest)
            else:
                # daca exista in ambele directoare,
                # continuam parcurgerea in adancime
                sync_bi(fis1_cu_cale, fis1_cu_cale)

    # directia folder2 -> folder1
    for fis2 in lista_f2:  # parcurgem lista de fisiere din directorul 2
        fis2_cu_cale = path.join(fisier2, fis2)

        if path.isfile(fis2_cu_cale):  # daca este fisier
            if fis2 not in lista_f1:  # si nu este in primul director
                # il copiem in folderul dat de primul parametru
                # (din nivelul curent de parcurgere)
                copy(fis2_cu_cale, fisier1)

        elif path.isdir(fis2_cu_cale):  # daca este folder
            if fis2 not in lista_f1:  # si nu este in pimul director
                # construim folderul destinatie cu cale completa
                folder_dest = path.join(fisier1, fis2)
                # il copiem recursiv in folderul dat primul parametru
                # (din nivelul curent de parcurgere)
                copytree(fis2_cu_cale, folder_dest)
            else:
                # daca exista in ambele directoare,
                # continuam parcurgerea in adancime
                sync_bi(fis2_cu_cale, fis2_cu_cale)


if __name__ == '__main__':
    sync_bi("dir1", "dir2")
