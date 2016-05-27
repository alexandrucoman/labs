#!/usr/bin/env python
"""
Functii auxiliare pentru syncronizarea fisierelor .
"""

from __future__ import print_function
import os
import shutil
import hashlib
import pickle

# standard keys in dict
FULL_PATH = "fullPath"
MD5 = "md5"
BASE_DIR = "baseDir"
LAST_EDIT = "lastEdit"
IS_FILE = "isFile"


def get_hash(path):
    """ Return the md5 of a file if it exists. """
    if os.path.exists(path) and os.path.isfile(path):
        try:
            fisier = open(path, "rb")
            data = fisier.read()
            fisier.close()
            return hashlib.md5(data).hexdigest()
        except IOError:
            return hashlib.md5(0)


def get_last_edit(path):
    """ Return last time a file was edited, if the file exists.
    If not, return None
    """
    if os.path.exists(path):
        return os.path.getmtime(path)
    else:
        return None


def write_sync_file(path, data):
    """ Scrie informatiile in fisieri .sync_unidirectional la pathul dat"""
    path = os.path.join(path, ".sync_unidirectional")
    try:
        sync_file = open(path, "wb")
        pickle.dump(data, sync_file)
        sync_file.close()
    except IOError:
        raise


def read_sync_file(path):
    """ returneaza informatiile din fisierul de sicronizare """
    path = os.path.join(path, ".sync_unidirectional")
    try:
        sync_file = open(path, "rb")
        data = pickle.load(sync_file)
        sync_file.close()
        return data
    except IOError:
        return None


def make_dirs(dest):
    """ creaza directoarele din destinatie  """
    paths_to_create = []
    dest_clone = dest
    while not os.path.exists(dest_clone):
        paths_to_create.insert(0, dest_clone)
        dest_clone = os.path.split(dest_clone)[0]
    for item in paths_to_create:
        os.mkdir(item)


def copy_r(source, dest):
    """ Copy the file from source to dest and create
    all the directory missing """
    base_directory = os.path.split(dest)[0]
    make_dirs(base_directory)

    shutil.copy(source, dest)


def get_same_file(item, info_b):
    """ cauta sa vada daca sunt fisiere in
    info_b, care au acelas md5, daca sunt le returneaza """
    md5_to_search = item[MD5]
    for item in info_b:
        if info_b[item][MD5] == md5_to_search:
            return item

    return None
