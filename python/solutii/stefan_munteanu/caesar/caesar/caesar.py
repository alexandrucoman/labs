<<<<<<< fb9f1b711dd83947ca8d071746fe22677b266648
"""Rezolv caesar"""

=======
<<<<<<< HEAD
<<<<<<< HEAD
=======

=======
"""Rezolv caesar"""
>>>>>>> a9b5cf5... Fix7

>>>>>>> 2cd989b... Fix7
>>>>>>> caesar
from __future__ import print_function


def first_word(word):
<<<<<<< fb9f1b711dd83947ca8d071746fe22677b266648
    """find ave caesar, or any other key
    """
    word.lower()
    return ord(word[0]) % 97


def decripteaza_mesajul(mesaj):
    """Fucntie cript."""

=======
    """find ave caesar, or any other key"""
    word.lower()
    return ord(word[0]) % 97

<<<<<<< HEAD
	
def decripteaza_mesajul(mesaj):
    """Fucntie cript."""
=======

def decripteaza_mesajul(mesaj):
    """Fucntie cript."""
<<<<<<< HEAD
    
>>>>>>> 2cd989b... Fix7
=======

>>>>>>> a9b5cf5... Fix7
>>>>>>> caesar
    words = mesaj.split('.,')
    key = first_word(words[0])
    unlocked = ' '
    for i in mesaj.lower():
        number_of_steps = ord(' ')
        if i.isalpha():
            number_of_steps = (ord(i)-key)
        if ((not chr(number_of_steps).isalpha() and
             chr(number_of_steps) != ' ') or
             chr(number_of_steps).isupper()):
                number_of_steps = number_of_steps + 26
        unlocked = unlocked + chr(number_of_steps)
    print(unlocked)

<<<<<<< fb9f1b711dd83947ca8d071746fe22677b266648

def main():
    """The main function."""

=======
<<<<<<< HEAD
	
def main():
    """The main function"""
=======

def main():
    """The main function."""
<<<<<<< HEAD
    
>>>>>>> 2cd989b... Fix7
=======

>>>>>>> d973dd6... Fix7
>>>>>>> caesar
    try:
        fisier = open("mesaje.secret", "r")
        mesaje = fisier.read()
        fisier.close()
    except IOError:
        print("Nu am putut obtine mesajele.")
        return

    for mesaj in mesaje.splitlines():
        decripteaza_mesajul(mesaj)

<<<<<<< fb9f1b711dd83947ca8d071746fe22677b266648
if __name__ == "__main__":
=======
		
if __name__ == "__main__":
<<<<<<< HEAD
    """main"""
=======
>>>>>>> a9714af... Fix7
>>>>>>> caesar
    main()
