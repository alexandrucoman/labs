<<<<<<< HEAD


=======
"""Povestea povestilor
"""
>>>>>>> a9714af6db17cca0d838819c69e85ca13a810dbf
from __future__ import print_function

def first_word(word):
    """find ave caesar, or any other key
    """
    word.lower()
    return ord(word[0]) % 97

def decripteaza_mesajul(mesaj):
    """Fucntie cript.
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
    """The main function
    """
    try:
        fisier = open("mesaje.secret", "r")
        mesaje = fisier.read()
        fisier.close()
    except IOError:
        print("Nu am putut obtine mesajele.")
        return

    for mesaj in mesaje.splitlines():
        decripteaza_mesajul(mesaj)

if __name__ == "__main__":
    main()
