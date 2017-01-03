"""
Programul sincronizezaza p1 cu p2(path-uri catre foldere) .Orice modificare in p1 , se realizeaza automat in p2.
"""
import os
from shutil import copy

def sincronFisiere(path1,path2):
    for item in os.listdir(path1):
        item_path1=os.path.join(path1,item)
        item_path2=os.path.join(path2,item)
        if item in os.listdir(path2):
            pass
        else:
            if os.path.isfile(item_path1):
                copy(item_path1,item_path2)
            if os.path.isdir(item_path1):
                    os.makedirs(item_path2)
                    sincronFisiere(item_path1,item_path2)


#schimba path-uri
p1="C:\\Users\\Anda\Documents\\Visual Studio 2013\\Projects\\examenPoo\\PythonApplication1\\PythonApplication1\\aname"
p2="C:\\Users\\Anda\Documents\\Visual Studio 2013\\Projects\\examenPoo\\PythonApplication1\\PythonApplication1\\anda_solutie"
while ((p1 is p2)==False):
    sincronFisiere(p1,p2)
