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

# from __future__ import print_function

# Notes: Pentru a instala bibleoteca yaml trebuie să rulați
#        următoarea comandă: pip install pyaml

import yaml
import os


def f_download(conf, log):
    ''' descarca un fisier intr-o locatie data '''
    destinatie = os.path.split(conf['destination'])
    dest = destinatie[0]
    if not os.path.exists(dest):
        os.makedirs(dest)
    log.write("".join(["created path for downloading ", conf['source'], "\n"]))
    os.system("".join(["wget -O ", conf['destination'], " ", conf['source']]))
    log.write("download done\n")


def f_run_script(conf, log):
    ''' ruleaza un script '''
    log.write("".join(["start running script ", conf['command'], "\n"]))
    return 1


def f_delete(conf, log):
    ''' sterge fisiere '''
    log.write("".join(["trying to delete ", conf['path'], "\n"]))
    try:
        os.system("".join(["rm -rf ", conf['path'], "\n"]))
    except IOError:
        log.write("".join(["Nu putem sterge ", conf['path'], "\n"]))


def f_shutdown(conf, log):
    ''' inchide sistemul '''
    log.write("shutting down..\n")
    if conf['method'] == 'hard':
        os.system("shutdown -h now")
    else:
        os.system("shutdown -h +5 Inchidem sistemul")


def f_reboot(conf, log):
    ''' reporneste sistemul '''
    log.write("rebooting..\n")
    if conf['method'] == 'hard':
        os.system("shutdown -r -f now")
    else:
        os.system("shutdown -r now")


def stage_config(conf, log):
    ''' Ruleaza scriptul de configurare '''
    log.write("".join(["start configuring to ", conf['hostname'], "\n"]))
    os.system("".join(["hostname ", conf['hostname']]))
    for user in conf["users"]:
        n_usr = "".join(["useradd -e ", conf['users'][user]['expiredate']])
        n_usr = "".join([n_usr, " -G ", conf['users'][user]["groups"][0]])
        n_usr = "".join([n_usr, " -g "])
        n_usr = "".join([n_usr, conf['users'][user]["primary-group"]])
        n_usr = "".join([n_usr, " -p ", conf['users'][user]['password']])
        n_usr = "".join([n_usr, " --comment "])
        n_usr = "".join([n_usr, conf['users'][user]['full_name']])
        n_usr = "".join([n_usr, " ", user])
        os.system(n_usr)
        log.write("".join(["created user ", user, '\n']))


def stage_before_install(conf, log):
    ''' Ruleaza scriptul de pregatire a instalarii '''
    print " -> before install: \n"
    for action in conf:
        for action_name in action:
            if action_name == 'download':
                f_download(action['download'], log)
            elif action_name == 'run_script':
                f_run_script(action['run_script'], log)
            elif action_name == 'delete':
                f_delete(action['delete'], log)
            elif action_name == 'shutdown':
                f_shutdown(action['shutdown'], log)
            elif action_name == 'reboot':
                f_reboot(action['reboot'], log)


def stage_install(conf, log):
    ''' Ruleaza scriptul de instalare '''
    print " -> install: \n"
    succes_state = 0
    for action in conf:
        for action_name in action:
            if action_name == 'download':
                f_download(action['download'], log)
            elif action_name == 'run_script':
                succes_state = f_run_script(action['run_script'], log)
            elif action_name == 'delete':
                f_delete(action['delete'], log)
            elif action_name == 'shutdown':
                f_shutdown(action['shutdown'], log)
            elif action_name == 'reboot':
                f_reboot(action['reboot'], log)
    return succes_state


def stage_install_failed(conf, log):
    ''' In caz ca nu se poate face instalarea se executa acest script '''
    print " -> inst failed: \n"
    for action in conf:
        for action_name in action:
            if action_name == 'download':
                f_download(action['download'], log)
            elif action_name == 'run_script':
                f_run_script(action['run_script'], log)
            elif action_name == 'delete':
                f_delete(action['delete'], log)
            elif action_name == 'shutdown':
                f_shutdown(action['shutdown'], log)
            elif action_name == 'reboot':
                f_reboot(action['reboot'], log)


def stage_after_install(conf, log):
    ''' Scriptul de dupa instalare '''
    print " -> after inst: \n"
    for action in conf:
        for action_name in action:
            if action_name == 'download':
                f_download(action['download'], log)
            elif action_name == 'run_script':
                f_run_script(action['run_script'], log)
            elif action_name == 'delete':
                f_delete(action['delete'], log)
            elif action_name == 'shutdown':
                f_shutdown(action['shutdown'], log)
            elif action_name == 'reboot':
                f_reboot(action['reboot'], log)


def main(path):
    """Citim fisierul de configurare."""
    try:
        with open(path, "r") as fisier:
            config = yaml.load(fisier)
    except (IOError, ValueError):
        print "Nu am putut citi datele din fisierul de configurare."
        return

    log = open("build.log", "w")
    succesfull = 1
    log.write("start!\n")
    log.write("configuring..\n")
    stage_config(config['config'], log)
    log.write("preparing install..\n")
    stage_before_install(config['before_install'], log)
    if stage_install(config['install'], log) is succesfull:
        log.write("install complete. post-install script running..\n")
        stage_after_install(config['after_install'], log)
    else:
        log.write("install failed.\n")
        stage_install_failed(config['install_failed'], log)

if __name__ == "__main__":
    main("../../../date_intrare/tuxy2.config")
