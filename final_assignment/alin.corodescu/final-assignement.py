
#import the config file in commands
import subprocess
import os
import time

#citesc fisierul de comenzi ca pe un dictionar
commands = eval(open("config.py").read())

def stage(name):
	""" executa instructiunile din stage-ul cu numele name"""
	if name == "install_failed":
		print "Instalarea a esuat"
		print "Execut comenzile de refacere"
	for command in commands[name]:
		#am o lista
		for dict_instr in command:
			#asta e un dictionar
			for cheie,dictionar in dict_instr.items():
			# forma  key :dictionar_parametri
				if cheie == "run_script":
					res = functie_run(dictionar)
					if (res != 0):
						stage("install_failed")
					continue
				if cheie == "download":
					res = functie_download(dictionar)
					if (res != 0):
						stage("install_failed")
					continue
				if cheie == "reboot":
					res = functie_reboot(dictionar)
					if (res != 0):
						stage("install_failed")
					continue
				if cheie == "delete":
					res = functie_delete(dicitonar)
					if (res != 0):
						stage("install_failed")
					continue
				if cheie == "shutdown":
					res = functie_shudtdown(dictionar)
					if (res != 0):
						stage("install_failed")
					continue

def functie_download(dictionar):
	"""downloadeaza fisierul din source in destinatie"""
	source = dictionar["source"]
	dest = dictionar["destination"]
	command = "wget %s %s" %source %dest
	try:
		proc = subprocess.check_output(['bash', '-c', command])
	except subprocess.CalledProcessError as error:
		print error.returncode
		print error.output
		return -1
	return 0

def functie_run(dictionar):
	"""ruleaza comenzile aflate in dictionar"""
	attempts = dictionar["attempts"]
	exit_codes = dictionar["check_exit_code"]
	command = dictionar["command"]
	cwd = dictionar["cwd"]
	env_variables = dictionar["env_variables"]
	retry_interval = dictionar["retry_interval"]
	local_shell = dictionar["shell"]

	while attempts:
		try:
			output = subprocess.check_output(['bash','-c', command], shell = local_shell)
		except subprocess.CalledProcessError:
			attempts = attempts - 1
			if attempts:
				time.sleep(retry_interval)
	else: 
		return -1
	try:
		proc = subprocess.check_output(['bash', '-c', "cwd " + cwd])
	except subprocess.CalledProcessError as error:
		print "Nu am putut schimba directorul de lucru"
		print error.returncode
		print error.output
		return -1

	for nume, val in env_variables:
		os.environ[nume] = string(val)

	return 0


def functie_reboot(dictionar):
	"""reboot la pc"""
	method = dictionar["method"]

	#if in linux , might not work on windows
	try:
		os.system('reboot now')
	except:
		return -1
	return 0

def functie_delete(dictionar):
	"""sterge path-ul cu optiunea din method"""
	method = dictionar["method"]
	path = dictionar["path"]
	command = "-rm "
	if method == "force":
		command += "-rf"
	command += path
	try:
		proc = subprocess.check_output(['bash', '-c', command])
	except subprocess.CalledProcessError as error:
		print error.returncode
		print error.output
		return -1
	return 0
 
def functie_shutdown(dictionar):
	"""shutdown la pc cu optiunea din method"""
	method = dicitonar["method"]

	command = "shutdown now"
	if method == "hard":
		command += " -h"
	try:
		os.system(command)
	except:
		return -1
	return 0

def run_config(dictionar):
	"""creaza useri si scrie fisiere"""
	for cheie, dict_param in dictionar.items():
		if cheie == "users":
			for user, params in dict_param.items():
				name = params["full_name"]
				pgrup = params["primary-group"]
				groups = params["groups"]
				exp = params["expiredate"]
				password = params["password"]
				group_list = "("+" ".join(groups) + ")"
				command = "-useradd -e %s -g %s -G %s -p %s %s" %exp %pgrup %group_list %password %name
				try:
					proc = subprocess.check_output(['bash', '-c', command])
				except subprocess.CalledProcessError as error:
					print error.returncode
					print error.output
				# creaza userul

		if cheie == "write_files":
			for val,detalii in dict_param.items():
				path = detalii["path"]
				perm = detalii["permissions"]
				encoding = detalii["encoding"]
				content = detalii["content"]

				out= open(path, "w", encoding)
				out.write(content)
				command = "chmod %s %s" %perm %path
				try:
					proc = subprocess.check_output(['bash', '-c', command])
				except subprocess.CalledProcessError as error:
					print error.returncode
					print error.output
					return -1
		if cheie == "hostname":
			command = "hostname %s" %dict_param
			try:
				proc = subprocess.check_output(['bash', '-c', command])
			except subprocess.CalledProcessError as error:
				print error.returncode
				print error.output
				return -1
	return 0

if (__name__ == "__main__"):
	"""apeleaza config si apoi install"""
	run_config(commands["config"])
	stage("before_install")
	stage("install")
	stage("after_install")
