"""
Programul afiseaza identatat continutul folderului curent (precum functia din git)
"""
import os
def afisezFisier(path):
    for item in os.listdir(path):
        path_item=os.path.join(path,item)
        print ( '-' , item)
        if os.path.isdir(path_item) :
           print ("\t-" +item )
afisezFisier(".")
