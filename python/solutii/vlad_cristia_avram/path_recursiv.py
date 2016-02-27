"""cautare recursiva in fisier"""


import os


def afla_calea(cale):
    """Functia de generat calea fisierului"""
    fisiere = os.listdir(cale)
    for fil in fisiere:
        curent = os.path.join(cale, fil)
        if os.path.isdir(curent):
            afla_calea(curent)
        elif os.path.isfile:
            if "a" in curent:
                print(curent)


if __name__ == "__main__":
    afla_calea(os.curdir)
