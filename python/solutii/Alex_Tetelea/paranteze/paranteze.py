"""Verificarea corectitudinei"""


def este_corect(expresie):
    """Functia verifica daca parantezele sunt puse corect
    :param expresie:
    """
    expp_len = len(expresie)
    while True:
        for i in xrange(len(expresie) - 1):
            if expresie[i] == '[' and expresie[i + 1] == ']' \
                    or expresie[i] == '{' and expresie[i + 1] == '}' \
                    or expresie[i] == '(' and expresie[i + 1] == ')':
                expresie = expresie[:i] + expresie[(i + 2):]
                break
        if len(expresie) < 1:
            break
        if expp_len == len(expresie):
            return False
        expp_len = len(expresie)

    if len(expresie) > 0:
        return False
    else:
        return True


if __name__ == "__main__":
    try:
        assert este_corect("[()[]]"), "Probleme la expresia 1"
        assert este_corect("()()[][]"), "Probleme la expresia 2"
        assert este_corect("([([])])"), "Probleme la expresia 3"
        assert not este_corect("[)()()()"), "Probleme la expresia 4"
        assert not este_corect("][[()][]"), "Probleme la expresia 5"
        assert not este_corect("([()]))"), "Probleme la expresia 6"
        assert not este_corect("([)]"), "Probleme la expresia 7"
    except AssertionError:
        print "Ati avut o eroare"
