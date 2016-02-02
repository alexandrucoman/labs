#!/usr/bin/env python
# *-* coding: UTF-8 *-*

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
    x = 0
    y = 0
    istoric = open("istoric.tuxy", 'r')
    com_string = istoric.read()
    comenzi = com_string.strip().split('\n')
    for comanda in comenzi:
        directia = comanda.strip().split(' ')[0].lower()
        distanta = int(comanda.strip().split(' ')[1])
        if directia == "jos":
            y-=distanta
        if directia == "sus":
            y+=distanta
        if directia == "STaNGA".lower():
            x-=distanta
        if directia == "dreapta":
            x+=distanta
    distance = (x*x+y*y)**0.5
    print distance
    pass


if __name__ == "__main__":
    distanta()
