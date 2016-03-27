def history(mesaj):
    unique = t[0]
    for i in xrange(1, len(istoric)):
        unique = unique^mesaj[i]
    return unique
