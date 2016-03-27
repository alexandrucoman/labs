def history(mesaj):
    unique = mesaj[0]
    for i in xrange(1, len(mesaj)):
        unique =unique^mesaj[i]
    return unique

