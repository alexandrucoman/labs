#! /usr/bin/python

"""
    Remote Server Control - Master (rsc-master)
    Aceasta aplicatie faciliteaza controlul, de la distanta, a unei multimi
    de servere. Conditia, desigur, este ca toate partile implicate sa fie
    conectate la internet si pe serverele (ce se doreste a fi controlate)
    sa ruleze <rsc-daemon>; controlul propriu-zis fiind realizat
    din aplicatia <rsc-master>.
"""

import sys
import os.path
import socket
from struct import pack, unpack
import pickle
from subprocess import Popen, PIPE
from inspect import getargspec
import shlex
import rsa
from colorama import init, Fore, Style, Back

init(autoreset=True)


class RSCNode(object):

    """
        Instantele acestei clase reprezinta Conexiuni TCP cu serverele (ce se
        doreste a fi controlate), ce asigura comunicarea dintre aplicatie
        si servere.
    """

    def get_last_error_message(self):

        """ Aceasta metoda returneaza ultimul mesaj de eroare. """

        return self._last_error_message

    def __init__(self, ip_address, port, timeout=3):

        self.ip_address = ip_address
        self.port = port
        self.timeout = timeout
        self.sock = None
        self.connected = False

        self._last_error_message = ""

    def get_info(self):

        """ Aceasta metoda returneaza Adresa IP si Portul. """

        return "{}:{}".format(self.ip_address, self.port)

    def establish_connection(self, password):

        """
            Aceasta metoda incearca sa stabileasca o Conexiune TCP
            cu rsc-daemon-ul, de pe un server,
            identificat prin ip_address si port.
            Odata stabilita o conexiune cu rsc-daemon-ul, este necesara
            autentificarea. In vederea realizarii acesteia, rsc-daemon-ul
            trimite Cheia Publica dintr-o Schema de Criptare RSA,
            pentru a fi criptata si, ulterior, trimisa parola de autentificare.
        """

        if self.connected:
            self._last_error_message = ""
            return ("{}{}Warning:{}"
                    " A connection is already established.".format(
                        Style.BRIGHT, Fore.YELLOW, Fore.WHITE))

        if not self.sock:
            try:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            except socket.error as error_message:
                self.sock = None
                self._last_error_message = error_message
                return ("{}{}Error:{} Could not create socket.".format(
                    Style.BRIGHT, Fore.RED, Fore.WHITE))

            self.sock.settimeout(self.timeout)

        try:
            self.sock.connect((self.ip_address, self.port))
        except socket.error as error_message:
            self.sock.close()
            self.sock = None
            self._last_error_message = error_message
            return ("{}{}Error:{} Could not connect to rsc-daemon.".format(
                Style.BRIGHT, Fore.RED, Fore.WHITE))

        public_key = self.recv_object()

        if public_key is None:
            self.sock.close()
            self.sock = None
            return ("{}{}Error:{} Could not authenticate to "
                    "rsc-daemon.".format(Style.BRIGHT, Fore.RED, Fore.WHITE))

        encrypted_password = rsa.encrypt(password, public_key)

        if not self.send_string(encrypted_password):
            self.sock.close()
            self.sock = None
            return ("{}{}Error:{} Could not authenticate to "
                    "rsc-daemon.".format(Style.BRIGHT, Fore.RED, Fore.WHITE))

        response = self.recv_string()

        if response is None:
            self.sock.close()
            self.sock = None
            return ("{}{}Error:{} Could not authenticate to "
                    "rsc-daemon.".format(Style.BRIGHT, Fore.RED, Fore.WHITE))

        if response == "INV":
            self._last_error_message = "Invalid Password!"
            self.sock.close()
            self.sock = None
            return ("{}{}Error:{} Could not authenticate to "
                    "rsc-daemon.".format(Style.BRIGHT, Fore.RED, Fore.WHITE))

        if response == "VAL":
            self._last_error_message = ""
            self.connected = True
            return "{}{}Connected.".format(Style.BRIGHT, Fore.GREEN)

        self._last_error_message = "Unknown Reasons!"
        self.sock.close()
        self.sock = None
        return ("{}{}Error:{} Could not authenticate to "
                "rsc-daemon.".format(Style.BRIGHT, Fore.RED, Fore.WHITE))

    def close_connection(self):

        """ Aceasta metoda inchide conexiunea cu rsc-daemon-ul. """

        if not self.connected:
            self._last_error_message = ""
            return ("{}{}Warning:{}"
                    " No connection established.".format(
                        Style.BRIGHT, Fore.YELLOW, Fore.WHITE))

        if not self.send_object(CommandLine("logout")):
            return ("{}{}Warning:{}"
                    " Could not Send Logout Command - {}.".format(
                        Style.BRIGHT, Fore.YELLOW, Fore.WHITE,
                        self.get_last_error_message()))

        if self.sock:
            self.sock.close()

        self.sock = None
        self.connected = False

    def is_connected(self):

        """
            Aceasta metoda returneaza True daca o conexiune este deja
            stabilita, False - in caz contrar.
        """

        return self.connected

    def _send(self, message):

        """ Aceasta metoda trimite pe socket buffer-ul message. (NJ) """

        try:
            self.sock.send(message)
        except socket.error as error_message:
            self._last_error_message = error_message
            self.connected = False
            return False

        return True

    def _recv(self, buffer_size=1024):

        """
            Aceasta metoda returneaza buffer_size octeti primiti pe socket.
            (Nivelul de Jos)
        """

        try:
            return self.sock.recv(buffer_size)
        except socket.timeout as ex:
            self._last_error_message = ex
        except socket.error as error_message:
            self._last_error_message = error_message

        self.connected = False

    def send_string(self, message):

        """
            Aceasta metoda trimite pe socket string-ul message
            conform urmatorului protocol: intai este trimisa lungimea
            string-ului, iar apoi string-ul efectiv.
        """

        message_length = len(message)
        message_length_packed = pack('L', message_length)

        if not self._send(message_length_packed):
            return False

        if not self._send(message):
            return False

        return True

    def recv_string(self):

        """
            Aceasta metoda returneaza string-ul primit pe socket
            conform urmatorului protocol: intai este primita lungimea
            string-ului, iar apoi string-ul efectiv.
        """

        message_length_packed = self._recv(4)

        if message_length_packed is None:
            return None

        message_length = unpack('L', message_length_packed)[0]

        message = self._recv(message_length)

        return message

    def send_object(self, obj):

        """
            Aceasta metoda trimite pe socket obiectul obj, avand la baza
            serializarea pickle.
        """

        return self.send_string(pickle.dumps(obj, -1))

    def recv_object(self):

        """
            Aceasta metoda returneaza obiectul primit pe socket,
            deserializat pickle.
        """

        serialized_object = self.recv_string()

        if serialized_object is None:
            return None

        return pickle.loads(serialized_object)

    def execute_command(self, command_line):

        """
            Aceasta metoda trimite comanda daemon-ului spre a fi executata;
            primeste rezultatul executiei si il returneaza.
        """

        if not self.connected:
            raise ExecuteCommandException("Not connected to RSC-Daemon")

        if not self.send_object(command_line):
            raise ExecuteCommandException("Could not Send Command - {}".format(
                self.get_last_error_message()))

        result = self.recv_object()

        if result is None:
            raise ExecuteCommandException("Could not Receive Result - {}"
                                          .format(
                                              self.get_last_error_message()))

        return result


