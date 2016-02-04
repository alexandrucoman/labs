import hashlib
import os

import time


def afisarefisier(curentPath):
    for item in os.listdir(curentPath):
        item = curentPath + os.path.sep + item
        if os.path.isfile(item):
            if open(item).read().__contains__("a"):
                print os.path.abspath(item)
        elif os.path.exists(item):
            afisarefisier(item)


# afisarefisier("..")
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def tree(curentPath, n):
    for item in os.listdir(curentPath):
        item = curentPath + os.path.sep + item
        if os.path.isfile(item):
            if open(item).read().__contains__("a"):
                print  "-" * n + bcolors.OKBLUE + os.path.basename(item)
        elif os.path.exists(item):
            print "-" * n + bcolors.OKGREEN + os.path.basename(item)
            tree(item, n + 1)


# tree("..", 0)


def compareFolders(first, second):
    second_dir = [item for item in os.listdir(second)]
    first_dir = [item for item in os.listdir(first)]
    for item_f in first_dir:
        if os.path.exists(os.path.join(first, item_f)) and os.path.isfile(os.path.join(first, item_f)):
            if item_f not in second_dir:
                print bcolors.BOLD + item_f + bcolors.OKBLUE + " Create"
                try:
                    open(os.path.join(second, item_f), 'wb').write(open(os.path.join(first, item_f), 'rb').read())
                except OSError:
                    print bcolors.FAIL + "Nu puteti crea fisiere aici!! " + second
            else:
                if hashlib.md5(open(os.path.join(first, item_f), 'rb').read()).hexdigest() == hashlib.md5(
                        open(os.path.join(second, item_f), 'rb').read()).hexdigest():
                    print bcolors.BOLD + item_f + bcolors.OKGREEN + " Identice"
                else:
                    print bcolors.BOLD + item_f + bcolors.WARNING + " Difera"
                    # TODO De terminat
                    if time.ctime(os.path.getmtime(os.path.join(first, item_f))) > time.ctime(
                            os.path.getmtime(os.path.join(second, item_f))):
                        open(os.path.join(first, item_f), 'ab').write(open(os.path.join(second, item_f), 'rb').read())
                    else:
                        open(os.path.join(second, item_f), 'ab').write(open(os.path.join(first, item_f), 'rb').read())
                        # TODO Trebuie de modificat - nu prea face bine

        elif os.path.exists(os.path.join(first, item_f)) and os.path.isdir(os.path.join(first, item_f)):
            if not os.path.exists(os.path.join(second, item_f)):
                try:
                    os.makedirs(second + os.path.sep + item_f)
                except OSError:
                    print bcolors.FAIL + "Nu puteti crea fisiere aici!! " + second
            compareFolders(os.path.join(first, item_f), os.path.join(second, item_f))


compareFolders("./test1", "./test2")
compareFolders("./test2", "./test1")
