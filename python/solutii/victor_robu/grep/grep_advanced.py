#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""
Nu a durat mult pana cand Tuxy nu a fost multumit de utilitarul creat anterior.

Acum el doreste cateva functionalitati in plus:
    [1] Afisarea fisierului si liniei in care se afla textul cautat [implicit]
    ex: [nume fisier]:[numar linie]:[linia cu textul cautat]
    [2] afisarea colorata a termenului cautat in cadrul liniei [-c]
    [3] implementarea operatorilor de expresii regulate:
        *: http://web.mit.edu/gnu/doc/html/regex_toc.html#SEC12
        ?: http://web.mit.edu/gnu/doc/html/regex_toc.html#SEC14
        .: http://web.mit.edu/gnu/doc/html/regex_toc.html#SEC9
        +: http://web.mit.edu/gnu/doc/html/regex_toc.html#SEC13
        |: http://web.mit.edu/gnu/doc/html/regex_toc.html#SEC16
        -: http://web.mit.edu/gnu/doc/html/regex_toc.html#SEC19
        ^: http://web.mit.edu/gnu/doc/html/regex_toc.html#SEC23
        $: http://web.mit.edu/gnu/doc/html/regex_toc.html#SEC24
    [4] afisarea top 5 cele mai folosite cuvinte din fisierul "text.txt" [-t]
    Indicatie: se va utiliza un dictionar pentru a memora topul:
        ex: top5 = {
        '1': 'Tuxy',
        '2': 'the',
        '3': 'average',
        '4': 'rocket',
        '5': 'surgeon'
        }
"""
