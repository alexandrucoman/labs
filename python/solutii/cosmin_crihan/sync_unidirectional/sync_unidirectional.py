"""
    Aplicatie care sincronizeaza 2 foldere, unidirectional (folder1 -> folder 2)
"""

from os import listdir, path
from shutil import copy, copytree


def sync_uni(fisier1, fisier2):

    # obtinem listele de fisiere din ambele directoare
    lista_f1 = listdir(fisier1)
    lista_f2 = listdir(fisier2)

    for f in lista_f1:  # parcurgem lista de fisiere din directorul 1
        f_cu_cale = path.join(fisier1, f)  # construim calea completa a fisierului curent din parcurgere

        if path.isfile(f_cu_cale):  # daca este fisier
            if f not in lista_f2:  # si nu este in directorul al doilea
                copy(f_cu_cale, fisier2)  # il copiem in folderul dat de al doilea parametru (din nivelul curent de parcurgere)

        elif path.isdir(f_cu_cale):  # daca este folder
            if f not in lista_f2:  # si nu este in directorul al doilea
                folder_dest = path.join(fisier2, f)  # construim folderul destinatie cu cale completa
                copytree(f_cu_cale, folder_dest)  # il copiem recursiv in folderul dat de al doilea parametru (din nivelul curent de parcurgere)
            else:
                sync_uni(f_cu_cale, f_cu_cale)  # daca exista in ambele directoare, continuam parcurgerea in adancime


if __name__ == '__main__':
    sync_uni("dir1", "dir2")