class CommandLine(object):

    """
        Instantele acestei clase incapsuleaza comenzi-terminal.
    """

    def __init__(self, content):

        self.content = content

        command_parts = shlex.split(self.content)

        if command_parts:
            self.command = command_parts[0]
        else:
            self.command = ""

    def get_command_line(self):

        """ Aceasta metoda returneaza intreg continutul comenzii. """

        return self.content

    def get_command(self):

        """ Aceasta metoda returneaza doar comanda (fara parametri). """

        return self.command

    def get_arguments(self):

        """ Aceasta metoda returneaza doar parametri (fara comanda). """

        return shlex.split(self.content)[1:]

    def get_splitted(self):

        """ Aceasta metoda returneaza intreg continutul comenzii, ca lista. """

        return shlex.split(self.content)

    def delete_prefix(self):

        """
            Aceasta metoda sterge prefixul (comanda) din intreg continutul
            comenzii, astfel incat comanda devine urmatorul prefix.
        """

        self.content = self.content[self.content.index(self.command) +
                                    len(self.command):].lstrip(" \t")

        command_parts = shlex.split(self.content)

        if command_parts:
            self.command = command_parts[0]
        else:
            self.command = ""


class Result(object):

    """
        Instantele acestei clase incapsuleaza rezultate, cat si mesaje
        de eroare, in urma executiei unei comenzi.
    """

    def __init__(self, stdout, stderr, cwd=None):

        self.stdout = stdout
        self.stderr = stderr
        self.cwd = cwd

    def get_stdout(self):

        """ Aceasta metoda returneaza continutul iesirii standard. """

        return self.stdout

    def get_stderr(self):

        """ Aceasta metoda returneaza continutul iesirii pentru erori. """

        return self.stderr

    def get_cwd(self):

        """ Aceasta metoda returneaza cwd (current working directory). """

        return self.cwd

    def set_cwd(self, cwd):

        """ Aceasta metoda seteaza cwd (current working directory). """

        self.cwd = cwd


