import os

def list_files(locatie):
    for root, dirs, files in os.walk(locatie):
        nivel = root.replace(locatie, '').count(os.sep)
        spatiu = '-' * 4 * (nivel)
        print '[DIR ]|%s%s' % (spatiu,os.path.basename(root))
        spatiu2 = '-' * 4 * (nivel + 1)
        for fisier in files:
            print '[FILE]|%s%s' % (spatiu2,fisier)

if __name__ == "__main__":
    list_files("D:\FACULTATE\CloudBase\labs\python\solutii\/bogdan_iacoboae\/extra")