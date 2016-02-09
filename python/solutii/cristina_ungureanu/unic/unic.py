#!/usr/bin/env python
# *-* coding: UTF-8 *-*

"""Contine functie ce gaseste unic din lista."""


def gaseste(istoric):
    """Cauta si intoarce elementul unic din lista."""
    for i in range(1, len(istoric)):
        istoric[0] = istoric[0] ^ istoric[i]
    return istoric[0]


if __name__ == "__main__":
    assert gaseste([1, 2, 3, 2, 1]) == 3
    assert gaseste([1, 1, 1, 2, 2]) == 1

