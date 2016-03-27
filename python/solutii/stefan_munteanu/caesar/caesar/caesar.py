"""�mp�ratul a primit serie de mesaje importante pe care este
important s� le descifreze c�t mai repede.
Din p�cate mesagerul nu a apucat s� �i spun� �mp�ratul care au fost
cheile alese pentru fiecare mesaj ?i tu ai fost ales s� descifrezi
misterul.
Informa?ii:
    �n criptografie, cifrul lui Caesar este o metod� simpl� de a cripta
un mesaj prin �nlocuirea fiec�rei litere cu litera de pe pozi?ia aflat�
la un n pa?i de ea �n alfabet (unde este n este un num�r �ntreg cunoscut
"""
# pylint: disable=unused-argument

from __future__ import print_function

def first_word(word):
# find ave caesar, or any other key
    word.lower()
    return ord(word[0]) % 97 

def decripteaza_mesajul(mesaj):
    """Func?ia va primi un mesaj criptat folosind cifrul lui Caesar ?i
    va �ncearca s� �l decripteze.
    """
    words = mesaj.split('.,')
    key = first_word(words[0])
    unlocked = ' '
    for i in mesaj.lower():
        NumberOfSteps = ord(' ')
        if i.isalpha():
            NumberOfSteps = (ord(i)-key)
        if (not chr(NumberOfSteps).isalpha() and chr(NumberOfSteps) != ' ')\
                or (chr(NumberOfSteps).isupper()):
            NumberOfSteps = NumberOfSteps + 26
        unlocked = unlocked + chr(NumberOfSteps)
    print(unlocked)


def main():
    try:
        fisier = open("mesaje.secret", "r")
        mesaje = fisier.read()
        fisier.close()
    except IOError:
        print("Nu am putut ob?ine mesajele.")
        return

    for mesaj in mesaje.splitlines():
        decripteaza_mesajul(mesaj)

if __name__ == "__main__":
    main()
