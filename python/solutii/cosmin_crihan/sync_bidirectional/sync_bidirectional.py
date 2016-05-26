"""
    Aplicatie care sincronizeaza 2 foldere, bidirectional (folder1 <-> folder 2)
"""

from os import listdir, path
from shutil import copy, copytree


def sync_bi(fisier1, fisier2):

    # obtinem listele de fisiere din ambele directoare
    lista_f1 = listdir(fisier1)
    lista_f2 = listdir(fisier2)

    # directia folder1 -> folder2
    for f1 in lista_f1:  # parcurgem lista de fisiere din directorul 1
        f1_cu_cale = path.join(fisier1, f1)  # construim calea completa a fisierului curent din parcurgere

        if path.isfile(f1_cu_cale):  # daca este fisier
            if f1 not in lista_f2:  # si nu este in directorul al doilea
                copy(f1_cu_cale, fisier2)  # il copiem in folderul dat de al doilea parametru (din nivelul curent de parcurgere)

        elif path.isdir(f1_cu_cale):  # daca este folder
            if f1 not in lista_f2:  # si nu este in directorul al doilea
                folder_dest = path.join(fisier2, f1)  # construim folderul destinatie cu cale completa
                copytree(f1_cu_cale, folder_dest)  # il copiem recursiv in folderul dat de al doilea parametru (din nivelul curent de parcurgere)
            else:
                sync_bi(f1_cu_cale, f1_cu_cale)  # daca exista in ambele directoare, continuam parcurgerea in adancime

    # directia folder2 -> folder1
    for f2 in lista_f2:  # parcurgem lista de fisiere din directorul 2
        f2_cu_cale = path.join(fisier2, f2)

        if path.isfile(f2_cu_cale):  # daca este fisier
            if f2 not in lista_f1:  # si nu este in primul director
                copy(f2_cu_cale,
                     fisier1)  # il copiem in folderul dat de primul parametru (din nivelul curent de parcurgere)

        elif path.isdir(f2_cu_cale):  # daca este folder
            if f2 not in lista_f1:  # si nu este in pimul director
                folder_dest = path.join(fisier1, f2)  # construim folderul destinatie cu cale completa
                copytree(f2_cu_cale,
                         folder_dest)  # il copiem recursiv in folderul dat primul parametru (din nivelul curent de parcurgere)
            else:
                sync_bi(f2_cu_cale, f2_cu_cale)  # daca exista in ambele directoare, continuam parcurgerea in adancime


if __name__ == '__main__':
    sync_bi("dir1", "dir2")