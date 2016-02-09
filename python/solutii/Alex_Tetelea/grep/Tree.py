import os
from BColors import BColors

# TODO - Terminat compareFolders - verificarea fisierelor cu nume identic
# TODO - De combinat verificarile bidirectionale intr-o functie


def tree(curentpath, n):
    """Afisarea Trrelui de fisiere/foldere din folderul respectiv
    :param n:
    :param curentpath:
    """
    for item in os.listdir(curentpath):
        item = curentpath + os.path.sep + item
        if os.path.isfile(item):
            if open(item).read().__contains__("a"):
                print("-" * n + BColors.OKBLUE + os.path.basename(item))
        elif os.path.exists(item):
            print "-" * n + BColors.OKGREEN + os.path.basename(item)
            tree(item, n + 1)


if __name__ == '__main__':
    path = ".."
    tree(path, 0)