class Interpreter(object):

    """
        Instantele acestei clase reprezinta interpretoare ce executa comenzi -
        - obiecte CommandLine, si returneaza rezultatul executiei - obiecte
        Result, pornind de la un director - cwd.
    """

    def __init__(self, cwd, shell=True):

        self.cwd = cwd
        self.shell = shell

        self.internal_commands = {"cd": self.cd_command}

    def get_cwd(self):

        """ Aceasta metoda returneaza cwd (current working directory). """

        return self.cwd

    def add_internal_command(self, command_name, function):

        """
            Aceasta metoda adauga o noua comanda (nume-comanda, comportament)
            setului de comenzi interne interpretorului.
        """

        if command_name in self.internal_commands:
            return False

        self.internal_commands[command_name] = function

        return True

    def nothing(self):

        """
            Aceasta metoda nu face nimic si returneaza tot nimic.
            Poate fi folosita pentru a suprascrie comportamentul
            unei comenzi-shell, astfel incat sa nu fie executata de Shell.
        """

        return Result(None, None)

    def execute(self, command_line):

        """
            Aceasta metoda executa in Shell comanda - obiectul CommandLine,
            si returneaza rezultatul executiei ca obiect Result.
        """

        process = Popen(command_line.get_command_line(), stdout=PIPE,
                        stderr=PIPE, shell=self.shell, cwd=self.cwd)

        stdout, stderr = process.communicate()

        return Result(stdout, stderr)

    def execute_command(self, command_line):

        """
            Aceasta metoda verifica daca comanda primita ca parametru
            apare in setul comenzilor interne. Daca apare, este executata
            metoda/functia asociata acesteia; altfel, comanda este executata
            in Shell.
        """

        command_name = command_line.get_command()

        if command_name not in self.internal_commands:
            return self.execute(command_line)

        args = getargspec(self.internal_commands[command_name]).args

        try:
            if "command_line" in args:
                result = self.internal_commands[command_name](
                    command_line=command_line)
            else:
                result = self.internal_commands[command_name]()
        except:
            return Result(None, sys.exc_info()[1][0])

        if not isinstance(result, Result):
            if result is not None:
                result = Result("Converted Function Output: {}".format(result),
                                None)
            else:
                result = Result(None, None)

        return result

    def cd_command(self, command_line):

        """
            Change Directory Command.
        """

        args = command_line.get_arguments()

        if not args:
            self.cwd = "/"
            return Result(None, None, self.cwd)

        if len(args) > 1:
            return Result(None, "cd: Too much arguments!")

        result = self.execute(command_line)

        if not result.get_stderr():
            self.cwd = os.path.normpath(os.path.join(self.cwd, args[0]))
            result.set_cwd(self.cwd)

        return result


