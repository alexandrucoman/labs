#!/usr/bin/env python
# *-* coding: UTF-8 *-*

"""
Tuxy își dorește un sistem care să automatizeze instalării unui proiect
pe infrastructura din `TuxyLand`.

Acest proiect de automatizare va primi un fișier de configurare ce va
conține toate instrucțiunile necesare pentru pregătirea mediului ideal
în care va rula `TuxyApp`.

Un exemplu de fișier de configurare ar putea fi:



{
    "before_install": [
        {
            "download": {
                "source": "https://localhost/file",
                "destination": "/home/alex/script.sh",
            }
        },
    ],
    "install": [
        {
            "run_script": {
                # How many times to retry running the command.
                "attempts": 3,
                # Single bool, int, or list of allowed exit codes.
                "check_exit_code": True,
                # The command passed to the command runner.
                "command": "bash /home/alex/script.sh",
                # Set the current working directory
                "cwd": "/home/alex/",
                # Environment variables and their values that
                # will be set for the process.
                "env_variables": {"tuxy": "Tuxy Pinguinescu"},
                # Interval between execute attempts, in seconds.
                "retry_interval": 3,
                # Whether or not there should be a shell used to
                # execute this command.
                "shell": True,
            },
            # ...
        }
    ],
    "after_install": [
        {
            "reboot": {
                "method": "soft",
            }
        }
    ],

    "install_failed": [
        {
            "delete": {
                "method": "force",
                "path": "/home/alex"
            },
        },
        {
            "shutdown": {
                "method": "hard",
            },
        },
    ],
    "config": {
        "hostname": "TuxyNode-1",
        "users": {
            "acoman": {
                "full_name": "Alexandru Coman",
                "primary-group": "admin",
                "groups": ["users"],
                "expiredate": "2016-09-01",
                "password": ""
            },
            # ...
        },
        "write_files": {
            0: {
                "path": "/home/alex/test",
                "permissions": "0555",
                "encoding": "gzip",
                "content": "",
            },
            # ...
        },
    }
}

Trebuie să dezvoltați o aplicație care să primească un fișier de
configurare și să rezolve toate sarcinile precizate în acesta.

La sfârșit va trebui să ofere un fișier build.log care să descrie
toate lucrurile care s-au întâmplat.
"""
from __future__ import print_function
import json
import os
import argparse
import urllib2
import shutil
import time
import platform


def write_log(message_type, message):
    """ scriem mesajul in fisierul cu log-uri.
    prefixul este dat de tipul de mesaj dorit """

    if message_type == 'e':
        message = "EROARE :" + message
    elif message_type == 'o':
        message = "OK :" + message
    elif message_type == 'w':
        message = "WARNING :" + message
    elif message_type == 'f':
        message = "FINISH :" + message
    elif message_type == 'h':
        message = "HINT :" + message
    elif message_type == 'd':
        message = "DUMP INFO:" + str(message)

    message = message + ' \n'
    with open('build.log', "a") as file_data:
        file_data.write(message)


def parse_file(path):
    """ parsam fisierul de configurare. """

    try:
        with open(path) as data_file:
            data = json.load(data_file)
            write_log('o', "Am citit informatiile de configurare din " + path)
    except ValueError:
        write_log('e', "Informatiile din fisier nu sunt valide (" + path + ")")
        data = {'NU_EXISTA': True}

    except IOError:
        write_log('e', "Nu am gasit fisierul (" + path + ")")
        data = {'NU_EXISTA': True}
    return data


def parser_cli_arguments():
    """ parseaza argumentele primite la rularea programului """
    args = argparse.ArgumentParser()
    args.add_argument("-c", "--config_file",
                      help="Path to config file")
    args = args.parse_args()
    return args


def function_download(name, valori):
    """ downloadam de la o sursa la o destinatie """
    it_workerd = True
    source = valori.get('source', None)
    destination = valori.get('destination', None)
    if not source and not destination:
        it_workerd = False
        write_log('e', "Nu putem efectua " + name)
        write_log('d', valori)

    try:
        response = urllib2.urlopen(source)
        data = response.read()
        response.close()
        try:
            file_data = open(destination, 'w')
            file_data.write(data)
        except IOError as error:
            write_log('e', 'Nu am putut scrie la locatia ' + destination)
            write_log('d', error)
            it_workerd = False
    except IOError as error:
        write_log('e', 'Nu am putut descarca de la ' + source)
        write_log('d', error)
        it_workerd = False

    write_log('o', "Am descarcat de la <" + source + "> si am ")
    write_log('o', "salvat in <" + destination + ">")
    return it_workerd


def function_run_script(name, valori):
    """ setam variabilele de sistem, si rulam un script """
    attemts = valori['attempts']
    check_exit_code = valori['check_exit_code']

    if isinstance(check_exit_code, unicode):
        check_exit_code = bool(check_exit_code)
    if isinstance(check_exit_code, bool):
        if check_exit_code:
            check_exit_code = [0]
        else:
            check_exit_code = []
    env_variables = valori['env_variables']
    retry_interval = valori['retry_interval']
    shell = valori["shell"]
    command = valori["command"]

    cwd = valori['cwd']
    try:
        if cwd:
            os.chdir(cwd)
        write_log('o', "Am setat cwd :" + cwd)
    except OSError:
        write_log('e', "Nu am putut seta cwd :" + cwd)
        write_log('e', "Probabil nu exista")
        return False

    for name in env_variables:
        os.environ[name] = env_variables[name]

    write_log('o', "Am setat variabilele de sistem ")
    write_log('d', env_variables)

    it_workerd = False
    while attemts:
        attemts -= 1
        if shell:
            try:
                ret = os.system(command)
            except OSError as error:
                write_log('e', "Nu am putut rula scriptul !")
                write_log('e', "Commanda " + command)
                write_log('d', error)
        else:
            pass

        if not check_exit_code:
            it_workerd = True
            break

        if ret in check_exit_code:
            it_workerd = True
            write_log('o', "Am rulat scriptul :" + command)
            write_log('o', "Am avut exitcodul " + str(ret))
            break
        else:
            write_log('e', "Am rulat scriptul :" + command)
            write_log('e', "Am avut exitcodul " + str(ret))
            write_log('e', "Expected exitcode :")
            write_log('d', check_exit_code)

    time.sleep(int(retry_interval))

    return it_workerd


