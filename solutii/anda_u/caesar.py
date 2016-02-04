#!/usr/bin/env python
# *-* coding: UTF-8 *-*

"""Împăratul a primit serie de mesaje importante pe care este
important să le descifreze cât mai repede.
Din păcate mesagerul nu a apucat să îi spună împăratul care au fost
cheile alese pentru fiecare mesaj ?i tu ai fost ales să descifrezi
misterul.
Informa?ii:
    În criptografie, cifrul lui Caesar este o metodă simplă de a cripta
un mesaj prin înlocuirea fiecărei litere cu litera de pe pozi?ia aflată
la un n pa?i de ea în alfabet (unde este n este un număr întreg cunoscut
"""
def decripteaza(mesaj,n):
    b=['a']
    for index in range(0,len(mesaj)):
        if mesaj[index].isalpha():
            if(ord(mesaj[index])-n)>=97 and (ord(mesaj[index])-n)<=122:
                litera=chr(ord(mesaj[index])-n)
            else :
                litera=chr(122-(n-(ord(mesaj[index])-97)-1))
            b.append(litera)
        else:
            b.append(mesaj[index])
    b=b[1:len(b)]
    b="".join(b)
    if "caesar" in b:
        print (b)
    else:
        decripteaza(mesaj,n+1)


def main():
    try:
        fisier = open("mesaje.secret", "r")
        mesaje = fisier.read()
        fisier.close()
    except IOError:
        print("Nu am putut ob?ine mesajele.")
        return

    for mesaj in mesaje.splitlines():
        decripteaza(mesaj,1)

if __name__ == "__main__":
    main()
