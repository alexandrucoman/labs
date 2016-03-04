#!/usr/bin/env python
# *-* coding: UTF-8 *-*
# pylint: disable=import-error

from __future__ import print_function

# Notes: Pentru a instala bibleoteca yaml trebuie să rulați
#        următoarea comandă: pip install pyaml

import yaml
import os

class Action:
    
    class Reboot:
        config_params = None
        
        def __init__(self, conf):
            self.config_params = conf
            self.execute()

        def execute(self):
            if self.config_params["method"] == "hard":
                os.system("shutdown -r now")
            else:
                os.system("shutdown -r")
            

    class Download:
        config_params = None
        
        def __init__(self, conf):
            self.config_params = conf
            self.execute()

        def execute(self):
            os.system("wget %s %s" % (self.config_params["source"], 
                     self.config_params["destination"]))

    """ Don't know exactly what is supposed to do"""
    class Hostname:
        config_params = None
        
        def __init__(self, conf):
            self.config_params = conf
            self.execute()

        def execute(self):
            pass

    class Users:
        config_params = None
        
        def __init__(self, conf):
            self.config_params = conf
            self.execute()

        def execute(self):
            for name, attr in self.config_params.items():
                os.system("useradd %s -f %s -s %s -G %s -g %s"
                         % (name, attr["expiredate"], attr["full_name"], ", ".join(attr["groups"],
                            attr["primary_group"])))
                os.system("chpasswd %s:%s" % (name, attr[password]))

    class WriteFiles:
        config_params = None
        
        def __init__(self, conf):
            self.config_params = conf
            self.execute()

        def execute(self):
            for file_name, attrs in self.config_params.items():
                os.system("touch %s " % (attrs["path"] + os.sep + file_name + "_tmp"))
                os.system("echo %s >> %s" % (attrs["content"], 
                         attrs["path"] + os.sep + file_name + "_tmp"))
                os.system("iconv -t %s %s > %s" % (attrs["encoding"], 
                                                  attrs["path"] + os.sep + file_name + "_tmp",
                                                  attrs["path"] + os.sep + file_name))
                os.system("rm %s" % attrs["path"] + os.sep + file_name + "_tmp")


    class RunScript:
        config_params = None
        
        def __init__(self, conf):
            self.config_params = conf
            self.execute()

        def execute(self):
            for var_name, var_value in self.config_params["env_variables"].items():
                os.environ[var_name] = var_value

            current_cwd = os.getcwd()
            os.chdir(config_params["cwd"])
            os.system(config_params["command"])
            os.chdir(current_cwd)


    class Delete:
        config_params = None
        
        def __init__(self, conf):
            self.config_params = conf
            self.execute()

        def execute(self):
            if self.config_params["method"] == "force":
                os.system("rm -f %s" % self.config_params["path"])
            else:
                os.system("rm %s" % self.config_params["path"])

    class Shutdown:
        config_params = None
        
        def __init__(self, conf):
            self.config_params = conf
            self.execute()

        def execute(self):
            if self.config_params["method"] == "hard":
                os.system("shutdown now")
            else:
                os.system("shutdown")


class ActionDispatcher:
    
    def __init__(self):
        pass
    
    def dispatch(self, actions):
        for action, params in actions.items():
            if action == "reboot":
                Action.Reboot(params)
            elif action == "download":
                Action.Download(params)
            elif action == "hostname":
                Action.Hostname(params)
            elif action == "users":
                Action.Users(params)
            elif action == "write_files":
                Action.WriteFiles(params)
            elif action == "run_script":
                Action.RunScript(params)
            elif action == "delete":
                Action.Delete(params)
            elif action == "shutdown":
                Action.Shutdown(params)


def main(path):
    """Citim fisierul de configurare."""
    try:
        with open(path, "r") as fisier:
            config = yaml.load(fisier)
            dispatcher = ActionDispatcher()
            
            for label, body in config.items():
                if isinstance(body, list):
                    for l_item in body:
                        dispatcher.dispatch(l_item)
                else:
                    dispatcher.dispatch(body)
                
    except (IOError, ValueError):
        print("Nu am putut citi datele din fisierul de configurare.")
        return

    print(config)


if __name__ == "__main__":
    main("../../date_intrare/tuxy.config")
