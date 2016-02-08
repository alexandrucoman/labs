Tuxy dorește să împlementeze un nou paint pentru consolă.

În timpul dezvoltării proiectului s-a izbit de o problemă
pe care nu o poate rezolva singur și a apelat la ajutorul tău.

Aplicația ține un istoric al tuturor mișcărilor pe care le-a
făcut utlizatorul în fișierul istoric.tuxy

Exemplu de istoric.tuxy:

```
STANGA 2
JOS 2
DREAPTA 5
```

Fișierul de mai sus ne spune că utilizatorul a mutat cursorul
2 căsuțe la stânga după care 2 căsuțe in jos iar ultima acțiune
a fost să poziționeze cursorul cu 5 căsuțe în dreapta față de
ultima poziție.

El dorește un utilitar care să îi spună care este distanța dintre
punctul de origine (0, 0) și poziția curentă a cursorului.

---

<<<<<<< HEAD:python/exercitii/paint/README.md
Tuxy dorește să împlementeze un nou paint pentru consolă.
=======
def distanta():
    x = 0
    y = 0
    raw = open("istoric.tuxy").read().splitlines()
    direction = ""
    amount = 0
    for item in raw:

        direction = item.split()[0]
        amount = int(item.split()[1])

        if direction == "SUS":
            x += amount
        elif direction == "JOS":
            x -= amount
        elif direction == "STANGA":
            y -= amount
        elif direction == "DREAPTA":
            y += amount
        else:
            print "Error, history invalid"

    print "Final X = " + str(x)
    print "Final Y = " + str(y)

    distance = (x * x + y * y) ** 0.5
    print "Distanta: " + str(distance)
>>>>>>> 683b5eb7272985582f89429a66d99fdc8f1f4c3f:exercitii/paint/cursor.py

În timpul dezvoltării proiectului s-a izbit de o problemă
pe care nu o poate rezolva singur și a apelat la ajutorul tău.

El dorește să adauge o unealtă care să permită umplerea unei
forme închise.
