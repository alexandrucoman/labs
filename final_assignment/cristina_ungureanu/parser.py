#!/usr/bin/env python
# *-* coding: UTF-8 *-*

import os
import json
import urllib2
import subprocess as sp
import time
from pprint import pprint

with open('document') as data_file:    
    data = json.load(data_file)


log_file = open("logfile","w")
log_file.close()

log_file = open("build.log","a")

#before_install
url_download = data["before_install"][0]["download"]["source"]
de_descarcat = urllib2.urlopen(url_download)
fisier_descarcat = open("/home/random/script.sh","w")
fisier_descarcat.write(de_descarcat.read())
fisier_descarcat.close()
log_file.write("Am terminat before_install.\n")


log_file.write("Trec la install.\n")


#install
attempts = int(data['install'][0]['run_script']['attempts'])
check_exit_code = data['install'][0]['run_script']['check_exit_code']
command = data['install'][0]['run_script']['command']
cwd = data['install'][0]['run_script']['cwd']
env_dict = dict(data['install'][0]['run_script']['env_variables'])
retry_interval = int(data['install'][0]['run_script']['retry_interval'])
shell = data['install'][0]['run_script']['shell']

log_file.write("Incarc parametrii din JSON.\n")

for i in range(attempts):
    process = sp.Popen(command.split(' '), stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = process.communicate()
    if len(err) == 0:
        break
    else:
        log_file.write(err)
        time.sleep(1)
       
os.environ["PWD"]=cwd
os.environ[env_dict.items()[0][0]]=env_dict.items()[0][1]

log_file.write("Gata install.")

#tip_metoda = data['after_install'][0]['reboot']["method"]

#if tip_metoda == "soft":
#    os.system('shutdown -r +5 "Restarting..."')
#if tip_metoda == "hard":
#    os.system('reboot -f')


failed_delete_type = data['install_failed'][0]['delete']["method"]
#print failed_delete_type
failed_delete_path = data['install_failed'][0]['delete']['path']
#print failed_delete_path
failed_shutdown_type = data['install_failed'][1]['shutdown']['method']
#print failed_shutdown_type


#print "hostname "+data['config']["hostname"]
#os.system("hostname "+data['config']["hostname"])


full_name = data['config']['users']['acoman']['full_name']
primary_group = data['config']['users']['acoman']['primary-group']
groups = list(data['config']['users']['acoman']['groups'])
expiredate = data['config']['users']['acoman']['expiredate']
password = data['config']['users']['acoman']['password']


#os.system("useradd -e \'"+expiredate+"\' -p \'"+password+"\' -c \'"+full_name+"\' -G ")

print "write_files:"
for idx in range(len(list(data['config']['write_files']))):
    print data['config']['write_files'][str(idx)]
    #...etc...




log_file.close()


