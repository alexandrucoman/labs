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
    n=ord(mesaj[0])-ord("a")
    mesajDecriptat=list(mesaj)
    for i in range(0,len(mesaj)):
        if ord(mesajDecriptat[i])-n<97:
            print("mai mic ca a")
        if (mesajDecriptat[i]==' ') | (mesajDecriptat[i]=='.') | (mesajDecriptat[i]==','):
            pass
        else: mesajDecriptat[i]=chr(ord(mesajDecriptat[i])-n)
    mesajString=''.join(mesajDecriptat)
    print(mesajString)
    pass


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
