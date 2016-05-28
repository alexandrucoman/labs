#!/usr/bin/env python
# *-* coding: UTF-8 *-*
# pylint: disable=unused-argument

def valid_xy(container, point):
    if ((point[0] >= 0 and point[0] <= len(container) - 1)
            and (point[1] >= 0 and point[1] <= len(container[0]) - 1)):
        return True
    return False

def umple_forma(imagine, punct):
    if not valid_xy(imagine, punct):
        return
    if imagine[punct[0]][punct[1]] == "*":
        return
    imagine[punct[0]][punct[1]] = "*"

    umple_forma(imagine, (punct[0] + 1, punct[1]))
    umple_forma(imagine, (punct[0] - 1, punct[1]))
    umple_forma(imagine, (punct[0], punct[1] + 1))
    umple_forma(imagine, (punct[0], punct[1] - 1))

def main():
    imaginea = [
        ["-", "-", "-", "-", "-", "*", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "-", "-", "-", "-", "-"],
        ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "*", "-", "-", "*", "-"],
        ["-", "-", "-", "-", "-", "*", "-", "*", "-", "-", "*", "-"],
    ]
    umple_forma(imaginea, (1, 3))
    umple_forma(imaginea, (5, 11))

if __name__ == "__main__":
    main()
    
