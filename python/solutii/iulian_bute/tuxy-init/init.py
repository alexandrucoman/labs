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


def f_download(conf):
    ''' descarca un fisier intr-o locatie data '''
    print "download: ", conf
    print
    os.system("".join(["wget -O ", conf['destination'], " ", conf['source']]))
    

def f_run_script(conf):
    ''' ruleaza un script '''
    print "run script: ", conf
    print
    return 0


def f_delete(conf):
    ''' sterge fisiere '''
    print "delete: ", conf
    print
    try:
        os.system("".join(["rm -rf ", conf['path']]))
    except:
        print "Nu putem sterge"


def f_shutdown(conf):
    ''' inchide sistemul '''
    print "shudown: ", conf
    print
    if conf['method'] == 'hard':
        os.system("shutdown -h now")
    else:
        os.system("shutdown -h +5 Inchidem sistemul")


def f_reboot(conf):
    ''' reporneste sistemul '''
    print "reboot: ", conf
    print
    if conf['method'] == 'hard':
        os.system("shutdown -r -f now")
    else:
        os.system("shutdown -r now")


def stage_config(conf):
    ''' Ruleaza scriptul de configurare '''
    print " -> config: ", type(conf), len(conf), '\n\n', conf
    print


def stage_before_install(conf):
    ''' Ruleaza scriptul de pregatire a instalarii '''
    print " -> bef install: \n"
    for action in conf:
        for action_name in action:
            if action_name == 'download':
                f_download(action['download'])
            elif action_name == 'run_script':
                f_run_script(action['run_script'])
            elif action_name == 'delete':
                f_delete(action['delete'])
            elif action_name == 'shutdown':
                f_shutdown(action['shutdown'])
            elif action_name == 'reboot':
                f_reboot(action['reboot'])


def stage_install(conf):
    ''' Ruleaza scriptul de instalare '''
    print " -> install: \n"
    succes_state = 0
    for action in conf:
        for action_name in action:
            if action_name == 'download':
                f_download(action['download'])
            elif action_name == 'run_script':
                succes_state = f_run_script(action['run_script'])
            elif action_name == 'delete':
                f_delete(action['delete'])
            elif action_name == 'shutdown':
                f_shutdown(action['shutdown'])
            elif action_name == 'reboot':
                f_reboot(action['reboot'])
    return succes_state


def stage_install_failed(conf):
    ''' In caz ca nu se poate face instalarea se executa acest script '''
    print " -> inst failed: \n"
    for action in conf:
        for action_name in action:
            if action_name == 'download':
                f_download(action['download'])
            elif action_name == 'run_script':
                f_run_script(action['run_script'])
            elif action_name == 'delete':
                f_delete(action['delete'])
            elif action_name == 'shutdown':
                f_shutdown(action['shutdown'])
            elif action_name == 'reboot':
                f_reboot(action['reboot'])


def stage_after_install(conf):
    ''' Scriptul de dupa instalare '''
    print " -> after inst: \n"
    for action in conf:
        for action_name in action:
            if action_name == 'download':
                f_download(action['download'])
            elif action_name == 'run_script':
                f_run_script(action['run_script'])
            elif action_name == 'delete':
                f_delete(action['delete'])
            elif action_name == 'shutdown':
                f_shutdown(action['shutdown'])
            elif action_name == 'reboot':
                f_reboot(action['reboot'])


def main(path):
    """Citim fisierul de configurare."""
    try:
        with open(path, "r") as fisier:
            config = yaml.load(fisier)
    except (IOError, ValueError):
        print "Nu am putut citi datele din fisierul de configurare."
        return

    succesfull = 1
    stage_config(config['config'])
    stage_before_install(config['before_install'])
    if stage_install(config['install']) is succesfull:
        stage_after_install(config['after_install'])
    else:
        stage_install_failed(config['install_failed'])

if __name__ == "__main__":
    main("tuxy.config")
