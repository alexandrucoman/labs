#Limbajul Python

---

#Obiective

- Prezentarea limbajului Python
- Pregătirea mediului de lucru
- Familiarizarea cu limbajul
    - Tipuri de date (int, float, *long*, str)
    - Operatori
    - Comentarii
    - Structuri de date
        - Liste și Tuples
        - Referințe
        - Dictionare
    - Funcții built-in (print, input, *raw_input*, open)
    - Instrucțiuni condiționale (if - elif - else)
    - Instrucțiuni repetitive (for, while)

*Timp estimat: **80** de minute*

---

#Limbajul Python

---

#Implementări ale limbajului

- **CPython - [python.org](https://www.python.org/)**
- Jython - [jython.org](http://www.jython.org/)
- Python for .NET - [pythonnet.sourceforge.net](http://pythonnet.sourceforge.net/)
- IronPython - [ironpython.net](http://ironpython.net/)
- PyPy - [pypy.org](http://pypy.org/)

---

#Instalarea

Mai multe detalii pe link-urile de mai jos:

- **CPython** - [python.org/downloads/](https://www.python.org/downloads/)
- Jython - [jython.org/downloads.html](http://www.jython.org/downloads.html)
- Python for .NET - [http://sourceforge.net/projects/pythonnet/files/](http://sourceforge.net/projects/pythonnet/files/)
- IronPython - [ironpython.net/download/](http://ironpython.net/download/)
- PyPy - [pypy.org/download.html](http://pypy.org/download.html)


---

#Interpretorul

```
~ $ python3
```

    !python
    Python 3.4.0 (default, Jun 19 2015, 14:20:21) 
    [GCC 4.8.2] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> dir
    <built-in function dir>
    >>> help
    Type help() for interactive help, or help(object) for help about object.
    >>> help(dir)

    >>> 

Funcții foarte utile:  ```dir(...)``` și ```help(...)```.

---

#Interpretorul

```
~ $ python3 search.py "Python România"
```
    
    !text
    Titlu: <b>Python</b> Weekend @Iași - RoPython
        URL:https://conference.ropython.org/
    Titlu: LocalUserGroups - <b>Python</b> Wiki
        URL:https://wiki.python.org/moin/LocalUserGroups
    Titlu: <b>Romania</b> | <b>Python</b> Data Recovery
        URL:http://www.python.ro/romania
    Titlu: <b>Python</b> Data Recovery | Recover every bit
        URL:http://www.python.ro/


```
~ $ cat search.py
```

    !python
    import sys
    import requests

    def search(query):
        url = "http://ajax.googleapis.com/ajax/services/search/web"
        params = {"v": "1.0", "q": query}
        response = requests.get(url, params=params)
        data = response.json()
        for result in data["responseData"]["results"]:
            print("Titlu: {}\n\tURL:{}".format(result["title"],
                                               result["url"]))

    if __name__ == "__main__":
        search(sys.argv[1])

---

#Mediul de lucru

- Editor text:
    - Sublime Text
    - Notepad++
    - Vim

Mai multe exemple aici: [en.wikipedia.org/wiki/List_of_text_editors](https://en.wikipedia.org/wiki/List_of_text_editors).

- IDE-uri pentru Python:
    - Komodo (Windows/Linux/Mac OS X)
    - LiClipse (Linux/Mac OS X/Windows)
    - PyCharm (Linux/Mac OS X/Windows)
    - Wing IDE (Windows, Linux, Mac OS X)

Mai multe exemple aici: [wiki.python.org/moin/IntegratedDevelopmentEnvironments](https://wiki.python.org/moin/IntegratedDevelopmentEnvironments).

---


#Tipuri de date

---

#Tipuri de date numerice

**Intreg**
    
    !python
    >>> 10
    10
    >>> int(100)
    100
    
    >>> dir(int(10))
    ['...', 'bit_length', 'conjugate', 'denominator', 'imag',
     'numerator', 'real']
    
    >>> int(10).bit_length()
    4
    
    >>> int(10).conjugate()
    10
    
    >>> int(10).denominator
    1
    
    >>> int(10).numerator
    10

---

#Tipuri de date numerice

**Float**
    
    !python
    >>> 10.0
    10.0
    >>> float(10)
    10.0
    
    >>> dir(float(10))
    ['...', 'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag',
     'is_integer', 'real']
    
    >>> float(10).as_integer_ratio()
    (10, 1)
    
    >>> float(10).hex()
    '0x1.4000000000000p+3'
    
    >>> float(10).is_integer()
    True

---

#Tipuri de date numerice

**Long - Python 2.x**
    
    !python
    >>> sys.maxint + 1
    9223372036854775808L
    >>> type(_)
    <type 'long'>
    >>> long(10)
    10L
    
    >>> dir(long(10))
    ['...', 'bit_length', 'conjugate', 'denominator', 'imag',
     'numerator', 'real']
    
    >>> (sys.maxint + 1).denominator
    1L
    
    >>> (sys.maxint + 1).imag
    0L
    
    >>> (sys.maxint + 1).real
    9223372036854775808L
    
    >>> (sys.maxint + 1).conjugate()
    9223372036854775808L
    >>> (sys.maxint + 1).bit_length()
    64

---

#Tipuri de date numerice

**Complex**
    
    !python
    >>> a = complex(10, 5)
    >>> a
    (10+5j)
    
    >>> dir(a)
    ['...', 'conjugate', 'imag', 'real']
    
    >>> a.imag
    5.0

    >>> a.real
    10.0

    >>> a.conjugate()
    (10-5j)

---

#Tipuri de date booleene
    
    !python
    >>> True
    True
    >>> False
    False
    >>> bool(1)
    True
    >>> bool(0)
    False

    >>> dir(bool(1))
    ['...', 'bit_length', 'conjugate', 'denominator', 'imag',
     'numerator', 'real']
    >>> bool(1).bit_length()
    1

---

#Șirurile de caractere
    
    !python
    sir1 = 'Acesta este un sir de caractere'
    sir2 = "Acesta este un sir de caractere"
    sir3 = """Acesta este un sir de caractere
    pe mai multe linii."""
    sir4 = '''Acesta este un sir de caractere
    pe mai multe linii.'''
    sir5 = (
        "Acesta este un sir de caractere foarte"
        " lung, dar care totusi este pe o singura "
        " linie."
    )
    
    >>> dir("")
    ['...', 'capitalize', 'center', 'count', 'decode', 'encode',
     'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum',
     'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper',
     'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind',
     'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split',
     'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate',
     'upper', 'zfill']

---

#Șirurile de caractere

    !python
    >>> "Ana are mere.".capitalize()
    'Ana are mere.'

    >>> "ana are mere.".center(62)
    '                        ana are mere.                         '
    >>> "ana are mere.".count("a")
    3

    >>> "ana are mere.".endswith("mere.")
    True

    >>> "ana are mere.".startswith("ana")
    True

    >>> "ana are mere.".partition("are")
    ('ana ', 'are', ' mere.')
    
    >>> "ana are mere.".upper()
    'ANA ARE MERE.'
    
    >>> "ana are mere.".title()
    'Ana Are Mere.'
    
    >>> "ana are mere.".split()
    ['ana', 'are', 'mere.']

---

#Șirurile de caractere

    !python
    >>> "%s are mere." % "Ana"
    'Ana are mere.'

    >>> "%s are %s." % ("Ana", "mere")
    'Ana are mere.'

    >>> "%(nume)s are %(fructe)s." % {"nume": "Ana", "fructe": "mere"}
    'Ana are mere.'

    >>> "{} are {}.".format("Ana", "mere")
    'Ana are mere.'

    >>> "{nume} are {fructe}.".format(nume="Ana", fructe="mere")
    'Ana are mere.'

---

#Operatori

---

#Operatori booleeni

    !python
    >>> True or False
    True
    
    >>> True and False
    False
    
    >>> not True
    False
    
    >>> not False
    True

---

#Operatori pentru comparație

    !python
    >>> x < y
    False
    
    >>> x <= y
    True
    
    >>> x > y
    False
    
    >>> x >= y
    True
    
    >>> x == y
    True
    
    >>> x != y
    False
    
    >>> x is y
    True
    
    >>> x is not y
    False

---

#Operatori pentru operații matematice

    !python
    >>> 4 + 5
    9
    
    >>> 4 - 5
    -1
    
    >>> 5 / 2
    2
    
    >>> 5 // 2
    2
    
    >>> 5 % 2
    1
    
    >>> -5
    -5
    
    >>> +5
    5

În Python 3.x

    !python
    >>> 5 / 2
    2.5
    >>> 5 // 2
    2

---

#Operatori binari

    !python
    >>> 2 | 4
    6
    
    >>> 2 ^ 4
    6
    
    >>> 2 & 4
    0
    
    >>> 1 << 3
    8
    
    >>> 8 >> 3
    1
    
    >>> ~8
    -9

---

#Comentarii
    
    !python
    """
    Acesta este un comentariu.
    """

    # Acesta este un comentariu


---


#Liste și Tupluri

**Lista**: Structură de date flexibilă ce poate încapsula date eterogene.

    !python
    laborator_python = [
        ["Laboratorul 1",
            ["interpretor", "CPython", "IronPython", "PyPy"],
            ["exerciții", "maxim", "palindrom", "par", "putere"],
            ["note", 10, 5.4, 3.4, 10, 2, 1, 4],
         ],
    ]
    laborator_python[1] = ["Laboratorul 2"] 


**Tupluri**: Structură de date inflexibilă ce poate încapsula date eterogene.

    !python
    laborator_python = (
        ("Laboratorul 1",
            ("interpretor", "CPython", "IronPython", "PyPy"),
            ("exerciții", "maxim", "palindrom", "par", "putere"),
            ("note", 10, 5.4, 3.4, 10, 2, 1, 4),
         ),
    )
    laborator_python[1] = ["Laboratorul 2"]

    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    TypeError: 'tuple' object does not support item assignment

---

#Accesarea elementelor

    !python
    >>> laborator_python = [
    ...     ["Laboratorul 1",
    ...         ["interpretor", "CPython", "IronPython", "PyPy"],
    ...         ["exerciții", "maxim", "palindrom", "par", "putere"],
    ...         ["note", 10, 5.4, 3.4, 10, 2, 1, 4],
    ...      ],
    ... ]

    >>> laborator_python[0]
    ['Laboratorul 1', ['interpretor', 'CPython', 'IronPython', 'PyPy'],
    ['exerci\xc8\x9bii', 'maxim', 'palindrom', 'par', 'putere'],
    ['note', 10, 5.4, 3.4, 10, 2, 1, 4]]
    
    >>> laborator_python[0][1]
    ['interpretor', 'CPython', 'IronPython', 'PyPy']
    
    >>> laborator_python[0][1][1]
    'CPython'
    
    >>> laborator_python[0][1][2]
    'IronPython'
    
    >>> laborator_python[0][1][2][3]
    'n'

---


#Indexi negativi

    !python
    >>> laborator_python = [
    ...     ["Laboratorul 1",
    ...         ["interpretor", "CPython", "IronPython", "PyPy"],
    ...         ["exerciții", "maxim", "palindrom", "par", "putere"],
    ...         ["note", 10, 5.4, 3.4, 10, 2, 1, 4],
    ...      ],
    ... ]
    >>> laborator_python[-1]
    ['Laboratorul 1', ['interpretor', 'CPython', 'IronPython', 'PyPy'],
    ['exerci\xc8\x9bii', 'maxim', 'palindrom', 'par', 'putere'],
    ['note', 10, 5.4, 3.4, 10, 2, 1, 4]]
    
    >>> laborator_python[-1][-1][0]
    'note'
    
    >>> laborator_python[-1][-1][-1]
    4
    
    >>> laborator_python[-1][-1][-2]
    1
    
    >>> laborator_python[-1][-1][-3]
    2
    
    >>> laborator_python[-1][-2][-3]
    'palindrom'

---

#List slices (lista[început:sfârșit])

    !python
    >>> lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    >>> lista[0:3]
    [1, 2, 3]
    
    >>> lista[:3]
    [1, 2, 3]
    
    >>> lista[3:6]
    [4, 5, 6]
    
    >>> lista[3:]
    [4, 5, 6, 7, 8, 9]
    
    >>> lista[-1:]
    [9]
    
    >>> lista[-2:]
    [8, 9]
    
    >>> lista[:-1]
    [1, 2, 3, 4, 5, 6, 7, 8]
    
    >>> lista[:-2]
    [1, 2, 3, 4, 5, 6, 7]

---

#List slices (lista[început:sfârșit:pas])

    !python
    >>> lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    >>> lista[1::2]
    [2, 4, 6, 8]
    
    >>> lista[::2]
    [1, 3, 5, 7, 9]
    
    >>> lista[::-1]
    [9, 8, 7, 6, 5, 4, 3, 2, 1]
    
    >>> lista[-1:-5:-1]
    [9, 8, 7, 6]

---

#Operații utile

    !python
    >>> lista = []
    >>> lista.append(1)
    >>> lista.append(2)
    >>> lista.append(3)
    >>> lista
    [1, 2, 3]
    
    >>> lista.extend([4, 5, 6])
    >>> lista
    [1, 2, 3, 4, 5, 6]
    
    >>> lista.reverse()
    >>> lista
    [6, 5, 4, 3, 2, 1]
    
    >>> lista.sort()
    >>> lista
    [1, 2, 3, 4, 5, 6]


Mai multe metode utile se pot găsi folosind `dir(lista)` și `help(lista.count)`.

---

#Dictionar

**Dictionar**: Structură de date de forma **cheie** : **valoare**

    !python
    laborator_python = {
        "interpretor": ["CPython", "IronPython", "PyPy"],
        "exerciții": ("maxim", "palindrom", "par", "putere"),
        "note": {
            10 : [10, 10],
             5 : [5.4],
             4 : [4],
             3 : [3.4],
             2 : [2],
             1 : [1]
        },
    }
    laborator_python["exerciții"] = ["Laboratorul 2"] 

---

#Referințe

    !python
    >>> lista = [1, 2, 3, 4, 5]
    >>> lista2 = lista
    >>>
    >>> lista.append("x")
    >>> lista2.append("y")

---

#Referințe

    !python
    >>> lista = [1, 2, 3, 4, 5]
    >>> lista2 = lista
    >>>
    >>> lista.append("x")
    >>> lista2.append("y")
    >>> 
    >>> lista
    [1, 2, 3, 4, 5, 'x', 'y']
    
    >>> lista2
    [1, 2, 3, 4, 5, 'x', 'y']

---

#Referințe

    !python
    >>> lista = [[0]] * 10
    >>> lista
    [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]
    
    >>> lista[0].append(1)
    >>> lista[0].append(2)
    >>> lista[0].append(3)
    >>> lista[0].append(4)
    >>> lista[0].append(5)
    >>> lista[0].append(6)
    >>> 
    >>> for rand in lista:
    ...     print(rand)
    ... 

---

#Referințe

    !python
    >>> lista = [[0]] * 10
    >>> lista
    [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]
    
    >>> lista[0].append(1)
    >>> lista[0].append(2)
    >>> lista[0].append(3)
    >>> lista[0].append(4)
    >>> lista[0].append(5)
    >>> lista[0].append(6)
    >>> 
    >>> for rand in lista:
    ...     print(rand)
    ... 
    [0, 1, 2, 3, 4, 5, 6]
    [0, 1, 2, 3, 4, 5, 6]
    [0, 1, 2, 3, 4, 5, 6]
    [0, 1, 2, 3, 4, 5, 6]
    [0, 1, 2, 3, 4, 5, 6]
    [0, 1, 2, 3, 4, 5, 6]
    [0, 1, 2, 3, 4, 5, 6]
    [0, 1, 2, 3, 4, 5, 6]
    [0, 1, 2, 3, 4, 5, 6]
    [0, 1, 2, 3, 4, 5, 6]
    >>> 

---

#Referințe

    !python
    >>> lista = [1, 2, 3, [1, 2, 3]]
    >>> lista2 = list(lista)
    >>> 
    >>> lista.append("x")
    >>> lista2.append("y")
    >>>
    ---

    #Referințe

    >>> lista = [1, 2, 3, [1, 2, 3]]
    >>> lista2 = list(lista)
    >>> 
    >>> lista.append("x")
    >>> lista2.append("y")
    >>>

    >>> lista
    [1, 2, 3, [1, 2, 3], 'x']

    >>> lista2
    [1, 2, 3, [1, 2, 3], 'y']

---

#Referințe

    !python
    >>> lista = [1, 2, 3, [1, 2, 3]]
    >>> lista2 = list(lista)
    >>> 
    >>> lista.append("x")
    >>> lista2.append("y")
    >>> 

    >>> lista
    [1, 2, 3, [1, 2, 3], 'x']

    >>> lista2
    [1, 2, 3, [1, 2, 3], 'y']

    >>> lista[3].append(4)
    >>> lista2[3].append(4) 

---

#Referințe

    !python
    >>> lista = [1, 2, 3, [1, 2, 3]]
    >>> lista2 = list(lista)
    >>> 
    >>> lista.append("x")
    >>> lista2.append("y")
    >>> 

    >>> lista
    [1, 2, 3, [1, 2, 3], 'x']

    >>> lista2
    [1, 2, 3, [1, 2, 3], 'y']
     
    >>> lista[3].append(4)
    >>> lista2[3].append(4) 

    >>> lista
    [1, 2, 3, [1, 2, 3, 4, 4], 'x']

    >>> lista2
    [1, 2, 3, [1, 2, 3, 4, 4], 'y'] 

---

#Funcții built-in

---

#Funcții built-in

**print** - Scrie un mesaj într-un stream (predefinit este stdout)

```
print(value, ..., sep=' ', end='\n', file=sys.stdout)
```

    !python
    >>>from __future__ import print_function

    >>> print("ana", "are", "mere")
    ana are mere
    
    >>> print("Ana", "are", "mere", end='\n')
    Ana are mere
    
    >>> print("Ana", "are", "mere", sep='\n')
    Ana
    are
    mere

---

#Funcții built-in

**input** și **raw_input** - citesc informații de la tastatură

    !python
    >>> raw_input("Ana are: ")
    Ana are: mere
    'mere'
    
    >>> input("Numarul de mere pe care le are ana este: ")
    Numarul de mere pe care le are ana este: 10
    10
    
    >>> type(_)
    <type 'int'>
    
    >>> raw_input("Numarul de mere pe care le are ana este: ")
    Numarul de mere pe care le are ana este: 10
    '10'
    
    >>> type(_)
    <type 'str'>

*raw_input* este prezent doar în Python 2.x

---

#Funcții built-in

**open** deschide un fișier

```
open(name[, mode[, buffering]])
```

    !python
    >>> file_handle = open("test.tuxy", "w")
    >>> file_handle.write("Tuxy Pinguinescu este cel mai tare.")
    >>> file_handle.close()

    >>> file_handle = open("test.tuxy", "r")
    >>> file_handle.read()
    'Tuxy Pinguinescu este cel mai tare.'
    >>> file_handle.close()

---

#Funcții built-in

    !python
    >>> dir(__builtins__)
    
    ['...'. 'abs', 'all', 'any', 'apply', 'basestring', 'bin', 'bool',
     'buffer', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod',
     'cmp', 'coerce', 'compile', 'complex', 'copyright', 'credits',
     'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'execfile',
     'exit', 'file', 'filter', 'float', 'format', 'frozenset', 'getattr',
     'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int',
     'intern', 'isinstance', 'issubclass', 'iter', 'len', 'license',
     'list', 'locals', 'long', 'map', 'max', 'memoryview', 'min',
     'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
     'quit', 'range', 'raw_input', 'reduce', 'reload', 'repr', 'reversed',
     'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str',
     'sum', 'super', 'tuple', 'type', 'unichr', 'unicode', 'vars', 'xrange',
     'zip'
    ]

---

#Instrucțiuni condiționale

---

# if - elif - else
    
    !python
    if_stmt ::=  "if" expression ":" suite
                 ( "elif" expression ":" suite )*
                 ["else" ":" suite]

-

    !python
    >>> if numar % 5 == 0 and numar % 3 == 0: 
    ...     pass
    ... elif numar % 7 == 0:
    ...     pass
    ... else:
    ...     pass
    ... 

---

# for
    !python
    >>> numbers = range(1, 10)
    >>> numbers
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> for number in numbers:
    ...     print("The number is %d" % number)
    ... 
    The number is 1
    The number is 2
    The number is 3
    The number is 4
    The number is 5
    The number is 6
    The number is 7
    The number is 8
    The number is 9

--- 

# for
    !python
    >>> number = 0
    >>> while number < 10:
    ...     print("The number is %d" % number)
    ...     x += 1
    ... 
    The number is 0
    The number is 1
    The number is 2
    The number is 3
    The number is 4
    The number is 5
    The number is 6
    The number is 7
    The number is 8
    The number is 9


--- 

#Resurse

- www.python.org
- www.learnpython.org/
- www.learnpythonthehardway.org
- www.corepython.com
- www.codecademy.com/tracks/python
- www.checkio.org
- www.ropython.org
- www.github.com/RoPython
