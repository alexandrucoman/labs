#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""Scrieți o funcție ce să determine dacă numărul primit
ca argument este par.

Cerințe:
    - Se va folosi structura condițională if-elif-else
"""


def par(numar):
    """Funcție ce determină dacă un număr este par."""
    return bool(numar % 2 == 0)

if __name__ == "__main__":
    assert not par(1)
    assert par(2)
    assert not par(3)
