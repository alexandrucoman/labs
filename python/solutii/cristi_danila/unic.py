#!/usr/bin/env python
# *-* coding: UTF-8 *-*
# pylint: disable=unused-argument

from __future__ import print_function

def gaseste_unic(istoric):
    """
    `Cercetatorul care...` implica ca ar fi doar unul. Deci, trebuie
    sa gasesc elementul al carui numar de ocurente este impar. Acel element
    reprezinta cercetatorul care sta dupa program.
    """

    for researcher in istoric:
        if istoric.count(researcher) % 2 != 0:
            return researcher

    return -1

if __name__ == "__main__":
    assert gaseste_unic([1, 2, 3, 2, 1]) == 3
    assert gaseste_unic([1, 1, 1, 2, 2]) == 1
