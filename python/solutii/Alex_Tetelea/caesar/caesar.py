"""Solve Caesar Cipher"""


# coding=utf-8
def decripteaza(mesaj):
    """Decrypt Caesar Cipher
    :param mesaj:
    """
    for i in xrange(0, 27):
        mesaj2 = [chr(((((ord(litera) - ord("a")) - i) % 26) +
                       ord("a"))) for litera in mesaj]
        if "caesar" in ''.join(mesaj2) \
                and "ave" in ''.join(mesaj2):
            print(i)
            for j in range(len(mesaj)):
                if mesaj[j] == ' ':
                    mesaj2[j] = ' '
                if not mesaj2[j].isalpha():
                    mesaj2[j] = ' '
            print(mesaj2)


def main():
    """First executedfunction"""
    try:
        fisier = open("mesaje.secret", "r")
        mesaje = fisier.read()
        fisier.close()
    except IOError:
        print('Nu am putut obține mesajele.')
        return

    for mesaj in mesaje.splitlines():
        decripteaza(mesaj)


if __name__ == "__main__":
    main()
