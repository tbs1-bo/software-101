
# Type-Hints in Python

In Python können ab Version 3.6 Typen im Quelltext annotiert werden. Mit `mypy` können diese Typen geprüft werden. Es kann einfach mit pip installiert werden.

    $ pip install mypy

Einfache Type können für Zahlen angegeben werden.


```python

a:int = 1
```



Mit mypy kann die Datei getestet werden.


```python
mypy typentest.py
```

Wir bauen nun einen Fehler ein.


```python

a:int = 1
a = "eins"
```



mypy zeigt nun den Fehler an.


```python
mypy typentest.py
```

    typentest.py:3: error: Incompatible types in assignment (expression has type "str", variable has type "int")


Funktionen können auch mit Typinformationen ausgestattet werden. Zu Erinnerung: so sehen für gewöhnlich Funktionen aus, wenn sie keine Typinformationen enthalten.


```python
def greet(name):
    return "Hallo" + name
```

Die Funktion kann um Typen ergänzt werden. Es kann sowohl der Parameter als auch der Rückgabewert typisiert werden.


```python

def greeting(name:str) -> str:
    return "Hallo" + name


greeting("Otto")          # OK
greeting("Du " + "Otto")  # OK
greeting(23)      # not OK
greeting(False)   # not OK
```



Durch eine Überprüfung können so Fehler im Quelltext entdeckt werden.


```python
mypy typentest.py
```

    typentest.py:8: error: Argument 1 to "greeting" has incompatible type "int"; expected "str"
    typentest.py:9: error: Argument 1 to "greeting" has incompatible type "bool"; expected "str"


Nun eine Funktion, die keinen Rückgabewert besitzt.


```python

def func_without_retval() -> None:
    print("In p()")
    
func_without_retval()           # OK
result = func_without_retval()  # not OK
```




```python
mypy typentest.py
```

    typentest.py:6: error: "func_without_retval" does not return a value


Es sind auch komplexe Typen wie Listen, Mengen oder Dictionaries erlaubt.


```python

from typing import List, Set

x1:List[int] = [1, 2, 3]    # OK
x2:List[int] = [1, 2, 3.3]  # not OK
y1:Set[float] = {1.1, 2.2}  # OK
y2:Set[float] = {1, "2"}    # not OK    
```




```python
mypy typentest.py
```

    typentest.py:5: error: List item 2 has incompatible type "float"; expected "int"
    typentest.py:7: error: Argument 2 to <set> has incompatible type "str"; expected "float"


Bei Dictionaries müssen der Typ für den Key und den Value angegeben werden.


```python

from typing import Dict

x:Dict[int, str] = {1: "eins", 2: "zwei"}    # OK
y:Dict[int, str] = {"1": "eins", 2: "zwei"}  # not OK
```




```python
mypy typentest.py
```

    typentest.py:5: error: Dict entry 0 has incompatible type "str": "str"; expected "int": "str"


Auch eigene Klassen können als Typen verwendet werden.


```python

class MeineKlasse:
    def __init__(self, x:int) -> None:
        self.x:int = x
            
            
mk1:MeineKlasse = MeineKlasse(23)     # OK
mk2:MeineKlasse = MeineKlasse(23.42)  # not OK
```




```python
mypy typentest.py
```

    typentest.py:8: error: Argument 1 to "MeineKlasse" has incompatible type "float"; expected "int"


Die Klasse kann auch in anderen Klassen verwendet werden.


```python

class MeineKlasse:
    def __init__(self) -> None:
        self.x:int = 23

class AndereKlasse:
    def __init__(self, mk: MeineKlasse) -> None:
        self.attr: MeineKlasse = mk
            
            
mk:MeineKlasse = MeineKlasse()
ak1:AndereKlasse = AndereKlasse(mk)  # OK
ak2:AndereKlasse = AndereKlasse(23)  # not OK
```




```python
mypy typentest.py
```

    typentest.py:13: error: Argument 1 to "AndereKlasse" has incompatible type "int"; expected "MeineKlasse"


Weitere Annotationen sind im [Cheat Sheet von mypy](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html) gelistet.
