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
    intrare=open("istoric.tuxy",'r')
    istoric=intrare.read()
    intrare.close()
    y_pos=0
    x_pos=0
    for miscare in istoric.splitlines():
        if miscare[0:2]=='SU':
            y_pos+=ord(miscare[4])-ord('0')
        elif miscare[0:2]=='JO':
            y_pos-=ord(miscare[4])-ord('0')
        elif miscare[0:2]=='ST':
            x_pos-=ord(miscare[4])-ord('0')
        elif miscare[0:2]=='DR':
            x_pos+=ord(miscare[4])-ord('0')
    distance=(x_pos**2+y_pos**2)**0.5
    print('%.2f' %distance)


if __name__ == "__main__":
    distanta()
