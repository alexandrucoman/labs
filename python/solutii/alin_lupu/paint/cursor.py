"""Tuxy dorește să împlementeze un nou paint pentru consolă.

În timpul dezvoltării proiectului s-a izbit de o problemă
pe care nu o poate rezolva singur și a apelat la ajutorul tău.

Aplicația ține un istoric al tuturor mișcărilor pe care le-a
făcut utlizatorul în fișierul istoric.tuxy

Exemplu de istoric.tuxy:

    STÂNGA 2
    JOS 2
    DREAPTA 5

Fișierul de mai sus ne spune că utilizatorul a mutat cursorul
2 căsuțe la stânga după care 2 căsuțe in jos iar ultima acțiune
a fost să poziționeze cursorul cu 5 căsuțe în dreapta față de
ultima poziție.

El dorește un utilitar care să îi spună care este distanța dintre
punctul de origine (0, 0) și poziția curentă a cursorului.
"""

from __future__ import print_function
from math import sqrt


def distanta():
    """
    Calculează distanța dintre origine și poziția curentă.
    Funcția citește conținutul fișierului istoric.tuxy și
    calculează distanța dintre punctul de origine și poziția
    curentă a cursorului.
    """
    try:
        f_in = open("../../../date_intrare/istoric.tuxy", "r")
        instructions = f_in.read().splitlines()
        f_in.close()
        
        x, y = 0, 0
        for instruction in instructions:
            commands = instruction.split(' ')
            if commands[0] and commands[0] in ["SUS", "JOS", "STANGA", "DREAPTA"]:
                if commands[0] == "SUS": y += int(commands[1])
                if commands[0] == "JOS": y -= int(commands[1])
                if commands[0] == "STANGA": x -= int(commands[1])
                if commands[0] == "DREAPTA": x += int(commands[1])
            else:
                return 0
    except IOError:
        print("FileNotFound")
        return
    return sqrt(pow(0 - x, 2) + pow(0 - y, 2))


if __name__ == "__main__":
    print(distanta())
