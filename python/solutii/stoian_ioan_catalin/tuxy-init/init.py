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
import shutil
import platform
import time
import sys


class TuxyApp(object):
    def __init__(self, config):
        self.config = config
        if not os.path.exists("build.log"):
            open("build.log", "a").close()

    @staticmethod
    def buildlog(text):
        """
        Aceasta functie scrie in log.
        :param text:
        :return:
        """
        lista = ['[', time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()), '] ', text, '\n']
        with open("build.log", "a") as myfile:
            myfile.write(''.join(lista))
        myfile.close()

    def configuration(self):
        """
        Aceasta functie configureaza sistemul.
        :return:
        """
        hostname = self.config['config']['hostname']
        users = self.config['config']['users']
        files = self.config['config']['write_files']
        subprocess.Popen(['hostname', hostname])
        self.buildlog(''.join(['S-a schimbat numele la hostname in ', hostname]))
        for name in users:
            listcommand = ["useradd", name,
                           '-e', users[name]['expiredate'],
                           '-p', users[name]['password'],
                           '-G', users[name]['primary-group']]
            subprocess.Popen(listcommand)
            self.buildlog(''.join(['S-a creat user-ul ', name]))
        for file in files:
            with open(files[file]['path'], "a") as myfile:
                myfile.write(files[file]['content'])
            subprocess.call(['chmod', files[file]['permission'], files[file]['path']])

    def beforeinstall(self):
        """
        Aceasta functie pregateste mediul pentru ca aplicatia sa fie instalata.
        :return:
        """
        url = self.config['before_install'][0]['download']['source']
        destination = self.config['before_install'][0]['download']['destination']
        try:
            req = requests.get(url)
        except IOError:
            self.buildlog(''.join(["Nu s-a putut descarca fisierul sursa de la adresa ", url]))
            sys.exit(0)

        open("tmp", 'a').close()
        self.buildlog("Se creaza un fisier temporar pentru a retine informatiile descarcate.")
        file = open("tmp", 'wb')
        for chunk in req.iter_content(100000):
            file.write(chunk)
        file.close()
        folders = destination.split("/")
        last = folders[-1]
        path = folders[1]
        if not os.path.exists(path):
            os.mkdir(folders[1])
            self.buildlog(''.join(["Se creaza path-ul ", destination]))
        if not os.path.exists(destination):
            for folder in folders[2:]:
                if last != folder:
                    path = os.path.join(path, folder)
                    if not os.path.exists(path):
                        os.mkdir(path)
                else:
                    shutil.copyfile("tmp", os.path.join(path, folder))
        self.buildlog("Descarcarea script-ului a fost finalizata cu succes.")
        os.remove("tmp")
        self.buildlog("Fisierul temporar a fost sters.")

    def install(self):
        """
        Aceasta functie se ocupa cu instalat-ul de aplicatie.
        :return:
        """
        cwd = self.config['install'][0]['run_script']['cwd']
        retry_interval = self.config['install'][0]['run_script']['retry_interval']
        command = self.config['install'][0]['run_script']['command']
        attempts = self.config['install'][0]['run_script']['attempts']
        env = self.config['install'][0]['run_script']['env_variables']
        shell = self.config['install'][0]['run_script']['shell']
        os.chdir(cwd)
        attempts = int(attempts)
        while attempts > 0:
            try:
                d = dict(os.environ)
                for var in env:
                    d[var] = env[var]
                subprocess.Popen(command.split(" "), shell=shell, env=d)
                break
            except(IOError, ValueError):
                sec = int(retry_interval)
                time.sleep(sec)
                attempts -= 1
                mlist = [
                    "EROARE: Comanda nu a putut fii executata. Se reincearca executarea script-ului. Incercari ramase",
                    attempts
                ]
                mesaj = ''.join(mlist)
                self.buildlog(mesaj)
        if attempts == 0:
            self.installfaild()

    def afterinstall(self):
        """
        Aceasta functie pregateste mediul dupa instalare.
        :return:
        """
        print(self.config['after_install'])
        method = self.config['after_install'][0]['reboot']['method']
        comanda = ""
        if platform.system() == "Windows":
            if method == "soft":
                comanda = "shutdown -r"
            else:
                comanda = "shutdown -r -f"
        elif platform.system() == "Linux":
            if method == "soft":
                comanda = "reboot"
            else:
                comanda = "reboot -f"
        self.buildlog("Instalare efectuata cu success.")
        self.buildlog("Sistemul se pregateste sa fie restartat.")
        subprocess.Popen(comanda.split(" "))

    def installfaild(self):
        """
        Aceasta functie trateaza cazul in care instalarea nu a putut fi efectuata.
        :return:
        """
        method = self.config['install_failed'][0]['shutdown']['method']
        del_path = self.config['install_failed']['delete']['path']
        self.buildlog("Instalare a fost abandonata. Se sterg fisierele descarcate.")
        if os.path.isdir(del_path):
            shutil.rmtree(del_path)
        elif os.path.isfile(del_path):
            os.remove(del_path)
        comanda = ""
        if platform.system() == "Windows":
            if method == "soft":
                comanda = "shutdown -r"
            else:
                comanda = "shutdown -r -f"
        elif platform.system() == "Linux":
            if method == "soft":
                comanda = "reboot"
            else:
                comanda = "reboot -f"
        self.buildlog("Sistemul se pregateste sa fie restartat.")
        subprocess.Popen(comanda.split(" "))

    def run(self):
        """
        Aceasta este functia care trebuie apelata atunci cand se creaza un obiect de aceasta clasa.
        :return:
        """
        self.buildlog("Se pregateste mediul de instalare")
        self.beforeinstall()
        self.buildlog("Se configureaza sistemul.")
        self.configuration()
        self.buildlog("Se instaleaza...")
        self.install()
        self.buildlog("Instalare efectuata cu success, se pregateste sistemul pentru restartare")
        self.afterinstall()


def main(path):
    """
    Citim fisierul de configurare
    :param path:
    :return:
    """
    try:
        with open(path, "r") as fisier:
            config = yaml.load(fisier)
            app = TuxyApp(config)
            app.run()
    except (IOError, ValueError):
        print("Nu am putut citi datele din fisierul de configurare.")
        return


if __name__ == "__main__":
    main("../../../date_intrare/tuxy.config")
