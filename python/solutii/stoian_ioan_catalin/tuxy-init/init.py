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

import yaml
import requests
import subprocess
import os
import sys
import shutil

class TuxyApp(object):
    def __init__(self, config):
        self.config = config

    def beforeinstall(self):
        url = self.config['before_install'][0]['download']['source']
        destination = self.config['before_install'][0]['download']['destination']
        req = requests.get(url)
        open("tmp", 'a').close()
        path = " "
        file = open("tmp", 'wb')
        for chunk in req.iter_content(100000):
            file.write(chunk)
        file.close()
        folders = destination.split("/")
        if not os.path.exists(destination):
            for folder in folders[:-1]:
                print(folder)
                path = os.path.join(path, folder)
                os.mkdir(path)
        open(folders[-1], 'a')
        shutil.copy("tmp", destination)
        os.remove("tmp")

    def install(self):
        print(self.config['install'])
        cwd = self.config['install'][0]['run_script']['cwd']
        retry_interval = self.config['install'][0]['run_script']['retry_interval']
        command = self.config['install'][0]['run_script']['command']
        attempts = self.config['install'][0]['run_script']['attempts']
        env = self.config['install'][0]['run_script']['env_variables']
        shell = self.config['install'][0]['run_script']['shell']
        print(os.getcwd())

    def run(self):
        self.beforeinstall()
        self.install()

def main(path):
    """Citim fisierul de configurare."""
    """
    try:
        with open(path, "r") as fisier:
            config = yaml.load(fisier)
            app = TuxyApp(config)
            app.run()
    except (IOError, ValueError):
        print("Nu am putut citi datele din fisierul de configurare.")
        return
    """
    with open(path, "r") as fisier:
            config = yaml.load(fisier)
            app = TuxyApp(config)
            app.run()



if __name__ == "__main__":
    main("../../../date_intrare/tuxy.config")

