import hashlib
import os
import time
from BColors import BColors


# TODO - Terminat compareFolders - verificarea fisierelor cu nume identic
# TODO - De combinat verificarile bidirectionale intr-o functie


def comparefolders(first, second):
    """Comparam un folder cu altul si cream fisierele ce nu ajung
    :param second:
    :param first:
    """
    second_dir = [item for item in os.listdir(second)]
    first_dir = [item for item in os.listdir(first)]
    for item_f in first_dir:
        if os.path.exists(os.path.join(first, item_f)) \
                and os.path.isfile(os.path.join(first, item_f)):
            if item_f not in second_dir:
                print BColors.BOLD + item_f + BColors.OKBLUE + " Create"
                try:
                    open(os.path.join(second, item_f), 'wb'). \
                        write(open(os.path.join(first, item_f), 'rb').read())
                except OSError:
                    print BColors.FAIL + "Nu puteti " \
                                         "crea fisiere aici!! " + second
            else:
                if hashlib.md5(open(os.path.join(first, item_f),
                                    'rb').read()).hexdigest() == hashlib.md5(
                    open(os.path.join(second, item_f), 'rb').read()). \
                        hexdigest():
                    print BColors.BOLD + item_f + BColors.OKGREEN + " Identice"
                else:
                    print BColors.BOLD + item_f + BColors.WARNING + " Difera"
                    # TODO De terminat
                    if time.ctime(os.path.getmtime(
                            os.path.join(first, item_f))) > \
                            time.ctime(os.path.getmtime(
                                os.path.join(second, item_f
                                             ))):
                        open(os.path.join(first, item_f), 'ab').write(
                            open(os.path.join(second, item_f), 'rb').read()
                        )
                    else:
                        open(os.path.join(second, item_f), 'ab').write(
                            open(os.path.join(first, item_f), 'rb').read())
                        # TODO Trebuie de modificat - nu prea face bine

        elif os.path.exists(os.path.join(first, item_f)) \
                and os.path.isdir(os.path.join(first, item_f)):
            if not os.path.exists(os.path.join(second, item_f)):
                try:
                    os.makedirs(second + os.path.sep + item_f)
                except OSError:
                    print BColors.FAIL + "Nu puteti " \
                                         "crea fisiere aici!! " + second
            comparefolders(os.path.join(
                first, item_f), os.path.join(second, item_f))


if __name__ == '__main__':
    comparefolders("./test1", "./test2")
    comparefolders("./test2", "./test1")
