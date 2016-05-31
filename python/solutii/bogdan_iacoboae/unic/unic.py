
def gaseste_unic(istoric):
    unic = istoric.pop(0)
    for index in istoric:
        unic ^= index
    return unic


if __name__ == "__main__":
    # lista = [1, 2, 3, 2, 1]
    lista = [1, 1, 1, 2, 2]
    print "Lista id-uri cercetatori: ",
    for index in lista :
        print index,
    print""
    print "Cercetatorul cu id-ul %s este cercetatorul care sta peste program" % (gaseste_unic(lista))

