"""Rezolvarea problemei Unic"""
#!/usr/bin/env python
# *-* coding: UTF-8 *-*

def gaseste(istoric):
    """Gaseste elementul fara duplicat."""
    element = istoric.pop()
    for numar in istoric:
        element = numar^element
    return element

if __name__ == "__main__":
    print gaseste([1, 2, 3, 4, 5, 1, 2, 3, 4])


