#!/usr/bin/env python
# *-* coding: UTF-8 *-*
import math
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


def distanta():
    try:
        fisier = open("../../date_intrare/istoric.tuxy", "r")
        mesaje = fisier.read()
        fisier.close()
    except IOError:
        print("Nu am putut obține mesajele.")
        return
    x = 0
    y = 0
    for mesaj in mesaje.splitlines():
        linie = mesaj.split(" ");
        if linie[0] == "STANGA":
            x -= int(linie[1])
        elif linie[0] == "DREAPTA":
            x += int(linie[1])
        elif linie[0] == "SUS":
            y += int(linie[1])
        elif linie[0] == "JOS":
            y -= int(linie[1])
    distanta = math.sqrt(x*x + y*y)
    print "distanta = " + str(distanta)
	

if __name__ == "__main__":
    distanta()
