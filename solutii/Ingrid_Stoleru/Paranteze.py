#!/usr/bin/env python
# *-* coding: UTF-8 *-*

Stiva= list()
def este_corect(expresie):
    i=0
    length=len(expresie)
    while i<length:
        if expresie[i] == "(" or expresie[i] == "[":
            Stiva.append(expresie[i])
        else:
            if expresie[i] == ")":
                if not Stiva or Stiva.pop() == "[":
                    print ("Nu este corect")
                    return 0
            if expresie[i] == "]":
                if not Stiva or Stiva.pop() == "(":
                    print ("Nu este corect")
                    return 0
        i=i+1

    if not Stiva:
        return 1
    else:
        return 0

if __name__ == "__main__":
    expresie="[(())]"
    print (este_corect(expresie))



