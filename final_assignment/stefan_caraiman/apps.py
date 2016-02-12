from __future__ import print_function
import urllib
import subprocess, sys, os

#os.system("shutdown -h")
CHEILE = ["before_install", "install", "after_install", "install_failed", "config"]
LOG_FILE = open('build.log', 'wb+')


def installapp(config_file):
    comenzi = eval(config_file)  # config file is given as a dictionary
    for key in comenzi:
        if key not in CHEILE:
            LOG_FILE.write("{} command is not part of the installing\n".format(key))
    for key in CHEILE:
        if key not in comenzi:
            LOG_FILE.write("Missing the {} command in the install\n".format(key))
    #before_install(comenzi["before_install"][0])
    #install(comenzi["install"][0])
    #after_install(comenzi["after_install"][0])
    #install_failed(comenzi["install_failed"][0])
    #config(comenzi["config"][0])
    #print(comenzi["before_install"])
    #print(comenzi["before_install"][0]["download"]['source'])


def before_install(before_i):
    source = before_i['download']['source']
    destination = before_i['download']['destination']
    try:
        file_install = open(destination, 'wb')
        file_install.write(urllib.urlopen(source).read())
        file_install.close()
        LOG_FILE.write("Finished the before-install process\n")
    except:
        LOG_FILE.write("Something went wrong with the before-install process\n")
        return


def install(install_c):
    for k in install_c:
        if k != "run_script":
            LOG_FILE.write("Unexpected command for the install process\n")
        elif k == "run_script":
            LOG_FILE.write("Starting the run_script command from the install process\n")
            shell_value = install_c["run_script"]["shell"]
            timeout_value = install_c["run_script"]["retry_interval"]
            attempts = install_c["run_script"]["attempts"]
            cwd = "cd "
            cwd += install_c["run_script"]["cwd"]
            command = install_c["run_script"]["command"]
            exit_code = install_c["run_script"]["check_exit_code"]
            for key in install_c["run_script"]["env_variables"]:
                os.environ[key] = install_c["run_script"]["env_variables"][key]
            if os.name == 'posix':
                for i in xrange(0, attempts):
                    run_process = subprocess.Popen(cwd, command, shell=shell_value,
                                                   executable='/bin/bash', timeout=timeout_value)
                    run_process.communicate()
            if os.name == "nt":
                pass
        LOG_FILE.write("Finished the run_script command from the install process\n")


def after_install(install_af):
    reboot_method = install_af["reboot"]["method"]
    if os.name == 'nt':
        run_process = subprocess.Popen(["powershell.exe", "Restart-Computer -computerName  -{}"
                                       .format(reboot_method)], stdout=sys.stdout)
        run_process.communicate()
    elif os.name == 'posix':
        run_process = subprocess.Popen("sudo reboot --{} ".format(reboot_method), shell=True, executable='/bin/bash')
        run_process.communicate()


def install_failed(install_f):
    path = os.path.dirname(os.path.abspath(__file__))
    if os.name == 'nt':
        run_process = subprocess.Popen(["powershell.exe", path+"\shutdownhard.ps1"], stdout = sys.stdout)
        run_process.communicate()
    elif os.name == 'posix':
        run_process = subprocess.Popen("sudo shutdown -h 0", shell=True, executable='/bin/bash')
        run_process.communicate()


def config(configd):
    hostname = configd["hostname"]
    print(hostname)


def main():
    try:
        fisier = open("config.txt", "r")
        configs = fisier.read()
        fisier.close()
        installapp(configs)
    except IOError:
        print("Nu am putut obtine fisierul de configurare.")


if __name__ == "__main__":
    main()