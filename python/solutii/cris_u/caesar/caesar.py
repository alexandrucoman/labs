#!/usr/bin/env python
# *-* coding: UTF-8 *-*


def decripteaza(mesaj):

    """Scrie in fisierul 'decript' posibilele decriptari"""

    newfisier = open("decript", "a")
    original = [item.lower() for item in mesaj]
    numere = [ord(item) for item in original]
    for index in range(1, 26):
        posibil = []
        for item in numere:
            if item >= 97 and item <= 122:
                if item-index >= 97:
                    posibil.append(chr(item-index))
                else:
                    amount = item - 97
                    posibil.append(chr(122-(index-amount)+1))
            else:
                posibil.append(chr(item))
        newfisier.write(''.join(posibil) + "\n")
    newfisier.write("\n\n")
    newfisier.close()


def main():

    """Fuctia principala?"""

    try:
        fisier = open("mesaje.secret", "r")
        mesaje = fisier.read()
        fisier.close()
    except IOError:
        print("Nu am putut obține mesajele.")
        return
    for mesaj in mesaje.splitlines():
        decripteaza(mesaj)


if __name__ == "__main__":
    main()

