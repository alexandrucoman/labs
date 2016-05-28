"""Find the unique value"""


def gaseste2(istoric):
    """Pastreaza rezultatele direct in lista
    :param istoric:
    """
    for i in xrange(len(istoric) - 1):
        istoric[i + 1] ^= istoric[i]
    return istoric[len(istoric) - 1]


if __name__ == "__main__":
    try:
        assert gaseste2([1, 2, 3, 2, 1]) == 3
    except AssertionError:
        print "Nu sunt amplasate corect"
    try:
        assert gaseste2([1, 1, 1, 2, 2]) == 1
    except AssertionError:
        print "Nu sunt amplasate corect"
