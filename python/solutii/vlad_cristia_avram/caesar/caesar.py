"""Rezolvare problema caesar"""

from __future__ import print_function


def gaseste_cheia(mesaj):
    """Aflam cheia mesajului"""
    prima_litera = mesaj[0]
    cheie = (ord('z') + 1 - ord(prima_litera))%26
    return cheie


def afiseaza_mesajul(mesaj, cheie):
    """Functie de afisare mesaj"""
    for litera in mesaj:
        aux2 = ord(litera)
        aux = ord('z')
        if litera.isalpha():
            if aux2 + cheie > aux:
                litera = chr(aux2 + cheie - aux + ord('a') - 1)
                print(litera, end="")
            else:
                litera = chr(aux2 + cheie)
                print(litera, end="")
        else:
            print(litera, end="")
    print()


def decripteaza_mesajul(mesaj):
    """Functia de decriptare a mesajului"""
    cheie = gaseste_cheia(mesaj)
    afiseaza_mesajul(mesaj, cheie)


def main():
    """Functia main a programului"""
    try:
        fisier = open("mesaje.secret", "r")
        mesaje = fisier.read()
        fisier.close()
    except IOError:
        print("Nu am putut obtine mesajele.")
        return

    for mesaj in mesaje.splitlines():
        decripteaza_mesajul(mesaj)


if __name__ == "__main__":
    main()
