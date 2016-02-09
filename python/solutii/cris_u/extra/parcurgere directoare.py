import os


def fnc(cdir):

    """Afiseaza recursiv fisierele ce contin 'a'"""

    for fisier in os.listdir(cdir):
        if os.path.isdir(os.path.join(cdir, fisier)):
            fnc(os.path.join(cdir, fisier))
        else:
            if 'a' in fisier:
                print os.path.abspath(fisier)


if __name__ == "__main__":
    fnc("./rand")

