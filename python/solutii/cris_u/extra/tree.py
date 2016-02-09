import os


def fnc(cdir, level):

    """Afiseaza (relativ) arborescent structura director"""

    print '|___' * level, os.path.basename(cdir)
    for fisier in os.listdir(cdir):
        if os.path.isdir(os.path.join(cdir, fisier)):
            fnc(os.path.join(cdir, fisier), level+1)
        else:
            print '|___' * (level+1), os.path.basename(fisier)


if __name__ == "__main__":
    fnc("./cdir", 0)

