import os
from sys import argv


def unidirectional(loc1, loc2):

    """Recursiv creeaza fisiere conform director 1"""

    if os.path.exists(loc1):
        for fisier in os.listdir(loc1):
            fisier_actual_1 = os.path.join(loc1, fisier)
            fisier_actual_2 = os.path.join(loc2, fisier)
            if (os.path.exists(fisier_actual_1) and
               os.path.isdir(fisier_actual_1)):
                if not os.path.exists(fisier_actual_2):
                    os.system('mkdir \''+fisier_actual_2+'\'')
                unidirectional(fisier_actual_1, fisier_actual_2)
            else:
                if not os.path.exists(fisier_actual_2):
                    os.system('cp \'' + fisier_actual_1 + '\' \'' +
                              fisier_actual_2 + '\'')


def rm_files(loc1, loc2):

    """Recursiv sterge fisiere in plus din director 2"""

    if os.path.exists(loc2):
        for fisier in os.listdir(loc2):
            fisier_actual_1 = os.path.join(loc1, fisier)
            fisier_actual_2 = os.path.join(loc2, fisier)
            if (os.path.exists(fisier_actual_2) and
               os.path.isdir(fisier_actual_2)):
                rm_files(fisier_actual_1, fisier_actual_2)
                if not os.path.exists(fisier_actual_1):
                    if os.path.exists(fisier_actual_2):
                        os.system('rmdir \''+fisier_actual_2+'\'')
            else:
                if not os.path.exists(fisier_actual_1):
                    os.system('rm -f \''+fisier_actual_2+'\'')


if __name__ == "__main__":
    if len(argv) < 3:
        print "Argumente insuficiente: [dir_1] [dir_2]"
    else:
        if not os.path.exists(argv[1]):
            os.system('mkdir '+argv[1])
        if not os.path.exists(argv[2]):
            os.system('mkdir '+argv[2])
        while True:
            actualiz(argv[1], argv[2])
            rm_files(argv[1], argv[2])

