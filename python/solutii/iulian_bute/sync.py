#!/usr/bin/env python
""" Sincronizarea a doua directoare """
import os
import time
import shutil
# pylint: disable=too-many-locals
# pylint: disable=global-statement

OLD_FILESET = dict()


def copyfile(src, dest):
    """ Copiaza fisiere cu metadate """
    destinatie = os.path.split(dest)
    dest = destinatie[0]
    if not os.path.exists(dest):
        os.makedirs(dest)
    shutil.copy2(src, dest)


def get_fileset(path):
    """ Construieste lista de fisiere din directorul dat si din subdirectoare,
        cu data ultimei moficari """
    fileset = dict()
    for root, _, files in list(os.walk(path)):
        if not os.path.islink(root):
            for fname in files:
                cfil = os.path.join(os.path.relpath(root, path), fname)
                fileset[cfil] = int(os.path.getmtime(os.path.join(path, cfil)))
    return fileset


def sync_folders(folder1, folder2):
    """ Functia de sincronizare a directoarelor """
    fileset1 = get_fileset(folder1)
    files1 = set(fileset1.keys())
    fileset2 = get_fileset(folder2)
    files2 = set(fileset2.keys())
    total_files = files1.union(files2)
    common_files = files1.intersection(files2)
    ch_comm_files = {o for o in common_files if fileset1[o] != fileset2[o]}
    ch_fs1_files = {o for o in ch_comm_files if fileset1[o] > fileset2[o]}
    ch_fs2_files = {o for o in ch_comm_files if fileset2[o] > fileset1[o]}
    files_only_in_set1 = total_files - files2
    files_only_in_set2 = total_files - files1
    deleted_set1 = files_only_in_set2.intersection(set(OLD_FILESET.keys()))
    deleted_set2 = files_only_in_set1.intersection(set(OLD_FILESET.keys()))
    new_files_in_set1 = files_only_in_set1 - deleted_set2
    new_files_in_set2 = files_only_in_set2 - deleted_set1
    for fisier in new_files_in_set1.union(ch_fs1_files):
        copyfile(os.path.join(folder1, fisier), os.path.join(folder2, fisier))
        print "se copiaza 1->2 ", fisier
    for fisier in new_files_in_set2.union(ch_fs2_files):
        copyfile(os.path.join(folder2, fisier), os.path.join(folder1, fisier))
        print "se copiaza 2->1 ", fisier
    for fisier in deleted_set1:
        os.remove(os.path.join(folder2, fisier))
        print "se sterge din 2 ", fisier
    for fisier in deleted_set2:
        os.remove(os.path.join(folder1, fisier))
        print "se sterge din 1 ", fisier


def main():
    """ Sincronizeaza 2 directoare """
    global OLD_FILESET
    folder1 = "/home/iulian/Desktop/testSync/A"
    folder2 = "/home/iulian/Desktop/testSync/B"
    interval_sincronizare = 10   # sec
    while 1:
        sync_folders(folder1, folder2)
        OLD_FILESET = get_fileset(folder1)
        time.sleep(interval_sincronizare)


if __name__ == "__main__":
    main()
