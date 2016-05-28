"""Rezolvarea problemei Iterarea printr-un director"""
from __future__ import print_function
import os

def iteration(path_to_dir):
    """Iterarea printr-un director"""
    for filename in os.listdir(path_to_dir):
        path = os.path.join(path_to_dir, filename)
        if os.path.isfile(path):
            if "a" in filename:
                print(filename)

        if os.path.isdir(path):
            iteration(path)

