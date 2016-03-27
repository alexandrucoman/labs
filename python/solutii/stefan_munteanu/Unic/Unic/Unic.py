def history(t):
    unique = t[0]
    for i in xrange(1, len(istoric)):
        unique =unique^t[i]
    return unique

