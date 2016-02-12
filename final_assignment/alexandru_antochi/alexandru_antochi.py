import json
import os
import subprocess
import shutil
from datetime import datetime
import time
import urllib

fail = 0


def parse_script():
    """Functia citeste scriptul dat si il executa"""

    log = open("tuxylog.log", 'a+')  # se creeaza fisierul de log
    try:
        with open('tuxy.json', encoding='utf-8') as file:
            data = json.load(file)
    except IOError:
        print("Nu se poate deschide fisierul")
        return
    if 'config' in data:
        for command in data['config']:
            if command == "hostname":
                os.system("hostname")
                os.system(command)
                log.write("Hostname set to: %s" % command)
            if command == "user":
                os.system("useradd")
                log.write("User %s added." % data['config']['hostname']['users'][0])
                os.system(data['config']['hostname']['users'][0])
                for i in data['config']['hostname']['users'][0]:
                    os.system(data['config']['hostname']['users'][0][i])  # scrie fiecare linie din script in shell
                    log.write("%s" % data['config']['hostname']['users'][0][i])
    if 'before_install' in data:
        for i in range(0, len(data["before_install"][0])):
            if 'download' in data["before_install"][i]:
                source = data["before_install"][i]["download"]["source"]
                destination = data["before_install"][i]["download"]["destination"]
                os.chdir(destination)  # setam working dir
                urllib.urlretrieve(source, ["script.sh"])  # !!nu gasesc comanda pentru retrieve de pe link
                log.write("[%s]Copied files from %s to %s" % (datetime.now(), source, destination))  # scriem in log
    if 'install' in data:
        for i in range(0, len(data["install"][0])):
            if 'run_script' in data["install"]:
                run_times = int(data["install"][i]["run_script"]["attempts"])
                retry_interval = int((data["install"][i]["run_script"]["retry_interval"]))
                check_exit_code = bool(data["install"][i]["run_script"]["check_exit_code"])
                command = (data["install"][i]["run_script"]["command"])
                cwd = (data["install"][i]["run_script"]["cwd"])
                env_variables = (data["install"][i]["run_script"]["env_variables"])
                log.write("Script #%s running..." % i)
                os.chdir(cwd)  # setam cwd
                for k in range(0, len(data["install"][i]["run_script"]["env_variables"][k])):
                    os.environ[(data["install"][0]["run_script"]["env_variables"][k])] = str(env_variables)
                for j in range(0, run_times):
                    subprocess.call(command)
                    if check_exit_code:
                        code_error = subprocess.STDOUT
                    if code_error == 0:
                        global fail
                        fail += 1
                        break
                    else:
                        log.write("Script %s error: %s" % (i, code_error))
                        time.sleep(int(retry_interval))  # intervalul de retry daca codul erorii !=0
    if fail == (data["install"][i]["run_script"]["attempts"]):
        log.write("Installation failed %s times" % fail)
        if "install_failed" in data:
            for i in range(0, data["install_failed"][0])
                for command in data["install_failed"]:
                    log.write(data["install_failed"]["command"])
                    if command == "delete":
                        method = data[data["install_failed"][command]["delete"]["method"]]
                        path = data[data["install_failed"][command]["delete"]["path"]]
                        shutil.rmtree(path + " -f")
                    if command == "shutdown":
                        method = data["install_failed"][command]["method"]
                        if method == 'hard' or method == 'force':
                            os.system("shutdown -f")
                        else:
                            os.system("shutdown")
    else:
        if 'after_install' in data:
            log.write("\n After install:")
            for i in range(0, len(data["after_install"][0])):
                if 'reboot' in (data["after_install"][i]):
                    method = (data["after_install"][i]["method"])
                    log.write("")
                    if method == 'hard':
                        os.system("reboot -f")
                    else:
                        os.system("reboot")
    if "write_files" in data:
        for command in data["write_files"]:
            for i in command:
                if i == "encoding":
                    encoding = data["write_files"]["command"][i]["encoding"]
                if i == "path":
                    path = (data["write_files"]["command"][i]["path"])
                    path = path.split('/')
                    os.chdir(path[0:len(path) - 2])
                    open(path[len(path) - 1], 'r+')  # content e gol
                if i == "permissions":
                    os.system('chmod' + path[len(path) - 1] + int(data["write_files"]["command"][i]["permissions"]))


if __name__ == "__main__":
    parse_script()
