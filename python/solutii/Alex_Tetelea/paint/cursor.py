"""Caclulate the distance between points"""


def distanta():
    """Functie care calculeaza distanta pana la un punct - de la origine"""
    var_x = 0
    var_y = 0
    istoric = open("istoric.tuxy", 'r')
    com_string = istoric.read()
    comenzi = com_string.strip().split('\n')
    for comanda in comenzi:
        directia = comanda.strip().split(' ')[0].lower()
        points = int(comanda.strip().split(' ')[1])
        if directia == r"jos":
            var_y -= points
        if directia == r"sus":
            var_y += points
        if directia == r"stanga".lower():
            var_x -= points
        if directia == r"dreapta":
            var_x += points
    distance = (var_x * var_x + var_y * var_y) ** 0.5
    print distance

if __name__ == "__main__":
    distanta()
