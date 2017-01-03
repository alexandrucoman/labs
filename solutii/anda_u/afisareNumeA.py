"""
Programul afiseaza toate fisierele in a caror nume exista litera a.
"""
import os
def afisezFileA(fila):
    for item in os.listdir(fila):
        item=os.path.join(fila,item)
        if os.path.isfile(item) and ('a' in item) :
            print (item)
        if os.path.isdir(item):
            afisezFileA(item)
afisezFileA(".")
