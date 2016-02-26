
"""
This is a program for sync two path while running.
"""

import os
import hashlib
import time
import shutil


def searchfordifference(path_from, path_to):
    """
    This function search for difference between files
    :param path_from:
    :param path_to:
    :return:
    """
    hasher_from = hashlib.md5()
    hasher_to = hashlib.md5()
    with open(path_from, "rb") as afile:
        buffer = afile.read()
        hasher_from.update(buffer)
    with open(path_to, "rb") as afile:
        buffer = afile.read()
        hasher_to.update(buffer)
    if hasher_from.digest() == hasher_to.digest():
        return False
    else:
        return True


def syncFiles(from_file, to_file):
    """
    This function sync files from params
    :param from_file:
    :param to_file:
    :return:
    """


def syncallfiles(path_from, path_to, time_dir1, time_dir2):
    """
    This function find all files that have param key
    :param path_from:
    :param path_to:
    :param time_dir1:
    :param time_dir2:
    :return:
    """
    for file in os.listdir(path_from):
        file_from = os.path.join(path_from, file)
        file_to = os.path.join(path_to, file)
        if os.path.isdir(file_from):
            if time_dir1 > time_dir2:
                if not os.path.isdir(file_to):
                    os.mkdir(file_to)
            else:
                if not os.path.isdir(file_to):
                    shutil.rmtree(file_from)
            syncallfiles(file_from, file_to, time_dir1, time_dir2)
        if os.path.isfile(file_from):
            if not os.path.isfile(file_to):
                if time_dir1 > time_dir2:
                    shutil.copyfile(file_from, file_to)
                else:
                    os.remove(file_from)
            else:
                if searchfordifference(file_from, file_to):
                    time_from = time.ctime(os.path.getmtime(file_from))
                    time_to = time.ctime(os.path.getmtime(file_to))
                    if time_from > time_to:
                        os.remove(file_to)
                        shutil.copyfile(file_from, file_to)
                    else:
                        os.remove(file_from)
                        shutil.copyfile(file_to, file_from)
                    #syncFiles(file_from, file_to)


def main(first, second):
    """
    This is the main function"
    :param first:
    :param second:
    """
    while True:
        time.sleep(0.2)
        time_dir1 = time.ctime(os.path.getmtime(first))
        time_dir2 = time.ctime(os.path.getmtime(second))
        if time_dir1 > time_dir2:
            syncallfiles(first, second, time_dir1, time_dir2)
        else:
            syncallfiles(second, first, time_dir2, time_dir1)

if __name__ == "__main__":
    main("recursiv1", "recursiv2")
