#!/usr/bin/env python
# *-* coding: UTF-8 *-*

"""Împăratul a primit serie de mesaje importante pe care este
important să le descifreze cât mai repede.

Din păcate mesagerul nu a apucat să îi spună împăratul care au fost
cheile alese pentru fiecare mesaj și tu ai fost ales să descifrezi
misterul.

Informații:
    În criptografie, cifrul lui Caesar este o metodă simplă de a cripta
un mesaj prin înlocuirea fiecărei litere cu litera de pe poziția aflată
la un n pași de ea în alfabet (unde este n este un număr întreg cunoscut
"""


def decripteaza(mesaj):
    mesaj2 = []
    for i in xrange(0,27):
        mesaj2 = [chr(((((ord(litera)-ord("a")) - i) % 26) + ord("a") )) for litera in mesaj ]
        if "caesar".lower() in ''.join(mesaj2).lower() and "ave" in ''.join(mesaj2).lower() :
            print i
            for j in xrange(len(mesaj)):
                if mesaj[j]==' ':
                    mesaj2[j] = ' '
                if not mesaj2[j].isalpha():
                    mesaj2[j] = ' '
            print mesaj2



def main():
    try:
        fisier = open("mesaje.secret", "r")
        mesaje = fisier.read()
        fisier.close()
    except IOError:
        print("Nu am putut obține mesajele.")
        return

    for mesaj in mesaje.splitlines():
        decripteaza(mesaj)

if __name__ == "__main__":
    main()
