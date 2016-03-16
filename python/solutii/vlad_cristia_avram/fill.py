"""Rezolvare pentru problema fill"""


def afiseaza_imagine(imagine):
    """Functie de afisare a imaginii"""
    print()
    for linii in imagine:
        for coloane in linii:
            print(coloane, end='')
        print()
    print()


def continuare(imagine, punct):
    """Functie de colorare a imaginii"""
    try:
        pntx = punct[0]
        pnty = punct[1]
        len0 = len(imagine)
        len1 = len(imagine[1])
        if imagine[pntx][pnty] == "*" or pntx < 0 or pnty < 0 or\
           pntx > len0 or pnty > len1:
            return
        else:
            imagine[punct[0]][punct[1]] = "*"
            continuare(imagine, (punct[0], punct[1] + 1))
            continuare(imagine, (punct[0], punct[1] - 1))
            continuare(imagine, (punct[0] + 1, punct[1]))
            continuare(imagine, (punct[0] - 1, punct[1]))
    except IndexError:
        return


def umple_forma(imagine, punct):
    """Functia care verifica acuratetea datelor si da acces\
la functia de umplere"""
    x_point = punct[0]
    y_point = punct[1]
    lines = len(imagine)
    columns = len(imagine[1])
    afiseaza_imagine(imagine)
    if x_point >= 0 and y_point >= 0 and x_point <= lines and\
       y_point <= columns:
        continuare(imagine, punct)
        afiseaza_imagine(imagine)
    else:
        print("Punctul dat este inafara matricei.")
        return


def main():
    """Functia main"""
    imaginea = [
        ["-", "-", "-", "-", "-", "*", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "-", "-", "-", "-", "-"],
        ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "*", "-", "-", "*", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "*", "-", "-", "*", "-"],
    ]
    umple_forma(imaginea, (1, 3))
    umple_forma(imaginea, (5, 11))


if __name__ == "__main__":
    main()
