"""
primeste o lista cu elemente numerice
si returneaza elem nu este duplicat.
"""

def history(mesaj):
    """
    :param istoric: istoric is the list of elements
    :return: the unique element from the list
    """
    unique = mesaj[0]
    for i in xrange(1, len(mesaj)):
        unique = unique ^ mesaj[i]
    return unique

if __name__ == "__main__":
    history([1, 2, 3, 2, 1])
    history([1, 1, 1, 2, 2])
