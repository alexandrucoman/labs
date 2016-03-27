"""Împãratul a primit serie de mesaje importante pe care este
important sã le descifreze cât mai repede.
Din pãcate mesagerul nu a apucat sã îi spunã împãratul care au fost
cheile alese pentru fiecare mesaj ?i tu ai fost ales sã descifrezi
misterul.
Informa?ii:
    În criptografie, cifrul lui Caesar este o metodã simplã de a cripta
un mesaj prin înlocuirea fiecãrei litere cu litera de pe pozi?ia aflatã
la un n pa?i de ea în alfabet (unde este n este un numãr întreg cunoscut
"""
from __future__ import print_function

def first_word(word):
    """find ave caesar, or any other key
    """
    word.lower()
    return ord(word[0]) % 97

def decripteaza_mesajul(mesaj):
    """Func?ia va primi un mesaj criptat folosind cifrul lui Caesar ?i
    va încearca sã îl decripteze.
    """
    words = mesaj.split('.,')
    key = first_word(words[0])
    unlocked = ' '
    for i in mesaj.lower():
        number_of_steps = ord(' ')
        if i.isalpha():
            number_of_steps = (ord(i)-key)
        if (not chr(number_of_steps).isalpha() and chr(number_of_steps) != ' ')\
            or (chr(number_of_steps).isupper()):
            number_of_steps = number_of_steps + 26
        unlocked = unlocked + chr(number_of_steps)
    print(unlocked)

def main():
    """
    The main function
    """
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
    """
    main
    """
    main()
