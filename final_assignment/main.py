#!/usr/bin/env python
# *-* coding: UTF-8 *-*

"""
Tuxy își dorește un sistem care să automatizeze instalării unui proiect
pe infrastructura din `TuxyLand`.

Acest proiect de automatizare va primi un fișier de configurare ce va
conține toate instrucțiunile necesare pentru pregătirea mediului ideal
în care va rula `TuxyApp`.

Un exemplu de fișier de configurare ar putea fi:

config.cfg

Trebuie să dezvoltați o aplicație care să primească un fișier de
configurare și să rezolve toate sarcinile precizate în acesta.

La sfârșit va trebui să ofere un fișier build.log care să descrie
toate lucrurile care s-au întâmplat.
"""
from __future__ import print_function
import ast

instructions = ["before_install", "install", "after_install", "install_failed", "config"]
mesaj1 = "\n\nIn timpul executarii scriptului:"
mesaj2 = ["\nA aperut o eroare!", "\nTotul a fost ok!"]

def citeste(fisier):
    """
        Funcita va primi la intrare fisierul cfg, il va citi si pune intr-un dicitionar.
    """
    try:
        with open(fisier, 'r') as fin:
            str = fin.read()
            try:
                dict = ast.literal_eval(str)
            except:
                return
        fin.close()
        if verifica(dict) == None:
            print("Configuratia contine si alte instructiuni.")
        return dict
    except IOError:
        print("Nu am putut obține configuratia.")
        return

def verifica(cfg):
    """
        Verifica daca fiserul primit este o configuratie OK
    """
    for key in cfg.keys():
        if key not in instructions:
            return
    return 1

def write_in_log(message):
    with open("build.log", "a") as fout:
        fout.write(message)


def exec_before_install(comands):
    """
        Are grija de comenzile dinainte de instalare
    """
    # presupun ca pot exista mai multe obiecte dupa tiparul lui download cu diverse nume
    for download in comands[0]:
        download_name = download
        download = comands[0].get(download)
        source = download.get("source")
        destination = download.get("destination")

        # Executa scriptul de dwonload pentru fiecare instructiune de tip download

        # In urma executarii scriptul va returna 0 sau 1:
        # 1 daca executia a avut loc cu succes
        # 0 daca executia nu a avut succes
        # voi presupune ca nu exista erori si toate scripturile se executa corect
        returnvalue = 1
        write_in_log(" ".join((mesaj1,  download_name, "(", source, ',', destination, ")", mesaj2[returnvalue])))

def exec_install(comands):
    """
    Are grija de comenizle din timpul instalarii
    """
    for run_script in comands[0]:
        run_script_name = run_script
        run_script = comands[0].get(run_script)
        attempts = run_script.get("attempts")
        check_exit_code = run_script.get("check_exit_code")
        command = run_script.get("command")
        cwd = run_script.get("cwd")
        env_variables = run_script.get("env_variables")
        retry_interval = run_script.get("retry_interval")
        shell = run_script.get("shell")

        # Executa scriptul de install

        # In urma executarii scriptul va returna 0 sau 1:
        # 1 daca executia a avut loc cu succes
        # 0 daca executia nu a avut succes
        # voi presupune ca nu exista erori si toate scripturile se executa corect
        returnvalue = 1
        write_in_log(" ".join((mesaj1, run_script_name, "(", str(attempts), ",",
                            str(check_exit_code), ",", str(command), ",", str(cwd), ",",
                            str(env_variables), ",", str(retry_interval), ",",
                            str(shell), ",", ")", mesaj2[returnvalue])))

def exec_after_install(comands):
    if "reboot" in comands[0].keys():
        method = comands[0].get("reboot").get("method")

        # Executa scriptul de reboot

        # In urma executarii scriptul va returna 0 sau 1:
        # 1 daca executia a avut loc cu succes
        # 0 daca executia nu a avut succes
        # voi presupune ca nu exista erori si toate scripturile se executa corect
        returnvalue = 1
        write_in_log(" ".join((mesaj1, "reboot", "(", str(method), ")", mesaj2[returnvalue])))

