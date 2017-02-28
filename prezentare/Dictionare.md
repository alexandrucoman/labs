#Limbajul Python - Dicționare

---

#Crearea dicționarelor


    !python
    >>> d = {}
    >>> d['key1'] = 'value1'
    >>> d['key2'] = 1
    >>> d[1] = 'value'
    >>> d[2] = 2
    >>> d['par'] = [2, 4, 6, 8]
    >>> print(d)
    {'key1': 'value1', 1: 'value', 2: 2, 'par': [2, 4, 6, 8], 'key2': 1}

    >>> d2 = {'key1': 'value1', 'key2': 1, 1: 2}
    >>> print(d2)
    {'key1': 'value1', 1: 2, 'key2': 1}

---

#Crearea dicționarelor

Folosind **dict()**.

    !python
    >>> d = dict([('key1', 'val1'), ('key2', 1), (1, 2)])
    >>> print(d)
    {'key1': 'val1', 1: 2, 'key2': 1}

Folosing **dictionary comprehension**

    !python
    >>> {x: x**2 for x in (2, 4, 6)}
    {2: 4, 4: 16, 6: 36}

---

#Dicționare imbricate

    !python
    d = {
        "key1": {
            "key2": {
                "key3": {
                    "key4": "value1"
                },
                "key5": "value2",
            }
        }
    }

    {'key1': {'key2': {'key3': {'key4': 'value1'}, 'key5': 'value2'}}}

---

#Accesarea elementelor unui dicționar

    !python
    >>> d = {'key1': 'value1', 1: 2, 'key2': 1}

    >>> print(d['key1'])
    'value1'

    >>> print(d[1])
    2

    >>> print(d[0])
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    KeyError: 0

    >>> d.get('key1')
    'value1'

---

#Parcurgerea dicționarelor

    !python
    >>> d = {'key1': 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}

    >>> for k in d:
    ...      print(k, d[k])
    ...
    key1 1
    key3 3
    key4 4
    key2 2
    key5 5

---

#Parcurgerea dicționarelor

    !python
    >>> d = {'key1': 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}

    >>> for k, v in d.items():
    ...     print(k, v)
    ...
    key1 1
    key3 3
    key4 4
    key2 2
    key5 5

    >>> d.items()
    dict_items([('key1', 1), ('key3', 3), ('key4', 4), ('key2', 2), ('key5', 5)])

---

#Modificarea unui dicționar

    !python
    >>> d = {'key1': 'value1', 1: 2, 'key2': 1}
    >>> print(d)
    {1: 2, 'key1': 'value1', 'key2': 1}

    >>> d['key1'] = 'value3'
    >>> print(d)
    {1: 2, 'key1': 'value3', 'key2': 1}

    >>> # Adăugarea unui nou element în dicționar
    >>> d['new'] = 'value'
    >>> print(d)
    {1: 2, 'key1': 'value3', 'new': 'value', 'key2': 1}

    >>> # Ștergerea unui element din dicționar
    >>> del d[1]
    >>> print(d)
    {'key1': 'value3', 'new': 'value', 'key2': 1}
    
    >>> # Ștergerea tuturor elementelor
    >>> d.clear()
    {}

---

#Modificarea unui dicționar

Metoda **update()**

    !python
    >>> d1 = {'key1': 1, "key2": 2}
    >>> d2 = {"key3": 3, "key4": 4, "key5": 5}

    >>> d1.update(d2)
    >>> d1
    {'key1': 1, 'key3': 3, 'key2': 2, 'key4': 4, 'key5': 5}
    >>> d2
    {'key3': 3, 'key4': 4, 'key5': 5}

---

#Modificarea unui dicționar

Metoda **pop()**

    !python
    >>> d = {'key1': 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}
    
    >>> d.pop('key1')
    1
    >>> print(d)
    {'key5': 5, 'key3': 3, 'key4': 4, 'key2': 2}

    >>> d.pop('key1')
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    KeyError: 'key1'

---

#Modificarea unui dicționar

Metoda **popitem()**

    >>> d = {'key1': 1, "key2": 2}

    >>> d.popitem()
    ('key2', 2)
    >>> d.popitem()
    ('key1', 1)
    >>> d.popitem()
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    KeyError: 'popitem(): dictionary is empty'

---

#Modificarea unui dicționar
    
Metoda **setdefault()**

    !python
    >>> d = {'key1': 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}
    
    >>> d.setdefault('key6', 6)
    6
    >>> d.setdefault('key6', 0)
    6
    >>> d
    {'key6': 6, 'key1': 1, 'key3': 3, 'key2': 2, 'key4': 4, 'key5': 5}

---

#Modificarea unui dicționar

Metoda **setdefault()**

    !python
    >>> d.setdefault('key6', 6)
    6
    >>> d.setdefault('key6', 0)
    6
    >>> d
    {'key6': 6, 'key1': 1, 'key3': 3, 'key2': 2, 'key4': 4, 'key5': 5}

    >>> help(d.setdefault)
    Help on built-in function setdefault:

    setdefault(...) method of builtins.dict instance
        D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D

---

#Referințe

    !python
    >>> d1 = {'key1': 1, 'key2': 2}
    >>> d2 = d1
    >>> d2['key3'] = 3

    >>> print(d1)
    {'key1': 1, 'key2': 2, 'key3': 3}
    >>> print(d2)
    {'key1': 1, 'key2': 2, 'key3': 3}

---

#Bibliografie

<sup>1</sup> <a href="https://docs.python.org/3.4/tutorial/datastructures.html">Documentația Python 3.4</a><br/>
<sup>2</sup> <a href="http://learnpythonthehardway.org/book/ex39.html">Learn Python the Hard Way</a><br/>
<sup>3</sup> <a href="http://www.learnpython.org/en/Welcome">Learn Python Tutorial</a>
