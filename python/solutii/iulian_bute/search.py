#!/usr/bin/env python
''' cauta intr-un director dat fisierele ce contin in nume o cheie '''
import os


def cauta_fisiere(path, key):
    ''' cauta intr-un director dat fisierele ce contin in nume o cheie '''
    for root, _, files in os.walk(path):
        for nume_fisier in files:
            if key in nume_fisier:
                print os.path.join(root, nume_fisier)


def main():
    ''' cauta intr-un director dat fisierele ce contin in nume o cheie '''
    key = ".py"
    path = "../../exercitii"
    cauta_fisiere(path, key)


if __name__ == "__main__":
    main()