def exec_install_failed(comands):
    if "delete" in comands[0].keys():
        method = comands[0].get("delete").get("method")
        path = comands[0].get("delete").get("path")

        # Executa scriptul de delete

        # In urma executarii scriptul va returna 0 sau 1:
        # 1 daca executia a avut loc cu succes
        # 0 daca executia nu a avut succes
        # voi presupune ca nu exista erori si toate scripturile se executa corect
        returnvalue = 1
        write_in_log(" ".join((mesaj1, "reboot", "(", str(method), ",", str(path), ")", mesaj2[returnvalue])))

    if "shutdown" in comands[0].keys():
        method = comands[0].get("shutdown").get("method")

        # Executa scriptul de shutdown

        # In urma executarii scriptul va returna 0 sau 1:
        # 1 daca executia a avut loc cu succes
        # 0 daca executia nu a avut succes
        # voi presupune ca nu exista erori si toate scripturile se executa corect
        returnvalue = 1
        write_in_log(" ".join((mesaj1, "shutdown", "(", str(method), ")", mesaj2[returnvalue])))

def exec_config(comands):
    if "hostname" in comands.keys():
        hostname = comands.get("hostname")

        # Executa scriptul de setare a hostnameului

        # In urma executarii scriptul va returna 0 sau 1:
        # 1 daca executia a avut loc cu succes
        # 0 daca executia nu a avut succes
        # voi presupune ca nu exista erori si toate scripturile se executa corect
        returnvalue = 1
        write_in_log(" ".join((mesaj1, "Set: hostname", "(", str(hostname), ")", mesaj2[returnvalue])))

    if "users" in comands.keys():
        for user in comands.get("users"):
            user = comands.get("users").get(user)
            full_name = user.get("full_name")
            primary_group = user.get("primary_group")
            groups = user.get("groups")
            expiredate = user.get("expiredate")
            password = user.get("password")

            # Executa scriptul de setare a userului curent

            # In urma executarii scriptul va returna 0 sau 1:
            # 1 daca executia a avut loc cu succes
            # 0 daca executia nu a avut succes
            # voi presupune ca nu exista erori si toate scripturile se executa corect
            returnvalue = 1
            details = ", ".join((primary_group, str(groups), str(expiredate), password))

            write_in_log(" ".join((mesaj1, "Set: ", full_name, "(", details, ")", mesaj2[returnvalue])))




    if "write_files" in comands.keys():
        for write_file in comands.get("write_files"):
            file_name = write_file
            write_file = comands.get("write_files").get(file_name)
            path = write_file.get("path")
            permissions = write_file.get("permissions")
            encoding = write_file.get("encoding")
            content = write_file.get("content")

            # Executa scriptul de scriere a fisierului curent

            # In urma executarii scriptul va returna 0 sau 1:
            # 1 daca executia a avut loc cu succes
            # 0 daca executia nu a avut succes
            # voi presupune ca nu exista erori si toate scripturile se executa corect
            returnvalue = 1
            details = ", ".join(( path, str(permissions), str(encoding), str(content)))

            write_in_log(" ".join((mesaj1, "Write file: ", str(file_name), "(", details, ")", mesaj2[returnvalue])))

def executa(cfg):
    """
    Executa comenzile date in fisierul de configurare
    """
    if(instructions[0] in cfg.keys()):
        exec_before_install(cfg.get(instructions[0]))

    if(instructions[1] in cfg.keys()):
        exec_install(cfg.get(instructions[1]))

    if(instructions[2] in cfg.keys()):
        exec_after_install(cfg.get(instructions[2]))

    if(instructions[3] in cfg.keys()):
        exec_install_failed(cfg.get(instructions[3]))

    if(instructions[4] in cfg.keys()):
        exec_config(cfg.get(instructions[4]))

def main():
    """
        Main function.
    """
    cfg = citeste('config.cfg')
    a = open("build.log","w")
    a.close()
    if cfg:
        # print(cfg)
        executa(cfg)




if __name__ == "__main__":
    main()
