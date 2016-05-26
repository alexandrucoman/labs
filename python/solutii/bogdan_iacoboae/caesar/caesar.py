# coding=utf-8
# from __future__ import print_function


def afla_pasul(mesaj):
    first_letter = 'a'
    my_letter = mesaj[0]
    return ord(my_letter) - ord(first_letter)


def real_letter(character, key):
    if character.isalpha():
        character = ord(character)-key
        if character<ord('a'):
            character=ord('z')-abs(ord('a')-character)+1 #122 - abs(97 -  [unicode character]) + 1
        return chr(character)
    else:
        return character

def decripteaza_mesajul(mesaj,fisier):
    key = afla_pasul(mesaj)
    puncte = 0.
    for index in mesaj:
        if index==".":
            if puncte == 1 :
                print ".\n"
                fisier.write("\n")
            else:
                puncte = puncte +1
                print ".",
                fisier.write(".")
        else:
            print real_letter(index,key),
            fisier.write(real_letter(index,key))



def main():
    """ Main function docstring """
    try:
        fisier = open("mesaje.secret", "r")
        towrite = open("mesaje.decodat", "w")
        mesaje = fisier.read()
        fisier.close()
    except IOError:
        print("Nu am putut obtine mesajele.")
        return

    for mesaj in mesaje.splitlines():
        decripteaza_mesajul(mesaj,towrite)

if __name__ == "__main__":
    main()