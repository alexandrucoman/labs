
"""
This is a program for sync two path while running.
"""

import os
import hashlib
import time
import shutil


class Tree(object):
    """
    this class build a dir structure.
    """
    def __init__(self, path):
        self.path = path
        self.dirstr = {}
        self.dirstr['last_mod'] = self.getlastdate(self.path)
        self.dirstr['path'] = path
        self.dirstr['type'] = 0
        self.dirstr['subdir'] = {}
        self.build(self.path, self.dirstr)

    def build(self, path, dir, stare=False):
        """
        Function auto-call on create it self
        :param path:
        :param dir:
        :param stare:
        :return:
        """
        for file in os.listdir(path):
            path_file = os.path.join(path, file)
            if os.path.isdir(path_file):
                dir['subdir'][path_file] = {
                    "type": 0,
                    "last_mod": self.getlastdate(path_file),
                    "path": path_file,
                    "subdir": {}
                }
                self.build(path_file, dir['subdir'][path_file])
            if os.path.isfile(path_file):
                dir['subdir'][path_file] = {
                    "type": 1,
                    "last_mod": self.getlastdate(path_file),
                    "path": path_file,
                    "edit": stare,
                    "encrypt": self.encrypt(path_file)
                }

    def encrypt(self, path):
        """
        this function encrypt content of file
        :param path:
        :return:
        """
        hasher = hashlib.md5()
        with open(path, "rb") as afile:
            buffer = afile.read()
            hasher.update(buffer)
            return hasher.digest()


    def update(self, path=None, dir=None):
        """
        this function update structure of tree.
        :param path:
        :param dir:
        :return:
        """
        if dir == None:
            dir = self.dirstr
        if path == None:
            path = self.dirstr['path']
        for file in os.listdir(path):
            path_file = os.path.join(path, file)
            if os.path.isdir(path_file):
                if path_file not in dir['subdir'].keys():
                    dir['subdir'][path_file] = {
                        "type": 0,
                        "last_mod": self.getlastdate(path_file),
                        "path": path_file,
                        "subdir": {}
                    }
                    self.update(path_file, dir['subdir'][path_file])
                else:
                    dir['subdir'][path_file]['last_mod'] = self.getlastdate(path_file)
                    self.update(path_file, dir['subdir'][path_file])
            if os.path.isfile(path_file):
                if path_file not in dir['subdir'].keys():
                    dir['subdir'][path_file] = {
                        "type": 1,
                        "last_mod": self.getlastdate(path_file),
                        "path": path_file,
                        "edit": False,
                        "encrypt": self.encrypt(path_file)
                    }
                else:
                    hash = self.encrypt(path_file)
                    if dir['subdir'][path_file]['encrypt'] != hash:
                        dir['subdir'][path_file]['encrypt'] = hash
                        dir['subdir'][path_file]['edit'] = True
                        dir['subdir'][path_file]["last_mod"] = self.getlastdate(path_file)
        return


    def getlastdate(self, path):
        """
        returneaza ultima actualizare a unui fisier/folder
        :param path:
        :return:
        """
        modificare = os.path.getmtime(path)
        return time.ctime(modificare)


    def sync(self, structure1, structure2, path1, path2):
        """
        :param structure1:
        :param structure2:
        :return:
        """
        forremove = []
        for path_2 in structure2['subdir']:
            path_1 = path_2.replace(path2, path1)
            if os.path.isfile(path_2):
                #Este fisier dar nu se gaseste in al doilea folder.
                if not os.path.isfile(path_1):
                    #Daca fisierul a fost sters inainte de ultima modificare a celui existent
                    if self.getlastdate(structure1['path']) > self.getlastdate(path_2):
                        os.remove(path_2)
                        print(path_2, " was removed.")
                        forremove.append(path_2)
                    else:
                        shutil.copy2(path_2, path_1)
                        print(path_1, " sync with ", path_2)
                #Este fisier, se gaseste si in al doilea folder, dar sunt diferite.
                if os.path.isfile(path_1):
                    if self.encrypt(path_1) != self.encrypt(path_2):
                        #Daca fisierul din folder1 a fost modificat ultima data.
                        if self.getlastdate(path_1) > self.getlastdate(path_2):
                            shutil.copy2(path_1, path_2)
                            print(path_2, " sync with ", path_1)
                        #Daca fisierul din folder2 a fost modificat ultima data.
                        else:
                            shutil.copy2(path_2, path_1)
                            print(path1, " sync with ", path_2)
            if os.path.isdir(path_2):
                #este director dar nu se gaseste in al doilea folder
                if not os.path.isdir(path_1):
                    if self.getlastdate(structure1['path']) > self.getlastdate(path_2):
                        shutil.rmtree(path_2)
                        print(path_2, " was removed.")
                        forremove.append(path_2)
                    else:
                        shutil.copytree(path_2, path_1)
                        print(path1, " sync with ", path_2)
                if os.path.isdir(path_1) and path_1 in structure1['subdir'].keys():
                    self.sync(structure1['subdir'][path_1], structure2['subdir'][path_2], path1, path2)
        for item in forremove:
            if item in structure1['subdir'].keys() and item in structure2['subdir'].keys():
                del(structure1['subir'][item])
                del(structure2['subdir'][item])
            if item in structure1['subdir'].keys():
                del(structure1['subdir'][item])
            elif item in structure2['subdir'].keys():
                del(structure2['subdir'][item])




    def find_difference_with(self, with_dir):
        """
        :param dir:
        :param with_dir:
        :return:
        """
        structure1 = self.dirstr
        structure2 = with_dir.dirstr
        self.sync(structure1, structure2, self.path, with_dir.path)
        self.sync(structure2, structure1, with_dir.path, self.path)
        self.update()
        with_dir.update()



def main(first, second):
    """
    This is the main function"
    :param first:
    :param second:
    """
    director1 = Tree(first)
    director2 = Tree(second)
    while True:
        time.sleep(1)
        director1.find_difference_with(director2)

if __name__ == "__main__":
    main("recursiv1", "recursiv2")
