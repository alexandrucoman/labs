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

letters = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
print len(letters)
print letters[26]

def shiftLetter(l, n):
    if l.isalpha():
        for i in range(26):
            if l == letters[i]:
                break
        return letters[i+n]
    else:
        return l

def decripteaza(mesaj, n):
    newMsg = ""
    for i in range (len(mesaj)):
        newMsg += shiftLetter(mesaj[i], n)
    if "ave" in newMsg:
        print newMsg


def main():
    try:
        fisier = open("mesaje.secret", "r")
        mesaje = fisier.read()
        fisier.close()
    except IOError:
        print("Nu am putut obține mesajele.")
        return

    print mesaje.splitlines()

    for mesaj in mesaje.splitlines():
        for i in range(26):
            decripteaza(mesaj, i)

if __name__ == "__main__":
    main()
