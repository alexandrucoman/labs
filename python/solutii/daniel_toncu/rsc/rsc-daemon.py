#! /usr/bin/python

"""
    Remote Server Control - Daemon (rsc-daemon)
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
from datetime import datetime, timedelta
import pickle
import random
import string
from subprocess import Popen, PIPE
from inspect import getargspec
import shlex
import rsa
from colorama import init, Fore, Style

init(autoreset=True)


class RSCDaemon(object):

    """
        Instantele acestei clase reprezinta Servere TCP,
        care accepta si, ulterior, serveste clienti rsc-master.
    """

    _last_error_message = ""

    def get_last_error_message(self):

        """ Aceasta metoda returneaza ultimul mesaj de eroare. """

        return self._last_error_message

    def add_logger(self, logger):

        """ Aceasta metoda adauga logger-ul la lista loggers a aplicatiei. """

        self.loggers.append(logger)

    def log(self, log_message):

        """
            Aceasta metoda notifica (apeleaza metoda log()) toti logger-ii
            aplicatiei cu mesajul log_message.
        """

        for logger in self.loggers:
            logger.log(log_message)

    def __init__(self, ip_address='localhost', port=50105, password=None):

        self.ip_address = ip_address
        self.port = port
        self.password = password
        self.sock = None
        self.connection = None
        self.started = False
        self.black_list = BlackList()
        self.loggers = []

        if self.password is None:
            self.password = ''.join(random.SystemRandom().choice(
                string.ascii_letters + string.digits) for _ in range(64))
            print " {}{}Random Generated Password:{} {}".format(
                Style.BRIGHT, Fore.BLUE, Fore.WHITE, self.password)

    def start_server(self):

        """
            Aceasta metoda initiaza si porneste daemon-ul pe post de server.
        """

        if self.started:
            self._last_error_message = ""
            return ("{}{}Warning:{}"
                    " The Server is already started.".format(
                        Style.BRIGHT, Fore.YELLOW, Fore.WHITE))

        if not self.sock:
            try:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            except socket.error as error_message:
                self.sock = None
                self._last_error_message = error_message
                return ("{}{}Error:{} Could not create socket.".format(
                    Style.BRIGHT, Fore.RED, Fore.WHITE))

        try:
            self.sock.bind((self.ip_address, self.port))
            self.sock.listen(1)
        except socket.error as error_message:
            self.sock.close()
            self.sock = None
            self._last_error_message = error_message
            return ("{}{}Error:{} Could not bind/listen on socket.".format(
                Style.BRIGHT, Fore.RED, Fore.WHITE))

        self.started = True

        print " {}{}Server Started Successfully! {}{}".format(
            Style.BRIGHT, Fore.GREEN, Fore.YELLOW, self.sock.getsockname())

        self.log("Server Started Successfully! {}".format(
            self.sock.getsockname()))

    def accept_client(self):

        """
            Aceasta metoda stabileste o conexiune cu rsc-master urmand pasii:
            accepta o conexiune noua, verifica daca Adresa IP ce a initiat
            conexiunea apare in BlackList, genereaza (random) o pereche
            de Chei RSA, trimite Cheia Publica, primeste Parola (criptata),
            decripteaza Parola si o compara cu cea stabilita anterior - daca
            Parola corespunde, conexiunea este acceptata;
            altfel, este ignorata.
        """

        try:
            self.connection, address = self.sock.accept()
        except socket.error as error_message:
            self.started = False
            self._last_error_message = error_message
            self.log("Server Stopped. Reason: {}.".format(
                self.get_last_error_message()))
            return False

        if not self.black_list.check(address[0]):
            self.connection.close()
            self.log("Connection Refused to Host {}."
                     " Reason: BlackList.".format(address))
            return False

        keys = rsa.newkeys(256)

        if not self.send_object(keys[0]):
            self.connection.close()
            self.log("Connection Refused to Host {}."
                     " Reason: Authentication: {}.".format(
                         address, self.get_last_error_message()))
            return False

        self.connection.settimeout(1)

        encrypted_password = self.recv_string()

        if encrypted_password is None:
            self.connection.close()
            self.log("Connection Refused to Host {}."
                     " Reason: Authentication: {}.".format(
                         address, self.get_last_error_message()))
            return False

        self.connection.settimeout(None)

        if rsa.decrypt(encrypted_password, keys[1]) == self.password:
            self.black_list.delete_entry(address[0])
            if not self.send_string("VAL"):
                self.connection.close()
                self.log("Connection Refused to Host {}."
                         " Reason: Authentication: {}.".format(
                             address, self.get_last_error_message()))
                return False
            self.log("Accepted Connection to Host {}.".format(address))
            return True

        self.send_string("INV")
        self.connection.close()
        self.log("Connection Refused to Host {}."
                 " Reason: Authentication: Invalid Password.".format(address))
        return False

    def start(self):

        """
            Aceasta metoda initiaza si porneste server-ul, dupa care,
            la fiecare iteratie, accepta si serveste un client <rsc-master>.
            Daemon-ul tranzitioneaza in starea in care serveste clientul
            acceptat doar daca Autentificarea a fost cu succes.
        """

        error_message = self.start_server()

        if error_message:
            print " {}{}Could not start Server!".format(
                Style.BRIGHT, Fore.WHITE)
            print "{} ({})".format(
                error_message, self.get_last_error_message())
            return None

        while self.started:

            if not self.accept_client():
                continue

            self.serve_client()

    def serve_client(self):

        """
            Aceasta metoda instantiaza un Interpretor - ce va executa comenzi,
            dupa care, pana la primirea comenzii logout, primeste o comanda,
            Interpretorul o executa si returneaza un rezultat - pe care il si
            trimite inapoi.
        """

        interpreter = Interpreter(cwd="/")

        interpreter.add_internal_command("logout", self.close_connection)

        session_start_time = datetime.now()

        while True:

            command_line = self.recv_object()

            if command_line is None:
                self.close_connection()
                self.log("Connection Failed after {}."
                         " on Receive Command: Reason: {}.".format(
                             str(datetime.now() - session_start_time),
                             self.get_last_error_message))
                return None

            logout_command = command_line.get_command() == "logout"

            result = interpreter.execute_command(command_line)

            if logout_command:
                self.log("Connection Successfully Terminated."
                         " Session duration {}.".format(
                             str(datetime.now() - session_start_time)))
                break

            if not self.send_object(result):
                self.close_connection()
                self.log("Connection Failed after {}."
                         " on Send Result: Reason: {}.".format(
                             str(datetime.now() - session_start_time),
                             self.get_last_error_message))
                return None

    def close_connection(self):

        """ Aceasta metoda inchide conexiunea cu rsc-master. """

        self.connection.close()
        self.connection = None

    def _send(self, message):

        """ Aceasta metoda trimite pe socket buffer-ul message. (NJ) """

        try:
            self.connection.send(message)
        except socket.error as error_message:
            self._last_error_message = error_message
            return False

        return True

    def _recv(self, buffer_size=1024):

        """
            Aceasta metoda returneaza buffer_size octeti primiti pe socket.
            (Nivelul de Jos)
        """

        try:
            return self.connection.recv(buffer_size)
        except socket.timeout as ex:
            self._last_error_message = ex
        except socket.error as error_message:
            self._last_error_message = error_message

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


class BlackList(object):

    """
        Instantele acestei clase reprezinta liste negre (blacklists)
        de Adrese IP.
        Scopul este de a refuza conexiunile de la Adresele IP ce au depasit
        un numar de incercari de a se conecta fara succes,
        in ultimele <timeout> minute.
    """

    def __init__(self, tries=3, timeout=30):

        self.timeout = timedelta(minutes=timeout)
        self.tries = tries
        self.black_list = {}

    def check(self, ip_address):

        """
            Aceasta metoda returneaza:
            True, daca de la <ip_address> au fost mai putin de <tries> cereri
            de conectare sau exact 3 cereri dar in mai mult de <timeout> min;
            False, altfel.
        """

        if ip_address not in self.black_list:
            self.black_list[ip_address] = [1, datetime.now()]
            return True

        if self.black_list[ip_address][0] < self.tries:
            self.black_list[ip_address][0] += 1
            self.black_list[ip_address][1] = datetime.now()
            return True

        if datetime.now() - self.black_list[ip_address][1] > self.timeout:
            self.black_list[ip_address][1] = datetime.now()
            return True

        return False

    def delete_entry(self, ip_address):

        """
            Aceasta metoda sterge, daca exista, intrarea <ip_address>.
        """

        if ip_address in self.black_list:
            del self.black_list[ip_address]


class Logger(object):

    """
        Instantele acestei clase rezulta log-files (fisiere-jurnal).
    """

    def __init__(self):

        self.filename = "rsc.log"

    def log(self, log_message):

        """
            Aceasta metoda adauga un mesaj in fisierul de jurnalizare.
            Daca fisierul nu exista, este creat si ii este adaugat un titlu.
        """

        title = ""

        if not os.path.exists(os.path.join(self.filename)):
            title = "    RSC Log File (created: {})\n\n\n".format(
                str(datetime.now()))

        with open(self.filename, 'a') as logfile:
            if title != "":
                logfile.write(title)
            logfile.write("[{}] {}\n".format(str(datetime.now()), log_message))

    def clear(self):

        """ Aceasta metoda curata fisierul de jurnalizare. """

        with open(self.filename, 'w') as logfile:
            logfile.write("    RSC Log File (created: {})\n\n\n".format(
                str(datetime.now())))


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

    def __init__(self, stdout, stderr):

        self.stdout = stdout
        self.stderr = stderr

    def get_stdout(self):

        """ Aceasta metoda returneaza continutul iesirii standard. """

        return self.stdout

    def get_stderr(self):

        """ Aceasta metoda returneaza continutul iesirii pentru erori. """

        return self.stderr


class Interpreter(object):

    """
        Instantele acestei clase reprezinta interpretoare ce executa comenzi -
        - obiecte CommandLine, si returneaza rezultatul executiei - obiecte
        Result, pornind de la un director - cwd.
    """

    def __init__(self, cwd, shell=True):

        self.cwd = cwd
        self.shell = shell

        self.internal_commands = {"cd": self.cd_command,
                                  "get-cwd": self.get_rcwd}

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
            return Result(None, None)

        if len(args) > 1:
            return Result(None, "cd: Too much arguments!")

        result = self.execute(command_line)

        if not result.get_stderr():
            self.cwd = os.path.normpath(os.path.join(self.cwd, args[0]))

        return result

    def get_rcwd(self):

        """ Aceasta metoda returneaza cwd incapsulat in Result. """

        return Result(self.get_cwd(), None)
