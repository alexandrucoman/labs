"""Update conda packages on binstars with latest versions"""
from __future__ import print_function

import hashlib
import json
import os
import subprocess
import time
import six

ATTEMPTS = 3
RETRY_INTERVAL = 0.1
CHECKS = {
    ".py": (["pylint", "-rn"], "flake8", "pep8"),
    ".sh": ("shellcheck", "bashate"),
}
CONFIG = {"whitelist": set()}
CONFIG_PATH = os.path.expanduser("~/.build/config.yml")


def _load():
    """Load the previous state of the repository."""
    if not os.path.exists(CONFIG_PATH):
        print("[x] No config file available: %s" % CONFIG_PATH)
        return

    with open(CONFIG_PATH) as file_handle:
        try:
            CONFIG.update(json.load(file_handle))
        except ValueError:
            print("[x] The config file is invalid.")


def _save():
    """Save the current state of the repository."""
    if not os.path.exists(os.path.dirname(CONFIG_PATH)):
        os.makedirs(os.path.dirname(CONFIG_PATH))

    print("[i] Saving the current state to: %s" % CONFIG_PATH)
    with open(CONFIG_PATH, "w") as file_handle:
        json.dump(CONFIG, file_handle)


def _sha1(path):
    """Compute SHA1 hash for the received file."""
    sha1_hash = hashlib.sha1()
    with open(path) as file_handle:
        while True:
            chunk = file_handle.read(2048)
            sha1_hash.update(chunk)
            if not chunk:
                break
    return sha1_hash.hexdigest()


def execute(command, **kwargs):
    """Helper method to shell out and execute a command through subprocess.

    :param attempts:        How many times to retry running the command.
    :param binary:          On Python 3, return stdout and stderr as bytes if
                            binary is True, as Unicode otherwise.
    :param check_exit_code: Single bool, int, or list of allowed exit
                            codes.  Defaults to [0].  Raise
                            :class:`CalledProcessError` unless
                            program exits with one of these code.
    :param command:         The command passed to the subprocess.Popen.
    :param cwd:             Set the current working directory
    :param env_variables:   Environment variables and their values that
                            will be set for the process.
    :param retry_interval:  Interval between execute attempts, in seconds
    :param shell:           whether or not there should be a shell used to
                            execute this command.

    :raises:                :class:`subprocess.CalledProcessError`
    """
    # pylint: disable=too-many-locals

    attempts = kwargs.pop("attempts", ATTEMPTS)
    binary = kwargs.pop('binary', False)
    check_exit_code = kwargs.pop('check_exit_code', [0])
    cwd = kwargs.pop('cwd', None)
    env_variables = kwargs.pop("env_variables", None)
    retry_interval = kwargs.pop("retry_interval", RETRY_INTERVAL)
    shell = kwargs.pop("shell", False)

    if cwd and not os.path.isdir(cwd):
        print("[w] Invalid value for cwd: {cwd}".format(cwd=cwd))
        cwd = None

    command = [str(argument) for argument in command]
    ignore_exit_code = False

    if isinstance(check_exit_code, bool):
        ignore_exit_code = not check_exit_code
        check_exit_code = [0]
    elif isinstance(check_exit_code, int):
        check_exit_code = [check_exit_code]

    while attempts > 0:
        attempts = attempts - 1
        try:
            process = subprocess.Popen(command,
                                       stdin=subprocess.PIPE,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE, shell=shell,
                                       cwd=cwd, env=env_variables)
            result = process.communicate()
            return_code = process.returncode

            if six.PY3 and not binary and result is not None:
                # pylint: disable=no-member

                # Decode from the locale using using the surrogate escape error
                # handler (decoding cannot fail)
                (stdout, stderr) = result
                stdout = os.fsdecode(stdout)
                stderr = os.fsdecode(stderr)
            else:
                stdout, stderr = result

            if not ignore_exit_code and return_code not in check_exit_code:
                raise subprocess.CalledProcessError(returncode=return_code,
                                                    cmd=command,
                                                    output=(stdout, stderr))
            else:
                return (stdout, stderr)
        except subprocess.CalledProcessError:
            if attempts:
                time.sleep(retry_interval)
            else:
                raise


def scripts(root):
    """Generator for all the scripts in the repository."""
    files_queue = [root]
    while files_queue:
        root = files_queue.pop()
        for files in os.listdir(root):
            if files in ('.', '..'):
                continue
            file_path = os.path.join(root, files)
            if os.path.isfile(file_path):
                yield file_path
            else:
                files_queue.append(file_path)


def main():
    """Check if all the scripts meet the requirements."""
    exit_code = 0
    whitelist = []
    _load()

    for script in scripts(os.path.curdir):
        script_type = script[-3:]
        if script_type not in CHECKS:
            continue

        file_hash = _sha1(script)
        if file_hash in CONFIG["whitelist"]:
            whitelist.append(file_hash)
            continue

        for checker in CHECKS[script_type]:
            if isinstance(checker, list):
                command = [argument for argument in checker]
            else:
                command = [checker]
            command.append(script)

            print("Running: ", " ".join(command), sep="", end="")
            try:
                execute(command, check_exit_code=0)
            except subprocess.CalledProcessError as exc:
                print(" [Failed]")
                print(exc.output[0])
                print(exc.output[1])
                exit_code = -1
            else:
                whitelist.append(file_hash)
                print(" [Done]")

    CONFIG["whitelist"] = whitelist
    _save()
    exit(exit_code)


if __name__ == "__main__":
    main()
