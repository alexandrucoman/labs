Tuxy nu dorește să uite de nici un eveniment important pentru el
sau pentru cineva apropiat lui așa că își dorește un sistem care
să îi permită gestiunea acestor evenimente.

Script-ul `executor` va primi o sarcină generată / pregătită de
către script-ul `scheduler` și va încerca să îndeplinească toate
cerințele ce sunt încapsulate în aceasta.

Script-ul `manager` îi oferă lui Tuxy posibilitatea de a adăuga
modifica sau șterge un eveniment.

Script-ul `scheduler.py` se va ocupa cu planificarea unei acțiuni
ce trebuie să fie executată de script-ul `executor.py`.

Câteva exemple acțiune ar putea fi:

```
29-03-2016-send-email
---
To: uxy@pinguinescu.ro
Subject: La mulți ani!
Content: Fie ca ...
```

```
29-03-2016-send-pigeon
---
To: Balconul cu o orhidee
Paper: A0
Content: Fie ca ...
```

```
29-03-2016-send-sms
---
To: +04 777 777 777 7
Sender: Sunt eu
Content: Fie ca ...
```

```
29-03-2016-send-drone
---
To: 47.1282901,27.6115742,17
Sender: doGenmud
Content: lusimirt tnuS
```
