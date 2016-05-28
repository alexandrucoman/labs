#!/usr/bin/env python
# *-* coding: UTF-8 *-*

"""
Tuxy își dorește un sistem care să automatizeze instalării unui proiect
pe infrastructura din `TuxyLand`.
Acest proiect de automatizare va primi un fișier de configurare ce va
conține toate instrucțiunile necesare pentru pregătirea mediului ideal
în care va rula `TuxyApp`.
Un exemplu de fișier de configurare ar putea fi: tuxy.config din
directorul python/date_intrare.
Trebuie să dezvoltați o aplicație care să primească un fișier de
configurare și să rezolve toate sarcinile precizate în acesta.
La sfârșit va trebui să ofere un fișier build.log care să descrie
toate lucrurile care s-au întâmplat.
"""
# pylint: disable=import-error

from __future__ import print_function

# Notes: Pentru a instala bibleoteca yaml trebuie să rulați
#        următoarea comandă: pip install pyaml

# INCOMPLETA


import yaml
import os

# definirea sarcinilor


def reboot(method):
    if method == 'soft':
        print("System is soft rebooting...")
        os.system('shutdown -r now')

def download(url, dest):
    try:
        file_name = url.split('/')[-1]
        u = urllib2.urlopen(url)
        dest_file = open(dest, 'wb')
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        print ("Downloading: %s Bytes: %s") % (file_name, file_size)

        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break
            file_size_dl += len(buffer)
            dest_file.write(buffer)
            status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
            status = status + chr(8)*(len(status)+1)
            print (status)
        dest_file.close()
    except IOError as err:
        print("Cannot create dest file because of: ", err)


# Functii pentru configurarea sistemului

def change_host_name(new_hostname):
    os.system(''.join(['hostname ',new_hostname]))

def create_user(new_user_name, attrs):
        for i in attrs:
            if i == "full_name":
                attrs["--comment "] = attrs.pop(i)
            elif i == "expiredate":
                attrs[i] = attrs.pop(i)
            elif i == "groups":
                attrs["-G "] = " ".join(groups)
                del attrs[i]
            elif i == "password":
                attrs["-p "] = attrs.pop(i)
            elif i == "primary-group":
                attrs["-g "] = attrs.pop(i)
            else
                print("dunno attribute")

        command_attrs = ' '.join(['{} {}'.format(key,val) for key,val in attrs.iteritems()])
        command = ' '.join(["-useradd", command_attrs])
        os.system(command)


def write_file(file_attrs):
   new_file = open(file_attrs['path'],'w+')
   new_file.write(file_attrs['content'])
   os.chmod(file_attrs['path'], int(value['permissions']))

   # new_file_enc = os.system("file -bi ")
   # os.system("iconv -f %s -t %s" % ( filename))

'''
def run_script():


def delete():
'''

def apply_commands_from_categ(categ):
    for command in categ:
        if command == 'download':
            download(command['source'], command['destination'])
        elif command == 'reboot':
            reboot(command['method'])
        else
            print("dunno command")
        # DE COMPLETAT

def shutdown(method):
    if method == 'hard':
        print("System is hard shutting down...")
        os.system('shutdown -h now')
    else:
        print("dunno what method is")


def main(path):
    """Citim fisierul de configurare."""
    try:
        with open(path, "r") as fisier:
            config = yaml.load(fisier)
    except (IOError, ValueError):
        print("Nu am putut citi datele din fisierul de configurare.")
        return
    for i in config:
    	print(i)
    print("\n")		

if __name__ == "__main__":
    main("../../../date_intrare/tuxy.config")
