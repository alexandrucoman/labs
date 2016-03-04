#  !/usr/bin/env python
#   *-* coding: UTF-8 *-*

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
#   pylint: disable=import-error

from __future__ import print_function

#   Notes: Pentru a instala bibleoteca yaml trebuie să rulați
#          următoarea comandă: pip install pyaml

import urllib
import subprocess
import os
import yaml


def after_install(config):
    """ after install """
    for command in config['after_install']:
        if 'reboot' in command.keys():
            #  """ Perform an hard / soft reboot """
            method = command['reboot']['method']
            if method == 'soft':
                bash_command = "shutdown -P 10"
            elif method == 'hard':
                bash_command = "shutdown -H 10"
            subprocess.Popen(bash_command.split())


def before_install(config):
    """ before install """
    for command in config['before_install']:
        if 'download' in command.keys():
            #  """ download an file from source to destination """
            destination = command['download']['destination']
            source = command['download']['source']
            download = urllib.URLopener()
            download.retrieve(source, destination)


def configuration(config):
    """ configuration """
    for command in config['config']:
        for do_this in command.split():
            if do_this == 'hostname':
                #  """ change hostname """
                bash_command = []
                bash_command.append("hostname")
                bash_command.append(config['config'][do_this])
                #  subprocess.Popen(" ".join(bash_command))
            if do_this == 'users':
                #  """ add users """
                for user in config['config'][do_this]:
                    user = config['config'][do_this]
                    add_user = []
                    add_user.append("useradd")
                    add_user.append(user.keys()[0])
                    #  subprocess.Popen(" ".join(add_user))
                    for commands in user:
                        #  print(user[commands]['expiredate'])
                        if 'expiredate' in user[commands]:
                            expire_date = []
                            expire_date.append("chage -E")
                            expire_date.append(user[commands]['expiredate'])
                            #  subprocess.Popen(" ".join(expire_date))
                        if 'full_name' in user[commands]:
                            full_name = []
                            full_name.append("chfn -f")
                            full_name.append(user[commands]['full_name'])
                            #  subprocess.Popen(" ".join(full_name))
                        if 'groups' in user[commands]:
                            #  """ add user to group
                            #     TO DO: check if group exist
                            #  """
                            groups = []
                            groups.append("useradd -G")
                            for name in user[commands]['groups']:
                                groups.append(name)
                            groups.append(user.keys()[0])
                            #  subprocess.Popen(" ".join(groups))
                        if 'password' in user[commands]:
                            #  """ change passwd  fo user
                            #     TO DO: think again
                            #  """
                            change_passwd = []
                            change_passwd.append("passwd")
                            change_passwd.append(user.keys()[0])
                            #  change_passwd.append(user[commands]['passwd'])
                            #  subprocess.Popen(" ".join(change_passwd))
                        if 'primary-group' in user[commands]:
                            #  """ add user to an primary group.
                            #     TO DO: check curent OS for sudoers grup name
                            #            check to see if group exist
                            #  """
                            primary_group = []
                            primary_group.append("usermod -g")
                            if user[commands]['primary-group'] == 'admin':
                                primary_group.append("sudo")
                            else:
                                gr_name = user[commands]['primary-group']
                                primary_group.append(gr_name)
                            primary_group.append(user.keys()[0])
                            #  subprocess.Popen(" ".join(primary_group))
            if do_this == 'write_files':
                #   """ write files
                #     TO DO: check encoding stuff
                #  """
                for filen in config['config'][do_this]:
                    filen = config['config'][do_this]
                    for index in filen:
                        if 'content' in filen[index]:
                            content = filen[index]['content']
                        if 'encoding' in filen[index]:
                            encoding = filen[index]['encoding']
                        if 'path' in filen[index]:
                            path = filen[index]['path']
                        if 'permissions' == filen[index]:
                            permissions = filen[index]['permissions']
                        print(encoding, content, path, permissions)
                        fisier = []
                        fisier.append(path)
                        fisier.append(content)
                        fisier = "/".join(fisier)
                        if os.path.exists(path):
                            fis = open(content, 'w')
                            fis.write(content)
                        else:
                            bash_command = []
                            bash_command.append = "mkdir"
                            bash_command.append = path
                            #  subprocess.Popen(" ".join(bash_command))
                            fis = open(path, 'w')
                            fis.write(content)
                        change_permissions = []
                        change_permissions.append("chmod")
                        change_permissions.append(permissions)
                        #  subprocess.Popen(" ".join(change_permissions))


def install(config):
    """ install """
    for command in config['install']:
        if 'run_script' in command.keys():
            #  """ run script with those options
            #     TO DO: check to see what options were given and make install
            #  """

            attempts = command['run_script']['attempts']
            check_exit_code = command['run_script']['check_exit_code']
            run_command = command['run_script']['command']
            run_wd = command['run_script']['cwd']
            env_variables = command['run_script']['env_variables']
            retry_interval = command['run_script']['retry_interval']
            shell = command['run_script']['shell']
            print(attempts, check_exit_code, run_command,
                  run_wd, env_variables, retry_interval, shell)


def install_failed(config):
    """ install_failed """
    for command in config['install_failed']:
        if 'delete' in command.keys():
            #  Delete files from path """
            method = command['delete']['method']
            path = command['delete']['path']
            if method == 'force':
                bash_command = []
                bash_command.append("rm -rf")
                bash_command.append(path)
            else:
                bash_command = []
                bash_command.append("rm -f")
                bash_command.append(path)
            #  subprocess.Popen(bash_command.split())

        if 'shutdown' in command.keys():
            #  Perform an hard / soft reboot
            if 'method' in command['shutdown']:
                method = command['shutdown']['method']
                if method == 'soft':
                    bash_command = "shutdown -P 10"
                elif method == 'hard':
                    bash_command = "shutdown -H 10"
                #  subprocess.Popen(bash_command.split())


def main(path):
    """Citim fisierul de configurare."""
    try:
        with open(path, "r") as fisier:
            config = yaml.load(fisier)
    except (IOError, ValueError):
        print("Nu am putut citi datele din fisierul de configurare.")
        return
    #  print(yaml.dump(config,default_flow_style=False))

    install_failed(config)

    # if 'config' in config.keys():
    #     configuration(config)
    # if 'before_install' in config.keys():
    #     before_install(config)
    # if 'install' in config.keys():
    #     done=install(config)
    # if done == False and 'install_failed' in config.keys():
    #     install_failed(config)
    # if done == True and 'after_install' in config.keys():
    #     after_install(config)


if __name__ == "__main__":
    """ To DO: install
               build log
    """
    main("../../../date_intrare/tuxy.config")
