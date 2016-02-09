#!/usr/bin/env python
# *-* coding: UTF-8 *-*

"""Parcurge recursiv si afiseaza fisiere cu a in nume."""

import os


def fnc(cdir):
    """Cauta si afiseaza recursiv fisierele ce contin a."""
    for fisier in os.listdir(cdir):
        if os.path.isdir(os.path.join(cdir, fisier)):
            fnc(os.path.join(cdir, fisier))
        else:
            if 'a' in fisier.lower():
                print os.path.abspath(fisier)


if __name__ == "__main__":
    fnc("./rand")