class ExecuteCommandException(Exception):

    """
        Instantele acestei clase reprezinta exceptii care pot fi aruncate
        atunci cand se incearca a fi executata o comanda pe un daemon.
    """

    def __init__(self, value):

        super(ExecuteCommandException, self).__init__(value)

        self.value = value

    def __str__(self):

        return repr(self.value)


class RSCMaster(object):

    """
        Instantele acestei clase reprezinta aplicatii RSC-Master.
    """

    def __init__(self):

        self.nodes = {}

        self.current_node = "{}rsc-master".format(Fore.RED)
        self.cwd = "/"
        self.prompter = "{1}{2} {3}[{5}{0}{2} {4}{0}{3}]{2} {3}>>{2} ".format(
            "{}", Style.BRIGHT, Fore.WHITE, Fore.BLUE, Fore.GREEN, Fore.CYAN)

        self.started = False

        self.interpreter = Interpreter(self.cwd)

    def start(self):

        """
            Aceasta metoda, la fiecare iteratie, citeste o comanda
            de la tastatura si determina categoria din care face parte -
            - RSC, NODE sau ALL, cu scopul de a fi executata corespunzator.
        """

        print self.interpreter.execute_command(
            CommandLine("clear")).get_stdout()

        print "{}{}".format(Style.BRIGHT, Fore.WHITE)
        print "{0}{1} {2}RSC-Master (Remote Server Control){1}".format(
            Style.BRIGHT, Fore.WHITE, Fore.BLUE)
        print "{}{}\n".format(Style.BRIGHT, Fore.WHITE)

        self.help()

        print "{}{}".format(Style.BRIGHT, Fore.WHITE)

        self.started = True

        while self.started:

            line = raw_input(self.prompter.format(self.current_node, self.cwd))

            if line == "":
                continue

            command_line = CommandLine(line)

            if command_line.get_command() == "":
                continue

            # Execute By Escape Command:

            if command_line.get_command().lower() == "rsc":
                command_line.delete_prefix()
                self.exec_command_rsc(command_line)
                continue

            if command_line.get_command() in self.nodes:
                name = command_line.get_command()
                command_line.delete_prefix()
                self.exec_command_node(name, command_line)
                continue

            if command_line.get_command().lower() == "all":
                command_line.delete_prefix()
                self.exec_command_all(command_line)
                continue

            # Execute By State:

            if self.current_node == "{}rsc-master".format(Fore.RED):
                self.exec_command_rsc(command_line)
                continue

            if self.current_node == "{}all".format(Fore.MAGENTA):
                self.exec_command_all(command_line)
                continue

            if self.current_node not in self.nodes:
                print "{}{}".format(Style.BRIGHT, Fore.WHITE)
                print ("{0}{1} {2}Error:{1} Unknown node name"
                       " - \"{3}\".".format(Style.BRIGHT, Fore.WHITE, Fore.RED,
                                            self.current_node))
                print "{}{}".format(Style.BRIGHT, Fore.WHITE)
                continue

            self.exec_command_node(self.current_node, command_line)

    def stop(self):

        """ Stop Command """

        self.started = False

    def add_node(self, name, ip_address, port):

        """ Add Command """

        if name in self.nodes:
            return ("{}{}Error:{} A node with the specified name - \"{}\","
                    " already exists.".format(
                        Style.BRIGHT, Fore.RED, Fore.WHITE, name))

        try:
            port = int(port)
        except ValueError:
            return "{}{}Error:{} Invalid argument value for PORT.".format(
                Style.BRIGHT, Fore.RED, Fore.WHITE)

        self.nodes[name] = RSCNode(ip_address, port)

    def remove_node(self, name):

        """ Remove Command """

        if name not in self.nodes:
            return ("{}{}Error:{} Node with the specified name - \"{}\","
                    " does not exists.".format(
                        Style.BRIGHT, Fore.RED, Fore.WHITE, name))

        self.disconnect_node(name)

        del self.nodes[name]

        if self.current_node == name:
            self.change_node()

    def connect_node(self, name, password):

        """ Connect Command """

        if name not in self.nodes:
            return ("{}{}Error:{} Node with the specified name - \"{}\","
                    " does not exists.".format(
                        Style.BRIGHT, Fore.RED, Fore.WHITE, name))

        result = self.nodes[name].establish_connection(password)

        if result and self.nodes[name].get_last_error_message():
            result += "{}\nReason: {}".format(
                Fore.WHITE, self.nodes[name].get_last_error_message())

        return result

    def disconnect_node(self, name):

        """ Disconnect Command """

        if name not in self.nodes:
            return ("{}{}Error:{} Node with the specified name - \"{}\","
                    " does not exists.".format(
                        Style.BRIGHT, Fore.RED, Fore.WHITE, name))

        return self.nodes[name].close_connection()

    def list_nodes(self):

        """ List Command """

        print "{}{}".format(Style.BRIGHT, Fore.WHITE)

        for name in self.nodes:

            status = "{}{}(NOT CONNECTED){}".format(
                Fore.WHITE, Back.RED, Back.RESET)

            if self.nodes[name].is_connected():
                status = "{}{}(CONNECTED){}".format(
                    Fore.WHITE, Back.GREEN, Back.RESET)

            print "{0}{1}     {2}{3}{1} - {4} {5}".format(
                Style.BRIGHT, Fore.WHITE, Fore.CYAN,
                name, self.nodes[name].get_info(), status)

        print "{}{}".format(Style.BRIGHT, Fore.WHITE)

    def change_node(self, name=None):

        """ Change Command """

        if name is None or name.lower() == "rsc-master":
            self.current_node = "{}rsc-master".format(Fore.RED)
            self.cwd = self.interpreter.get_cwd()
            return None

        if name.lower() == "all":
            self.current_node = "{}all".format(Fore.MAGENTA)
            self.cwd = "#"
            return None

        if name not in self.nodes:
            return ("{}{}Error:{} Node with the specified name - \"{}\","
                    " does not exists.".format(
                        Style.BRIGHT, Fore.RED, Fore.WHITE, name))

        self.current_node = name

        try:
            result = self.nodes[name].execute_command(
                CommandLine("cwd-update"))
        except ExecuteCommandException:
            self.cwd = "N/A"
            return ("{}{}Warning:{} Could not get CWD "
                    "(Current Working Directory).".format(
                        Style.BRIGHT, Fore.YELLOW, Fore.WHITE))

        self.cwd = result.get_cwd()

    def help(self):

        """ Help Command """

        print "{}{}".format(Style.BRIGHT, Fore.WHITE)

        print ("{0}{1} In RSC-Master application, there are 3 state classes: "
               "{2}rsc-master{1}, {3}all{1} and {4}node{1},"
               " so the introduced command will be executed by the class"
               " entity state in which the application is.\n".format(
                   Style.BRIGHT, Fore.WHITE,
                   Fore.RED, Fore.MAGENTA, Fore.CYAN))

        print ("{0}{1}     {2}{4}{1} - Local {3}RSC-Commands{1}"
               " (have priority) and Shell Commands".format(
                   Style.BRIGHT, Fore.WHITE, Fore.RED, Fore.BLUE,
                   "rsc-master"))
        print ("{0}{1}     {2}{3}{1} - Shell Commands on ALL Nodes".format(
            Style.BRIGHT, Fore.WHITE, Fore.MAGENTA, "all"))
        print ("{0}{1}     {2}{3}{1} - Shell Commands on Selected Node".format(
            Style.BRIGHT, Fore.WHITE, Fore.CYAN, "$node-name"))

        print "{}{}".format(Style.BRIGHT, Fore.WHITE)

        print ("{0}{1} Note: Use {2}change{1} command to transition between"
               " states.".format(Style.BRIGHT, Fore.WHITE, Fore.CYAN))

        print "{}{}".format(Style.BRIGHT, Fore.WHITE)

        print ("{0}{1} Exceptions of the rule above are Escape Commands: "
               "{2}rsc{1}, {3}all{1} and {4}$node-name{1}."
               " A command preceded by one of these escape commands,"
               " will be executed by the class entity state"
               " it describes.".format(Style.BRIGHT, Fore.WHITE,
                                       Fore.RED, Fore.MAGENTA, Fore.CYAN))

        print "{}{}\n".format(Style.BRIGHT, Fore.WHITE)

        print "{0}{1} {2}RSC-Commands{1}\n".format(
            Style.BRIGHT, Fore.WHITE, Fore.BLUE)

        print "{0}{1}     {2}{4}{1} {3}{5}{1} {3}{6}{1} {3}{7}{1}".format(
            Style.BRIGHT, Fore.WHITE, Fore.CYAN, Fore.YELLOW,
            "add", "name", "ip_address", "port")
        print "{0}{1}     {2}{4}{1} {3}{5}{1}".format(
            Style.BRIGHT, Fore.WHITE, Fore.CYAN, Fore.YELLOW,
            "remove", "name")
        print "{0}{1}     {2}{4}{1} {3}{5}{1} {3}{6}{1}".format(
            Style.BRIGHT, Fore.WHITE, Fore.CYAN, Fore.YELLOW,
            "connect", "name", "password")
        print "{0}{1}     {2}{4}{1} {3}{5}{1}".format(
            Style.BRIGHT, Fore.WHITE, Fore.CYAN, Fore.YELLOW,
            "disconnect", "name")
        print "{0}{1}     {2}{3}{1}".format(
            Style.BRIGHT, Fore.WHITE, Fore.CYAN, "list")
        print ("{0}{1}     {2}{6}{1}"
               " [ {3}{7}{1} | {4}{8}{1} | {5}{9}{1} ]".format(
                   Style.BRIGHT, Fore.WHITE, Fore.CYAN,
                   Fore.RED, Fore.MAGENTA, Fore.YELLOW,
                   "change", "rsc-master", "all", "node-name"))
        print "{0}{1}     {2}{3}{1}".format(
            Style.BRIGHT, Fore.WHITE, Fore.RED, "exit")

        print "{}{}".format(Style.BRIGHT, Fore.WHITE)

    def exec_command_rsc(self, command_line):

        """
            Aceasta metoda incearca sa execute comanda (primita ca parametru)
            ca o comanda interna (proprie aplicatiei).
            Daca nu este identificata ca fiind o comanda interna,
            este executata in Shell.
        """

        command_name = command_line.get_command().lower()
        arguments = command_line.get_arguments()
        number_of_arguments = len(arguments)

        if command_name == "":

            return None

        if command_name == "exit":
            self.stop()

            return None

        if command_name == "rschelp":
            self.help()

            return None

        if command_name == "add":
            if number_of_arguments == 3:
                cresult = self.add_node(arguments[0], arguments[1],
                                        arguments[2])
                if cresult:
                    print "{}{}".format(Style.BRIGHT, Fore.WHITE)
                    print "{}{} {}".format(Style.BRIGHT, Fore.WHITE, cresult)
                    print "{}{}".format(Style.BRIGHT, Fore.WHITE)
            else:
                print "{}{}".format(Style.BRIGHT, Fore.WHITE)
                if number_of_arguments < 3:
                    print ("{0}{1} {2}Too many arguments!"
                           "{1} For more information, type rschelp.".format(
                               Style.BRIGHT, Fore.WHITE, Fore.YELLOW))
                else:
                    print ("{0}{1} {2}Too much arguments!"
                           "{1} For more information, type rschelp.".format(
                               Style.BRIGHT, Fore.WHITE, Fore.YELLOW))
                print "{}{}".format(Style.BRIGHT, Fore.WHITE)

            return None

        if command_name == "remove":
            if number_of_arguments == 1:
                cresult = self.remove_node(arguments[0])
                if cresult:
                    print "{}{}".format(Style.BRIGHT, Fore.WHITE)
                    print "{}{} {}".format(Style.BRIGHT, Fore.WHITE, cresult)
                    print "{}{}".format(Style.BRIGHT, Fore.WHITE)
            else:
                print "{}{}".format(Style.BRIGHT, Fore.WHITE)
                if number_of_arguments < 1:
                    print ("{0}{1} {2}Too many arguments!"
                           "{1} For more information, type rschelp.".format(
                               Style.BRIGHT, Fore.WHITE, Fore.YELLOW))
                else:
                    print ("{0}{1} {2}Too much arguments!"
                           "{1} For more information, type rschelp.".format(
                               Style.BRIGHT, Fore.WHITE, Fore.YELLOW))
                print "{}{}".format(Style.BRIGHT, Fore.WHITE)

            return None

        if command_name == "connect":
            if number_of_arguments == 2:
                cresult = self.connect_node(arguments[0], arguments[1])
                if cresult:
                    print "{}{}".format(Style.BRIGHT, Fore.WHITE)
                    print "{}{} {}".format(Style.BRIGHT, Fore.WHITE, cresult)
                    print "{}{}".format(Style.BRIGHT, Fore.WHITE)
            else:
                print "{}{}".format(Style.BRIGHT, Fore.WHITE)
                if number_of_arguments < 2:
                    print ("{0}{1} {2}Too many arguments!"
                           "{1} For more information, type rschelp.".format(
                               Style.BRIGHT, Fore.WHITE, Fore.YELLOW))
                else:
                    print ("{0}{1} {2}Too much arguments!"
                           "{1} For more information, type rschelp.".format(
                               Style.BRIGHT, Fore.WHITE, Fore.YELLOW))
                print "{}{}".format(Style.BRIGHT, Fore.WHITE)

            return None

        if command_name == "disconnect":
            if number_of_arguments == 1:
                cresult = self.disconnect_node(arguments[0])
                if cresult:
                    print "{}{}".format(Style.BRIGHT, Fore.WHITE)
                    print "{}{} {}".format(Style.BRIGHT, Fore.WHITE, cresult)
                    print "{}{}".format(Style.BRIGHT, Fore.WHITE)
            else:
                print "{}{}".format(Style.BRIGHT, Fore.WHITE)
                if number_of_arguments < 1:
                    print ("{0}{1} {2}Too many arguments!"
                           "{1} For more information, type rschelp.".format(
                               Style.BRIGHT, Fore.WHITE, Fore.YELLOW))
                else:
                    print ("{0}{1} {2}Too much arguments!"
                           "{1} For more information, type rschelp.".format(
                               Style.BRIGHT, Fore.WHITE, Fore.YELLOW))
                print "{}{}".format(Style.BRIGHT, Fore.WHITE)

            return None

        if command_name == "list":
            if number_of_arguments == 0:
                self.list_nodes()
            else:
                print "{}{}".format(Style.BRIGHT, Fore.WHITE)
                print ("{0}{1} {2}Too much arguments!"
                       "{1} For more information, type rschelp.".format(
                           Style.BRIGHT, Fore.WHITE, Fore.YELLOW))
                print "{}{}".format(Style.BRIGHT, Fore.WHITE)

            return None

        if command_name == "change":
            if number_of_arguments <= 1:
                if number_of_arguments == 0:
                    cresult = self.change_node()
                else:
                    cresult = self.change_node(arguments[0])
                if cresult:
                    print "{}{}".format(Style.BRIGHT, Fore.WHITE)
                    print "{}{} {}".format(Style.BRIGHT, Fore.WHITE, cresult)
                    print "{}{}".format(Style.BRIGHT, Fore.WHITE)
            else:
                print "{}{}".format(Style.BRIGHT, Fore.WHITE)
                print ("{0}{1} {2}Too much arguments!"
                       "{1} For more information, type rschelp.".format(
                           Style.BRIGHT, Fore.WHITE, Fore.YELLOW))
                print "{}{}".format(Style.BRIGHT, Fore.WHITE)

            return None

        result = self.interpreter.execute_command(command_line)

        if result.get_cwd():
            if self.current_node == "{}rsc-master".format(Fore.RED):
                self.cwd = result.get_cwd()

        if result.get_stderr():
            print "{}{}".format(Style.BRIGHT, Fore.WHITE)
            print "{}{}".format(Fore.RED, result.get_stderr())
            print "{}{}".format(Style.BRIGHT, Fore.WHITE)

        if result.get_stdout():
            print "{}{}".format(Style.BRIGHT, Fore.WHITE)
            print "{}".format(result.get_stdout())
            print "{}{}".format(Style.BRIGHT, Fore.WHITE)

    def exec_command_node(self, name, command_line):

        """
            Aceasta metoda executa comanda (primita ca parametru) pe nodul
            cu numele $name si afiseaza rezultatul executiei.
        """

        try:
            result = self.nodes[name].execute_command(command_line)
        except ExecuteCommandException as ex:
            print "{}{}".format(Style.BRIGHT, Fore.WHITE)
            print "{0}{1} {2}Execute Command Error:{1} {3}.".format(
                Style.BRIGHT, Fore.WHITE, Fore.RED, ex.value)
            print "{}{}".format(Style.BRIGHT, Fore.WHITE)

            return None

        if result.get_cwd():
            if self.current_node == name:
                self.cwd = result.get_cwd()

        if result.get_stderr():
            print "{}{}".format(Style.BRIGHT, Fore.WHITE)
            print "{}{}".format(Fore.RED, result.get_stderr())
            print "{}{}".format(Style.BRIGHT, Fore.WHITE)

        if result.get_stdout():
            print "{}{}".format(Style.BRIGHT, Fore.WHITE)
            print "{}".format(result.get_stdout())
            print "{}{}".format(Style.BRIGHT, Fore.WHITE)

    def exec_command_all(self, command_line):

        """
            Aceasta metoda executa comanda (primita ca parametru)
            pe fiecare dintre noduri.
        """

        print "{}{}".format(Style.BRIGHT, Fore.WHITE)

        for name in self.nodes:

            status = "{}{}(NOT CONNECTED){}".format(
                Fore.WHITE, Back.RED, Back.RESET)

            if self.nodes[name].is_connected():
                status = "{}{}(CONNECTED){}".format(
                    Fore.WHITE, Back.GREEN, Back.RESET)

            print "{0}{1}     Node {2}{3}{1} - {4} {5}:".format(
                Style.BRIGHT, Fore.WHITE, Fore.CYAN, name,
                self.nodes[name].get_info(), status)

            self.exec_command_node(name, command_line)

        print "{}{}".format(Style.BRIGHT, Fore.WHITE)


def main():

    """ Main """

    rsc_master = RSCMaster()
    rsc_master.start()

if __name__ == '__main__':
    main()
