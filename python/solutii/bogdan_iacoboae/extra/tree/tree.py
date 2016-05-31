import os
import tkFileDialog


def list_files(locatie):
    for root, dirs, files in os.walk(locatie):
        nivel = root.replace(locatie, '').count(os.sep)
        spatiu = '-' * 4 * (nivel)
        print '[DIR ]|%s%s' % (spatiu,os.path.basename(root))
        spatiu2 = '-' * 4 * (nivel + 1)
        for fisier in files:
            print '[FILE]|%s%s' % (spatiu2,fisier)

if __name__ == "__main__":
    foldername= tkFileDialog.askdirectory()
    list_files(foldername)