#! /usr/bin/python2.7
from __future__ import print_function
import os
import shutil
import sys
import time

class PathTree:

    def __init__(self, name):
        self.name = name
        self.children = []

    def get_name(self):
        return self.name

    def add_file(self, path):
        path_components = path.split(os.sep)
        
        node_pointer = self
        for path_way in path_components:
            matches = [child for child in node_pointer.children \
                                if child.get_name() == path_way]
            if len(matches) == 0:
                node_pointer.children.append(PathTree(path_way))
                node_pointer = node_pointer.children[-1] 
            else:
                node_pointer = matches[0]

    def contains(self, rel_path):
        node_pointer = self
        for path_way in rel_path.split(os.sep):
           matches = [child for child in node_pointer.children \
                                if child.get_name() == path_way]
           if len(matches) == 0:
               return False
           node_pointer = matches[0]

        return True

    def delete(self, rel_path):
        node_pointer = self
        path_components = rel_path.split(os.sep)
        desired_name = path_components[-1]
        for idx, path_way in enumerate(path_components):
            if idx == len(path_components) - 1:
                desired_name = path_components[-1]
            else:
                desired_name = path_way
                      
            matches = [child for child in node_pointer.children \
                                if child.get_name() == desired_name]
            
            if len(matches) > 0 and idx == len(path_components) - 1:
                node_pointer.children.remove(matches[0])
                break
            elif len(matches) == 0:
                return
            else:
                node_pointer = matches[0]

def sync_dirs(ch_dir1, ch_dir2):
    root1 = ch_dir1.get_name()
    root2 = ch_dir2.get_name()

    for dirpath, dirnames, filenames in os.walk(root1):
        rel_path = dirpath.split(root1, 1)[1]
        for filename in filenames:
            file_path = dirpath + os.sep + filename
            twin_path = root2 + rel_path + os.sep + filename

            if (not os.path.exists(twin_path) and 
                    ch_dir2.contains(rel_path + os.sep + filename)):
                # Synced from 2 to 1. Then deleted from 2.
                os.remove(file_path)
                ch_dir1.delete(rel_path + os.sep + filename)
                ch_dir2.delete(rel_path + os.sep + filename)
            elif not os.path.exists(twin_path):
                dirs = rel_path.split(os.sep)
                for idx, parent_dir in enumerate(dirs):
                    parent_dir_path = root2 + os.sep.join(dirs[:idx + 1:])
                    if not os.path.exists(parent_dir_path):
                        os.mkdir(parent_dir_path)
                shutil.copy(file_path, twin_path)
                ch_dir2.add_file(rel_path + os.sep + filename)

            # Sync empty directories as well.
            for dirname in dirnames:
                twin_path = root2 + os.sep + rel_path + os.sep + dirname
                if (len(os.listdir(dirpath + os.sep + dirname)) == 0 and 
                        ch_dir2.contains(rel_path + os.sep + dirname)):
                    os.rmdir(dirpath + os.sep + dirname)
                    ch_dir1.delete(rel_path + os.sep + dirname)
                    ch_dir2.delete(rel_path + os.sep + dirname)
                elif (len(os.listdir(dirpath + os.sep + dirname)) == 0
                    and not os.path.exists(twin_path)):
                    os.mkdir(twin_path)
                    ch_dir2.add_file(rel_path + os.sep + dirname) 

if __name__ == "__main__":
    
    if len(sys.argv) != 3:
        print("Usage: sync_dirs dir1 dir2")
        sys.exit(1)
    
    if sys.argv[1][-1] == os.sep:
        ch_dir1 = PathTree(sys.argv[1][:-1:])
    else:
        ch_dir1 = PathTree(sys.argv[1])

    if sys.argv[2][-1] == os.sep:
        ch_dir2 = PathTree(sys.argv[2][:-1:])
    else:
        ch_dir2 = PathTree(sys.argv[2])

    for dirpath, dirnames, filenames in os.walk(ch_dir1.get_name()):
        for filename in filenames:
            ch_dir1.add_file(dirpath + os.sep + filename)
        for dirname in dirnames:
            ch_dir1.add_file(dirpath + os.sep + dirname)

    for dirpath, dirnames, filenames in os.walk(ch_dir2.get_name()):
        for filename in filenames:
            ch_dir2.add_file(dirpath + os.sep + filename)
        for dirname in dirnames:
            ch_dir2.add_file(dirpath + os.sep + dirname)

    print("Press Ctrl + C to stop syncing.")
    while True:
        # Sync at 2 seconds.
        time.sleep(2)
        sync_dirs(ch_dir1, ch_dir2)
        sync_dirs(ch_dir2, ch_dir1)

