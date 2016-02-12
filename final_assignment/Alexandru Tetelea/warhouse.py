import json
import os
import subprocess
import time
import urllib2
import shutil
import sys
import logging
import crypt
import sys

logging.basicConfig(filename='build.log', level=logging.INFO)


def system():
    return os.name


def Download(url, destination):
    file_name = destination.split('/')[-1]
    u = urllib2.urlopen(url)
    f = open(destination, 'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading: %s Bytes: %s" % (file_name, file_size)

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8) * (len(status) + 1)
        print status,

    f.close()


def install_program(param_atempts, param_alowedExit, param_camand, param_cwd, param_env, param_retry_interval,
                    param_shell):
    logging.info("Try to install!: " + param_camand)
    if param_atempts < 1:
        return -1
    os.chdir(param_cwd)
    fail = 1
    for i in xrange(param_atempts):
        compiler = list(param_camand.split(" ")).__getitem__(0)
        installer = list(param_camand.split(" ")).__getitem__(1)
        os.environ.copy()
        error = 0
        ret = subprocess.Popen([compiler, installer], env=param_env).wait()
        if isinstance(param_alowedExit, bool):
            if ret != 0:
                if param_alowedExit:
                    print "Eroare grava!!!"
                    error = 1
        elif isinstance(param_alowedExit, int):
            if not param_alowedExit == ret:
                print "Eroare grava!!!"
                error = 1
        elif isinstance(param_alowedExit, list):
            if not param_alowedExit in ret:
                print "Eroare grava!!!"
                error = 1
        if error == 0:
            print "SUCCESS!!"
            fail = 0
            break
        time.sleep(param_retry_interval)
    return fail


def reboot(type="soft"):
    message = 'Rebooting'
    logging.info("Restart System!")
    timeout = 5
    bReboot = 1
    if str(sys.platform).__contains__("linux"):
        try:
            if type == "soft":
                os.system('/sbin/shutdown -r now')
            elif type == "hard":
                os.system('/sbin/reboot -f')
        except:
            logging.warn("Posibil sa nu avti drepturile necesare!")
    elif str(sys.platform).__contains__("win"):
        try:
            import win32api
            if type == "soft":
                win32api.InitiateSystemShutdown(None, message, timeout, 0, bReboot)
            elif type == "hard":
                win32api.InitiateSystemShutdown(None, message, timeout, 1, bReboot)
        except:
            logging.warn("Posibil sa nu aveti drepturile necesare!")


def ShutDown(type="soft"):
    message = 'ShutDown'
    timeout = 5
    logging.info("Restart! ")
    if str(sys.platform).__contains__("linux"):
        try:
            if type == "soft":
                os.system('/sbin/shutdown now')
            elif type == "hard":
                os.system('/sbin/poweroff')
        except:
            logging.warn("Posibil sa nu avti drepturile necesare!")
    elif str(sys.platform).__contains__("win"):
        try:
            import win32api
            if type == "soft":
                win32api.InitiateSystemShutdown(None, message, timeout, 0, 0)
            elif type == "hard":
                win32api.InitiateSystemShutdown(None, message, timeout, 1, 0)
        except:
            logging.warn("Posibil sa nu aveti drepturile necesare!")


def delete(type="force", path=os.getcwd()):
    logging.info("Delete File")

    if os.path.exists(path):
        try:
            if type=="soft":
                shutil.rmtree(path)
                logging.info("Sters cu succes!: " + path)
            elif type=="hard":
                os.unlink(path)
                os.rmdir(path)
        except:

            logging.warn("Nu s-a putut sterge!: " + path)
    else:
        logging.warn("Inexistent!: " + path)


def config(configData):
    logging.info("Config System")

    os.system(configData["hostname"])
    for key, value in configData["users"].iteritems():
        createUser(value["full_name"], key, value["password"])


def createUser(name, username, password):
    logging.info("Create user")
    encPass = crypt.crypt(password, "22")
    return os.system(
        "useradd -p " + encPass + " -s " + "/bin/bash " + "-d " + "/home/" + username + " -m " + " -c \"" + name + "\" " + username)


def main(file):
    with open(file) as data_file:
        data = json.load(data_file)
        fail = 0
        for need in data["before_install"]:
            Download(need["download"]["source"], need["download"]["destination"])
        if "install" in dict(data).keys():
            for task in data["install"]:
                attempts = task["run_script"]["attempts"]
                allowed_exit_codes = task["run_script"]["check_exit_code"]
                if allowed_exit_codes.lower() == "true":
                    allowed_exit_codes = bool("true")
                elif allowed_exit_codes.lower() == "false":
                    allowed_exit_codes = bool("")
                command = task["run_script"]["command"]
                cwd = task["run_script"]["cwd"]
                env_variables = task["run_script"]["env_variables"]
                retry_interval = task["run_script"]["retry_interval"]
                shell = task["run_script"]["shell"]
                fail = install_program(attempts, allowed_exit_codes, command, cwd, env_variables, retry_interval, shell)
            if "after_install" in dict(data).keys():
                if fail == 0:
                    for task_after in data["after_install"]:
                        if "reboot" in task_after.keys():
                            if "reboot" in task_after.keys():
                                ShutDown(str(task_after["reboot"]["method"]).lower())
                            elif "delete" in task_after.keys():
                                delete(str(task_after["delete"]["method"]).lower(),
                                       str(task_after["delete"]["path"]).lower())
                            elif "shutdown" in task_after.keys():
                                ShutDown(str(task_after["shutdown"]["method"]).lower())
                elif fail == 1:
                    for task_after_fail in data["install_failed"]:
                        if "reboot" in task_after_fail.keys():
                            ShutDown(str(task_after_fail["reboot"]["method"]).lower())
                        elif "delete" in task_after_fail.keys():
                            delete(str(task_after_fail["delete"]["method"]).lower(),
                                   str(task_after_fail["delete"]["path"]).lower())
                        elif "shutdown" in task_after_fail.keys():
                            ShutDown(str(task_after_fail["shutdown"]["method"]).lower())

        if "config" in dict(data).keys():
            config(data["config"])
            pass


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print("Nu ati dat numele fisierului!")
