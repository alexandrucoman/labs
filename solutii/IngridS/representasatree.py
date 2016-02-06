"""Solutia problemei Reprezentarea unui director ca arbore"""
from __future__ import print_function
import os

def representastree(path_to_dir, depth=0):
    """Reprezentarea unui director ca arbore"""
    files_in_dir = os.listdir(path_to_dir)
    for filename in files_in_dir:
        print ('\t' * depth, filename)
        path = os.path.join(path_to_dir, filename)
        if os.path.isdir(path):
            representastree(path, depth+1)

