import subprocess
import os
import urllib
import argparse


def before_install():
    """ Run the download script """
    os.system("bash ./download.sh")


def install():
    """ Run the install script """
    attempts = 0
    retry_interval = 3
    command = "bash /home/alex/script.sh"
    cwd = "/home/alex/"
    env_variables = {"tuxy": "Tuxy Pinguinescu"}
    while attempts != 3:
        os.system("bash /home/alex/script.sh > /home/alex/")
        attempts += 1


def bigf():
    """ Parse the config file """
    fis = open("/Users/ilaumarius/Desktop/Test Labs/config.in", "r")
    words = [word.strip() for line in fis.readlines() for word in line.split('[ ]') if word.strip()]
    words = ''.join(c for c in words if c not in ':{[}], ')
    print(words)
#    print(", ".join(words))

bigf()
before_install()
