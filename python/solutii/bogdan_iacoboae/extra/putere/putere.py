__author__ = 'kali'


def power(number):
    binar = bin(number)[2:]
    # binar = "{0:b}".format(number)
    if binar.count("1") == 1:
        print "Este putere a lui doi"
    else:
        print "Nu este putere a lui doi"

if __name__ == "__main__":
    input = int(raw_input("Gimme the number: "))
    power(input)
