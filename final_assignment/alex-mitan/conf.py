#!/usr/bin/env python
# *-* coding: UTF-8 *-*

from __future__ import print_function

import ast
import os
import sys
import time
import urllib

# the raw content of the config file

build_log = open("build.log", "w")


def func_config(cfg_path):
    # Phase -1 - Set variables
    build_log.write("Working platform: " + sys.platform + '\n')

    if sys.platform.lower().startswith("win"):
        work_os = "windows"
    elif sys.platform.lower().startswith("linux"):
        work_os = "linux"

    build_log.write("Platform interpreted as: " + work_os + '\n' + '\n')
    # Phase 0 - Parse dict from file

    # cut out the actual portion of the string for the config dictionary
    cfg_raw = open(cfg_path, "r").read()

    dict_start = cfg_raw.index("{")
    dict_end = len(cfg_raw) - 1
    while cfg_raw[dict_end] != "}":
        dict_end -= 1

    cfg_raw = cfg_raw[dict_start:dict_end + 1]
    cfg_dict = dict(eval(cfg_raw))

    if cfg_dict:
        build_log.write("Config dictionary successfully parsed")
    else:
        build_log.write("ERROR: Config dictionary failed to parse")
        return "error"

    # Phase 1 - Go through dict

    # For each phase (before_install, install, after_install)
    for phase_list in cfg_dict.keys():
        build_log.write("            phase_list: " + phase_list + '\n')

        # For each command list in process
        for cmd_dict in cfg_dict[phase_list]:

            build_log.write("    cmd_dict: " + str(cmd_dict) + '\n')
            for command in cmd_dict:

                # CONFIG
                if phase_list == "config":
                    # TODO: config phase
                    pass

                # BEFORE INSTALL :
                if phase_list == "before_install":
                    build_log.write("    PRE-INSTALL COMMAND: " + command + '\n')

                    # download a file
                    if command == "download":
                        dl_url = cmd_dict["download"]["source"]
                        build_log.write("dl_url: " + dl_url + '\n')
                        dl_path = cmd_dict["download"]["destination"]
                        build_log.write("dl_path: " + dl_path + '\n')

                        dl_content = urllib.URLopener()
                        dl_content.retrieve(dl_url, dl_path)

                        if os.path.getsize(dl_path):
                            build_log.write("File \"" + os.path.basename(
                                dl_path) + "\" successfully downloaded from " + dl_url + '\n')
                        else:
                            build_log.write("ERROR: File not downloaded" + '\n')
                            return "error"

                    else:
                        build_log.write("Invalid before_install command: " + command + '\n')
                # INSTALL:
                if phase_list == "install":
                    build_log.write("        INSTALL COMMAND: " + command + '\n')

                    # run a script
                    if command == "run_script":
                        scr_command = cmd_dict["run_script"]["command"]
                        # change directory
                        if cmd_dict["run_script"]["cwd"]:
                            if not os.system("cd " + cmd_dict["run_script"]["cwd"]):
                                build_log.write("Changed directory to: " + cmd_dict["run_script"]["cwd"] + '\n')
                            else:
                                build_log.write("ERROR: changing directory failed!" + '\n')
                                return "error"

                        # set env. variables
                        for var in cmd_dict["run_script"]["env_variables"]:
                            var_value = cmd_dict["run_script"]["env_variables"][var]
                            build_log.write("Setting variable: " + var + "to" + str(var_value) + '\n')
                            os.environ[var] = var_value
                            if os.environ[var] == var_value:
                                build_log.write("+   Successfully set " + var + "to" + var_value + '\n')

                        # execute command
                        scr_exit_code = os.system(scr_command)
                        build_log.write("script exit command: " + str(scr_exit_code) + '\n')
                        build_log.write("script attempt: " + "1" + '\n')

                        # if we have to repeat it
                        if cmd_dict["run_script"]["check_exit_code"]:
                            if cmd_dict["run_script"]["retry_interval"]:
                                scr_interv = cmd_dict["run_script"]["retry_interval"]
                            attempts = 1
                            while attempts <= cmd_dict["run_script"]["attempts"] and scr_exit_code:
                                # sleep for interval
                                if scr_interv:
                                    time.sleep(scr_interv)
                                build_log.write("Checking exit code and retrying" + '\n')
                                attempts += 1
                                build_log.write("script attempt: " + attempts + '\n')
                                scr_exit_code = os.system(scr_command)
                        if cmd_dict["run_script"]["shell"]:
                            pass
                            # TODO: shell stuff

                # AFTER INSTALL:
                if phase_list == "after_install":
                    build_log.write("        INSTALL COMMAND: " + command)
                    if command == "reboot":
                        if cmd_dict["reboot"]["method"] == "soft":
                            build_log.write("Performing soft reboot")
                            if work_os == "linux":
                                # os.system("sudo reboot")
                                pass
                            elif work_os == "windows":
                                # os.system("shutdown -r")
                                pass
                        elif cmd_dict["reboot"]["method"] == "hard":
                            build_log.write("Performing hard reboot")
                            if work_os == "linux":
                                # os.system("sudo halt")
                                pass
                            elif work_os == "windows":
                                # os.system("shutdown -r -f")
                                pass
                        pass

    return "fine"


# the path to the config file
config_path = "/home/alex/git/python-lab/final_assignment/alex-mitan/myConfig.txt"

if func_config(config_path) != "fine":
    # TODO: if function fails, do -force
    pass
