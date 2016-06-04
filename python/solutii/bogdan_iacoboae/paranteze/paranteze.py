__author__ = 'kali'


def verifica_expresia(paranteze):
    lista = []
    for index in paranteze:
        if index == '(' or index == '[':
            lista.append(index)
        elif len(lista) > 0:
            if index == ')' and lista[-1] == '(':
                lista.pop()
            elif index == ']' and lista[-1] == '[':
                lista.pop()
            else:
                return False
        else:
            return False
    return True

if __name__ == "__main__":
    input = raw_input("Give me your parenthesis : ")
    if verifica_expresia(input) == True:
        print "Parantezele au fost puse bine"
    else:
        print "Parantezele nu au fost puse bine"
