#!/usr/bin/env python
# *-* coding: UTF-8 *-*
from __future__ import print_function
import urllib
import shutil
import os
import json
from pprint import pprint

def analiza_comanda(comanda,fila):
    for it_comand in comanda:
        for it_it_comanda in it_comand:
            if it_it_comanda == "download":
                info_down=it_comand[it_it_comanda]
                url=info_down['source']
                print (url)
                f = open('/home/alex/script.sh','wb')
                f.write(urllib.urlopen(url).read())
                f.close()
                fila.write("Descarcat de la url ")
            if it_it_comanda == "reboot":
                os.system("shutdown /r /t %s " % time)
                fila.write("Restart ")
            if it_it_comanda == "install_failed":
                fila.write("Failed ")
                for it_it_it_comanda in it_it_comanda:
                    if it_it_it_comanda == "delete":
                        filename="/home/alex"
                        fila.write("Delete ")
                        if os.path.exists(filename):
                            if os.path.isfile(filename):
                                os.remove(filename)
                            if os.path.isdir(filename):
                                shutil.rmtree(filename)
                    if it_it_it_comanda == "shutdown":
                        os.system("shutdown /t %s " % time)
                        fila.write("Shutdown")
            

def main():
    with open('data.json') as data_file:    
        data = json.load(data_file)
        fisier = open("icao_intrare", "w+")
    fisier.close()
    for item in data:
        analiza_comanda(data[item],fisier)
        break

if __name__ == "__main__":
    main()