def function_delete(functie_name, valori):
    """ deletam ce se afla la path"""
    path_to_delete = valori.get("path", None)

    if not path_to_delete:
        write_log('e', "Nu ati dat un path")
        return False

    if not os.path.exists(path_to_delete):
        write_log('e', "Pathul nu este valid :" + path_to_delete)

    if os.path.isfile(path_to_delete):
        os.remove(path_to_delete)
        write_log('o', "Am eliminat fisierul :" + path_to_delete)

    elif os.path.isdir(path_to_delete):
        shutil.rmtree(path_to_delete)
        write_log('o', "Am eliminat directorul :" + path_to_delete)

    write_log('o', "Am executat cu succes " + functie_name)
    return True


def function_shutdown(valori):
    """ restartam calculator """

    command = "win32api call"
    if valori['method'] == "soft":
        command = "shutdown now"
    elif valori['method'] == "hard":
        command = "halt now"

    # sa nu dau restart din prostie
    command = "asdasd"

    platfm = platform.system()

    write_log('h', "Dam restart folosind :" + command)
    write_log('d', platfm)

    if platfm == "Linux":
        os.system(command)
    elif platfm == "Windows":
        import win32api
        win32api.InitiateSystemShutdown()
    return True


def create_accout_linux(name, p_grup, groups, exp_date, passwd):
    """ cream un cont pe linux"""
    write_log('w', "Trebuie sa adaugam un user cu :")
    write_log('d', name)
    write_log('d', p_grup)
    write_log('d', groups)
    write_log('d', exp_date)
    write_log('d', passwd)


def create_accout_windows(name, p_grup, groups, exp_date, passwd):
    """ cream un cont pe linux"""
    write_log('w', "Trebuie sa adaugam un user cu :")
    write_log('d', name)
    write_log('d', p_grup)
    write_log('d', groups)
    write_log('d', exp_date)
    write_log('d', passwd)


def function_account(valori):
    """ Cream conturi """
    platfm = platform.system()
    write_log('h', "Cream un user pe " + platfm)
    write_log('d', valori)

    name = valori["full_name"]
    p_grup = valori["primary_group"]
    groups = valori["users"]
    exp_date = valori["expiredate"]
    passwd = valori["password"]

    if platfm == "Linux":
        create_accout_linux(name, p_grup, groups, exp_date, passwd)
    elif platfm == "Windows":
        create_accout_windows(name, p_grup, groups, exp_date, passwd)

    return True


def apel_functie(functie_name, valori):
    """ apelam parsam valorile pentru functie si apelam functia """
    it_workerd = True

    if functie_name == 'download':
        it_workerd = function_download(functie_name, valori)
    elif functie_name == 'run_script':
        it_workerd = function_run_script(functie_name, valori)
    elif functie_name == 'delete':
        it_workerd = function_delete(functie_name, valori)
    elif functie_name == 'shutdown':
        it_workerd = function_shutdown(valori)
    elif functie_name == 'account':
        it_workerd = function_account(valori)

    return it_workerd


def do_set_of_instructions(faza, set_of_instructiuni):
    """ primeste o faza si face setul de instructiuni din acea faza"""
    write_log("h", "Rulam faza :" + faza)
    it_workerd = True

    # deoarece after_install, install, si after_install sunt liste cu un
    # element
    if isinstance(set_of_instructiuni, dict):
        set_of_instructiuni = [set_of_instructiuni]

    for instructiuni in set_of_instructiuni:
        for key in instructiuni:
            value = instructiuni[key]
            it_workerd = apel_functie(key, value)

            if not it_workerd:
                write_log("e", "Nu am putut efectua instructiunea " + key)
                write_log("d", value)
                break

    return it_workerd


def main():
    """ main function """
    args = parser_cli_arguments()
    data = parse_file(args.config_file)

    # delete log file
    log_file = open('build.log', 'w')
    log_file.write('')
    log_file.close()

    it_workerd = True
    if not data:
        write_log('w', "Am terminat programul!")
        it_workerd = False

    if 'config' in data.keys() and it_workerd:
        it_workerd = do_set_of_instructions('config', data['config'])

    if 'before_install' in data.keys() and it_workerd:
        it_workerd = do_set_of_instructions('before_install',
                                            data['before_install'])

    if 'install' in data.keys() and it_workerd:
        it_workerd = do_set_of_instructions('install',
                                            data['install'])

    if 'after_install' in data.keys() and it_workerd:
        it_workerd = do_set_of_instructions('after_install',
                                            data['after_install'])

    if 'install_failed' in data.keys() and not it_workerd:
        do_set_of_instructions("install_failed", data['install_failed'])


if __name__ == "__main__":
    main()
