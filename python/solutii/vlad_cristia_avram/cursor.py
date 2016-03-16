"""Solutie pentru problema cursor"""


def modifica_punct(directie, valoare):
    """Functie de aflare a modificarilor ce trebuie facute asupra punctelor"""
    punct = [0, 0]
    if directie == "STANGA":
        punct[0] = punct[0] - valoare
    elif directie == "DREAPTA":
        punct[0] = punct[0] + valoare
    elif directie == "SUS":
        punct[1] = punct[1] + valoare
    elif directie == "JOS":
        punct[1] = punct[1] - valoare
    return punct


def calculeaza_distanta(punct):
    """Functie matematica de a afla distantai"""
    dist = (punct[0] ** 2 + punct[1] ** 2) ** 0.5
    return dist


def distanta(cale):
    """Functia de baza a programului"""
    try:
        fisier = open(cale, "r")
        mesaj = fisier.read()
        fisier.close()
    except IOError:
        return "Fisierul istoric.tuxy nu exista."
    punct = [0, 0]
    modificare = [0, 0]
    directie = ""
    valoare = 0
    for linie in mesaj.splitlines():
        for cuvant in linie.split():
            if directie == "":
                if cuvant == "STANGA" or cuvant == "DREAPTA" or \
                   cuvant == "SUS" or cuvant == "JOS":
                    directie = cuvant
            else:
                try:
                    cuvant = int(cuvant)
                    valoare = cuvant
                    modificare = modifica_punct(directie, valoare)
                    punct[0] = punct[0] + modificare[0]
                    punct[1] = punct[1] + modificare[1]
                    directie = ""
                except ValueError:
                    return "Fisierul dumneavoastra nu respecta template-ul."

    dist = calculeaza_distanta(punct)
    return dist


if __name__ == "__main__":
    distanta("istoric.tuxy")
