#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""Rezolvarea problemei Fill"""
def umple(imagine, point):
    """Fill the matrix"""
    coordonata_x = point[0]
    coordonata_y = point[1]
    if imagine[coordonata_x][coordonata_y] != '*':
        imagine[coordonata_x][coordonata_y] = '*'
    if coordonata_x > 0 and imagine[coordonata_x-1][coordonata_y] != '*':
        umple(imagine, (point[0]-1, point[1]))
    if (coordonata_x < len(imagine[coordonata_y]) - 1 and
            imagine[coordonata_x+1][coordonata_y] != '*'):
        umple(imagine, (point[0]+1, point[1]))
    if (coordonata_y > 0 and
            imagine[coordonata_x][coordonata_y-1] != '*'):
        umple(imagine, (point[0], point[1]-1))
    if (coordonata_y < len(imagine) - 1 and
            imagine[coordonata_x][coordonata_y+1] != '*'):
        umple(imagine, (point[0], point[1]+1))
    return imagine

def main():
    """Apelarea functiei"""
    imaginea = [
        ["-", "-", "-", "-", "-", "*", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "-", "-", "-", "-", "-"],
        ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "*", "-", "-", "*", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "*", "-", "-", "*", "-"],
    ]
    punct = (1, 3)
    print umple(imaginea, punct)

if __name__ == "__main__":
    main()

