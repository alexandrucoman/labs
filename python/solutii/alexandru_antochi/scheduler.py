#!/usr/bin/env python
# *-* coding: UTF-8 *-*

"""
Tuxy nu dorește să uite de nici un eveniment important pentru el
sau pentru cineva apropiat lui așa că își dorește un sistem care
să îi permită gestiunea acestor evenimente.

Script-ul `scheduler.py` se va ocupa cu planificarea unei acțiuni
ce trebuie să fie executată de script-ul `executor.py`.

Un exemplu de acțiune ar putea fi:

29-03-2016-send-email
---
To: uxy@pinguinescu.ro
Subject: La mulți ani!
Content: Fie ca ...
"""

from datetime import datetime
import os

schedule = open("schedule.dat", "w+")


def comparedate(b_day):
    """Compara data de astazi cu data de nastere b_day"""
    if int(b_day.split('/')[0]) == datetime.now().day:
        if int(b_day.split('/')[1]) == datetime.now().month:
            return True
    return False


def options(person):
    """Functia iti cere sa alegi cum sa trimiti msajul"""
    print("\nCum vrei sa-i urezi la multi ani lui\033[94m %s\033[0m?" % (person.split('$')[0]))
    print("Mesajul va fi trimis la %s, contactul adaugat de utilizator." % (person.split('$')[2]))
    option = input("1 - trimite e-mail \n2 - trimite sms \n3 - sari peste\n")
    while int(option) < 1 or int(option) > 3:
        option = input("Optiune invalida, alege iar.\n")
    if int(option) == 3:
        print("%s nu va primi mesaj de La multi ani :(\n" % (person.split('$')[0]))
        return
    mesaj = input("Ce mesaj vrei sa ii trimti lui %s? \n" % (person.split('$')[0]))
    if int(option) == 1:
        schedule.write(person.split('$')[2] + '$mail$' + mesaj + "\n")
    elif int(option) == 2:
        schedule.write(person.split('$')[2] + '$sms$' + mesaj + "\n")


def scheduler():
    """Planifică evenimentele."""
    file = open("data.dat", "r").read()
    for person in file.splitlines():
        if comparedate(person.split('$')[1]):
            options(person)
    schedule.close()
    if os.stat("schedule.dat").st_size == 0:
        print("Astazi nu este ziua nimanui :(")
        print(datetime.now().month)


if __name__ == "__main__":
    scheduler()
