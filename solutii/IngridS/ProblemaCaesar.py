"""Solutia corecta a problemei Caesar"""

def decripteaza(mesaj):
    """Decriptarea mesajului"""
    mesaj_decriptat = []
    for key in range(26):
        for caracter in mesaj.lower():
            if caracter.isalpha():
                aux = (ord(caracter)-key)
                if aux >= 97 and aux <= 122:
                    caracter = chr(aux)
                else:
                    caracter = chr(122-(97-aux))
            mesaj_decriptat.append(caracter)
        mesaj_decriptat_final = ''.join(mesaj_decriptat)
        if "caesar" in mesaj_decriptat_final:
            print mesaj_decriptat_final
def main():
    """Apelarea functiei"""
    try:
        fisier = open("mesaje.secret", "r")
        mesaje = fisier.read()
        fisier.close()
    except IOError:
        print "Nu am putut obtine mesajele"
        return
    for mesaj in mesaje.splitlines():
        decripteaza(mesaj)
if __name__ == "__main__":
    main()


