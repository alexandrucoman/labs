
"""
This is a program for sync two path while running.
"""

import os
import hashlib
import time
import shutil

class tree(object):
    def __init__(self, path):
        self.path = path
        self.dir = {}
        self.dir['last_mod'] = time.ctime(os.path.getmtime(self.path))
        self.dir['path'] = path
        self.dir['type'] = 0
        self.dir['subdir'] = {}
        self.build(self.path, self.dir)


    def build(self, path, dir, stare=False):
        for file in os.listdir(path):
            path_file = os.path.join(path, file)
            if os.path.isdir(path_file):
                dir['subdir'][path_file] = {
                    "type": 0,
                    "last_mod": time.ctime(os.path.getmtime(path_file)),
                    "path": path_file,
                    "subdir": {}
                }
                self.build(path_file, dir['subdir'][path_file])
            if os.path.isfile(path_file):
                dir['subdir'][path_file] = {
                    "type": 1,
                    "last_mod": time.ctime(os.path.getmtime(path_file)),
                    "path": path_file,
                    "edit": stare,
                    "encrypt": self.encrypt(path_file)
                }


    def encrypt(self, path):
        hasher = hashlib.md5()
        with open(path, "rb") as afile:
            buffer = afile.read()
            hasher.update(buffer)
            return hasher.digest()


    def auto_remove(self, dir):
        if dir == None:
            dir = self.dir
        forRemove = []
        if 'subdir' in dir:
            for path in dir['subdir']:
                if not os.path.exists(dir['subdir'][path]['path']):
                    forRemove.append(path)
                if os.path.isdir(dir['subdir'][path]['path']):
                    self.auto_remove(dir['subdir'][path])

        for item in forRemove:
            del(dir['subdir'][item])


    def update(self, path=None, dir=None):
        if dir == None:
            dir = self.dir
        if path == None:
            path = self.dir['path']
        forRemove = []
        for file in os.listdir(path):
            path_file = os.path.join(path, file)
            if os.path.isdir(path_file):
                if path_file not in dir['subdir'].keys():
                    dir['subdir'][path_file] = {
                        "type": 0,
                        "last_mod": time.ctime(os.path.getmtime(path_file)),
                        "path": path_file,
                        "subdir": {}
                    }
                    self.update(path_file, dir['subdir'][path_file])
                else:
                    dir['subdir'][path_file]['last_mod'] = time.ctime(os.path.getmtime(path_file))
                    self.update(path_file, dir['subdir'][path_file])
            if os.path.isfile(path_file):
                if path_file not in dir['subdir'].keys():
                    dir['subdir'][path_file] = {
                        "type": 1,
                        "last_mod": time.ctime(os.path.getmtime(path_file)),
                        "path": path_file,
                        "edit": False,
                        "encrypt": self.encrypt(path_file)
                    }
                else:
                    hash = self.encrypt(path_file)
                    if dir['subdir'][path_file]['encrypt'] != hash:
                        dir['subdir'][path_file]['encrypt'] = hash
                        dir['subdir'][path_file]['edit'] = True
                        dir['subdir'][path_file]["last_mod"] = time.ctime(os.path.getmtime(path_file))
        self.auto_remove(None)
        return




def main(first, second):
    """
    This is the main function"
    :param first:
    :param second:
    """
    tree1 = tree(first)
    print(tree1.dir)
    while True:
        time.sleep(3)
        tree1.update()
        print(tree1.dir)

if __name__ == "__main__":
    main("recursiv1", "recursiv2")
