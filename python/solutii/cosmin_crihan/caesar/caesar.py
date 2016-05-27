#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""Împăratul a primit o serie de mesaje importante pe care este
important să le descifreze cât mai repede.

Din păcate mesagerul nu a apucat să îi spună împăratului care au fost
cheile alese pentru fiecare mesaj și tu ai fost ales să descifrezi
misterul.

Informații:
    În criptografie, cifrul lui Caesar este o metodă simplă de a cripta
un mesaj prin înlocuirea fiecărei litere cu litera de pe poziția aflată
la n pași de ea în alfabet (unde este n este un număr întreg cunoscut)
"""

from __future__ import print_function

# dictionar de frecvente de utilizare a literelor din alfabetul englez
# folosit pentru decriptarea cu brute-force
FREQ_DICT = {
    'a': 8.167,
    'b': 1.492,
    'c': 2.782,
    'd': 4.253,
    'e': 12.702,
    'f': 2.228,
    'g': 2.015,
    'h': 6.094,
    'i': 6.966,
    'j': 0.153,
    'k': 0.772,
    'l': 4.025,
    'm': 2.406,
    'n': 6.749,
    'o': 7.507,
    'p': 1.929,
    'q': 0.095,
    'r': 5.987,
    's': 6.327,
    't': 9.056,
    'u': 2.758,
    'v': 0.978,
    'w': 2.361,
    'x': 0.150,
    'y': 1.974,
    'z': 0.074
}


def decripteaza_mesajul(mesaj):
    """Funcția va primi un mesaj criptat folosind cifrul lui Caesar și
    va încerca să îl decripteze.
    """

    decriptat = []  # mesajul decriptat (lista de caractere)
    plauzibilitate_maxima = 0
    decriptat_plauzibil = []

    # 26 de litere (mici) posibile in alfabetul englez
    for n_cheie in range(1, 26):

        for litera in mesaj:  # decriptam fiecare litera in parte
            if litera in "., ":  # cu exceptia semnelor de punctuatie
                litera_decriptata = litera
            else:
                index_litera = (ord(litera) - ord('a') + n_cheie) % 26
                litera_decriptata = chr(index_litera + ord('a'))
            decriptat.append(litera_decriptata)

        print("\nn=%d: " % n_cheie, end='')

        for litera in decriptat:
            print(litera, end='')

        # verificam daca sirul decriptat este plauzibil, adica
        # are cel mai mare scor conform dictionarului de frecvente
        plauzibilitate = 0
        for litera in decriptat:
            if 'a' <= litera <= 'z':
                # adaugam frecventa de aparitie a literei curente la indicele
                # de plauzibilitate
                plauzibilitate += FREQ_DICT[litera]

        # daca mesajul este cel corect, atunci are un indice maxim
        if plauzibilitate > plauzibilitate_maxima:
            plauzibilitate_maxima = plauzibilitate
            decriptat_plauzibil = decriptat

        decriptat = []

    print("\n\nCel mai plauzibil mesaj "
          "este: %s" % "".join(decriptat_plauzibil))
    return "".join(decriptat_plauzibil)


def decripteaza_mesajul_n(mesaj, n_cheie):
    """Funcția va primi un mesaj criptat folosind cifrul lui Caesar și
    îl va decripta folosind cheia n trimisa ca parametru
    """

    decriptat = []

    for litera in mesaj:  # decriptam fiecare litera in parte
        if litera in "., ":  # cu exceptia semnelor de punctuatie
            litera_decriptata = litera
        else:
            # indicele literei in alfabet = ord(litera) - ord('a')
            index_litera = (ord(litera) - ord('a') + n_cheie) % 26
            litera_decriptata = chr(index_litera + ord('a'))
        decriptat.append(litera_decriptata)

    return "".join(decriptat)


def main():

    """ Main function docstring """
    try:
        fisier = open("mesaje.secret", "r")
        mesaje = fisier.read()
        fisier.close()
    except IOError:
        print("Nu am putut obține mesajele.")
        return

    try:
        mesaje_decriptate = open("mesaje.decriptate", "w")
    except IOError:
        print("Nu pot deschide fisierul de scriere a mesajelor decriptate.")
        return

    i = 1
    for mesaj in mesaje.splitlines():
        if i == 1:  # primul mesaj il decriptam prin incercari
            print("Primul mesaj decriptat prin incercari:")
            mesaje_decriptate.write("%s\n" % decripteaza_mesajul(mesaj))
        else:
            # urmatoarele mesaje le decriptam prin formula:
            # n = 26 - indice_prima_litera
            cheie = 26 - (ord(mesaj[0]) - ord('a'))
            mesaje_decriptate.write("%s\n" %
                                    decripteaza_mesajul_n(mesaj, cheie))
        i += 1

    mesaje_decriptate.close()

    print("\nMesajele au fost decriptate si plasate in fisierul "
          "\"mesaje.decriptate\"!")

if __name__ == "__main__":
    main()
