Tuxy cauta in fiecare zi cate o problema de matematica complet noua pentru el.

Rezolvand problema 101, a observat ca are nevoie de cateva formule mai vechi.
A revenit la fisierul lui de teoreme "teoreme1.txt" pentru ajutor. S-a bucurat 
ca a reusit sa il gaseasca la timp ,fisierul fiind in /tmp/ciorne. 
Uitandu-se prin el,a observat ca folosea o regula cand scria teoreme noi:

```
[Index].[Spatiu][Spatiu][Numele Teoremei]
[Numele scurt]
[Rand nou]
[Rand nou]
[Teorema]
[Rand nou]
[Rand nou]
```

Exemplu: 

```
1.  The Irrationality of the Square Root of 2  
    SQRT_2_IRRATIONAL 
   
    
 |- ~rational(sqrt(&2))
```

---

Stiind limbajul de programare python si fiind un fan al liniei de comanda,
el doreste sa implementeze un utilitar inteligent de cautat formule. 
Functionalitatile care doreste sa le implementeze sunt:

1. cautare indiferent de caz (ex. 'a'=='A' ) [-i]
2. cautare exacta ( nu ia in considere parti ale cuvintelor) [-e]
3. cautare si inlocuire a sirurilor de caractere [-s]
    Exemplu: python utilitar.py -s "CARD" "CARDINAL"
    fiecare sir "CARD" a fost inlocuit cu "CARDINAL"
4. numararea aparitiilor unui sir de caractere [-n]
5. cautare recursiva a fisierelor prin director [-r]
6. introducerea parametrilor din linia de comanda:
    Exemplu: python utilitar.py -in "CARD" teoreme1.txt
    sirul "CARD" (insensitiv) apare de 44 de ori in teoreme1.txt
7. afisarea unui mesaj de ajutor daca parametrii introdusi sunt gresiti

Notă: Prin inteligent se refera ca v-a returna tot ce stie despre teorema(nume,
nume scurt siteorema). Daca sirul de caractere cautat apare in mai multe
teoreme, utilitarul returneaza doar numele complet si cel scurt al teoremelor.

---

Oare cum a implementat Tuxy acest utilitar?

Posibila documentatie:

- http://linux.die.net/man/1/grep
- http://git.savannah.gnu.org/cgit/grep.git/snapshot/grep-2.22.tar.gz
- din cadrul arhivei amintite anterior, folderul "src"
- https://github.com/heyhuyen/python-grep

---

Nu a durat mult pana cand Tuxy nu a fost multumit de utilitarul creat anterior.
Acum el doreste cateva functionalitati in plus:

1. Afisarea fisierului si liniei in care se afla textul cautat [implicit]
    ex: [nume fisier]:[numar linie]:[linia cu textul cautat]
2. afisarea colorata a termenului cautat in cadrul liniei [-c]
3. implementarea operatorilor de expresii regulate:

- `*`: http://web.mit.edu/gnu/doc/html/regex_toc.html#SEC12
- `?`: http://web.mit.edu/gnu/doc/html/regex_toc.html#SEC14
- `.`: http://web.mit.edu/gnu/doc/html/regex_toc.html#SEC9
- `+`: http://web.mit.edu/gnu/doc/html/regex_toc.html#SEC13
- `|`: http://web.mit.edu/gnu/doc/html/regex_toc.html#SEC16
- `-`: http://web.mit.edu/gnu/doc/html/regex_toc.html#SEC19
- `^`: http://web.mit.edu/gnu/doc/html/regex_toc.html#SEC23
- `$`: http://web.mit.edu/gnu/doc/html/regex_toc.html#SEC24

4. afisarea top 5 cele mai folosite cuvinte din fisierul "text.txt" [-t]
Indicatie: se va utiliza un dictionar pentru a memora topul:
    
```python
top5 = {
    '1': 'Tuxy',
    '2': 'the',
    '3': 'average',
    '4': 'rocket',
    '5': 'surgeon'
}
```