
# Unittests

Mit Unittests (auf deutsch Komponententests) können in Python Klassen getestet werden. Hierfür wird das Modul [unittest](https://docs.python.org/3/library/unittest.html) verwendet, das mit jeder Python-Installation ausgeliefert wird.

Wir erstellen zunächst eine einfache Klasse, die getestet werden soll und speichern sie in der Datei `person.py`.



```python

class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
        
    def altern(self, jahre):
        self.alter += jahre
```



Wir testen nun die Methode `altern` und schauen, ob sie das tut, was sie soll. Hierfür wird eine Testklasse erzeugt - vorzugsweise in einer neuen Datei. 

Ein Testfall erbt von `unittest.TestCase` und erhält dadurch verschiedene Methoden, die in Testfällen verwendet werden können - z.B. `assertEqual, assertTrue, assertFalse`.

Alle Methoden, die mit `test...` beginnen sind Testfälle, die automatisch ausgeführt werden.

Die Methode `setUp` wird vor jeder Methode `test...` ausgeführt. Hier können Vorbereitungen für den Test getroffen werden.


```python

from person import Person
import unittest

class PersonTest(unittest.TestCase):
    def setUp(self):
        self.p = Person("Hans", 18)
        
    def test_altern(self):
        vorher = self.p.alter
        self.p.altern(1)
        
        self.assertEqual(self.p.alter, 19)
        self.assertTrue(self.p.alter == 19)        
```



Die Test können anschließend ausgeführt werden.


```python
python3 -m unittest person_test.py
```

    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.000s
    
    OK


Das sieht gut aus. Es gibt keine Fehler.

Mit der Option `-v` werden zusätzliche Informationen beim Ausführen der Tests angezeigt.


```python
python3 -m unittest -v person_test.py
```

    test_altern (person_test.PersonTest) ... ok
    
    ----------------------------------------------------------------------
    Ran 1 test in 0.000s
    
    OK


Es gibt jedoch ein Problem mit der Methode `altern`. Wenn `altern` mit einem negativen Parameter aufgerufen wird, wird die Zahl abgezogen. Das sollte nicht passieren, da dieses Verhalten nicht zum Name `altern` passt.


```python

from person import Person
import unittest

class PersonTest(unittest.TestCase):
    def setUp(self):
        self.p = Person("Hans", 18)
        
    def test_altern(self):
        vorher = self.p.alter
        self.p.altern(1)
        
        self.assertEqual(self.p.alter, 19)
        self.assertTrue(self.p.alter == 19)
        
    def test_altern2(self):  # ein neuer Testfall
        self.p.altern(-100)  # Das sollte nicht funktionieren dürfen
        self.assertTrue(self.p.alter > 0, "Die Person hat ein negatives Alter!")        
```



Nun schlägt der Testfall fehl.


```python
python3 -m unittest person_test.py
```

    .F
    ======================================================================
    FAIL: test_altern2 (person_test.PersonTest)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "/Users/bakera/proj/software-101/unittest/person_test.py", line 18, in test_altern2
        self.assertTrue(self.p.alter > 0, "Die Person hat ein negatives Alter!")
    AssertionError: False is not true : Die Person hat ein negatives Alter!
    
    ----------------------------------------------------------------------
    Ran 2 tests in 0.000s
    
    FAILED (failures=1)


Wir beheben das Problem, indem wir die Methode `altern` so anpassen, dass sie bei negativen Werten nichts tut.


```python

class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
        
    def altern(self, jahre):
        if jahre >= 0:
            self.alter += jahre
```



Nun läuft unser Test durch.


```python
python3 -m unittest person_test.py
```

    ..
    ----------------------------------------------------------------------
    Ran 2 tests in 0.000s
    
    OK


# Doctest

Eine Besonderheit von Python sind doctests. Darunter versteht man Kommentare im Quelltext, die gleichzeitig getestet werden können.

Wir verwenden wieder die defekte Version der Klasse Person. Kommentare ähneln nun einer Interpreter-Sitzung und werden bei einem Test ausgeführt. Eingaben beginnen mit `>>>` und erwartete Ausgaben stehen direkt darunter.


```python
class Person:
    '''Eine Person. Die Klasse kann wie folgt verwendet werden.
    
    >>> peter = Person("Person", 21)
    >>> peter.alter
    21
    
    >>> peter.altern(1)
    >>> peter.alter
    22
    
    Wenn ein negativer Wert für altern verwendet wird, so 
    ändert sich das Alter nicht.
    
    >>> peter.altern(-10)
    >>> peter.alter
    22
    
    '''
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
        
    def altern(self, jahre):
        self.alter += jahre
```

Mit Hilfe des Moduls `doctest` kann das aktuelle Modul mit der Methode `testmod` getestet werden.


```python
import doctest
doctest.testmod()
```

    **********************************************************************
    File "__main__", line ?, in __main__.Person
    Failed example:
        peter.alter
    Expected:
        22
    Got:
        12
    **********************************************************************
    1 items had failures:
       1 of   6 in __main__.Person
    ***Test Failed*** 1 failures.





    TestResults(failed=1, attempted=6)



Wir sehen einen Fehler. Er taucht bei der Verwendung `altern(-10)` auf. Wir müssen die Methode `altern` reparieren. Das Alter soll sich nicht ändern, wenn der Änderungswert negativ ist. Mit einer geänderten Version der Methode klappen die Tests schließlich wieder.


```python
class Person:
    '''Eine Person. Die Klasse kann wie folgt verwendet werden.
    
    >>> peter = Person("Person", 21)
    >>> peter.alter
    21
    
    >>> peter.altern(1)
    >>> peter.alter
    22
    
    Wenn ein negativer Wert für altern verwendet wird, so 
    ändert sich das Alter nicht.
    
    >>> peter.altern(-10)
    >>> peter.alter
    22
    
    '''
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
        
    def altern(self, jahre):
        if jahre >= 0:
            self.alter += jahre
```

Erneut lassen wir die Tests laufen.


```python
doctest.testmod()
```




    TestResults(failed=0, attempted=6)



Wir erhalten keine Ausgaben. Dies zeigt an, dass die Tests durchgelaufen sind.

# Pytest

Das Modul [pytest](https://docs.pytest.org) ist ein Python-Modul, das den Entwickler beim Testen unterstützen will. 

## Installation

Die Installation erfolgt mit pip.

  - Linux/MacOS: `pip3 install pytest` oder `python3 -m pip install pytest`
  - Windows: `pip install pytest` oder `python -m pip install pytest` oder `py -m pip install pytest`
  
Danach steht ein Befehl `pytest` zur Verfügung, mit dem die Tests durchgeführt werden.


```python
pytest
```

    ============================= test session starts ==============================
    platform linux -- Python 3.5.2, pytest-3.8.2, py-1.6.0, pluggy-0.7.1
    rootdir: /home/marco/proj/software-101/testing, inifile:
    collected 0 items                                                              
    
    ========================= no tests ran in 0.00 seconds =========================


## Pytest-Beispiele

Wir verwenden wieder die bekannte Klasse Person und ergänzen sie um eine Methode `test_person`. Methoden, die mit `test` beginnen, werden von pytest für die Tests genutzt. Die eigentlichen Annahmen, werden mit gewöhnlichen `assert`-Statements durchgeführt. Dadurch müssen keine weiteren Bibliotheken importiert werden.


```python

class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
        
    def altern(self, jahre):
        self.alter += jahre
        
def test_person():
    p = Person("Hans", 18)
        
    vorher = p.alter
    p.altern(1)
    
    assert p.alter > vorher
    assert p.alter == 19

    p.altern(-100)  # Das sollte nicht funktionieren dürfen
    assert p.alter > 0, "Die Person hat ein negatives Alter!"        
```



Wenn wir die Tests nun ausführen, schlagen sie wie erwartet fehlt.


```python
pytest person.py
```

    ============================= test session starts ==============================
    platform linux -- Python 3.5.2, pytest-3.8.2, py-1.6.0, pluggy-0.7.1
    rootdir: /home/marco/proj/software-101/testing, inifile:
    collected 1 item                                                               
    
    person.py F                                                              [100%]
    
    =================================== FAILURES ===================================
    _________________________________ test_person __________________________________
    
        def test_person():
            p = Person("Hans", 18)
        
            vorher = p.alter
            p.altern(1)
        
            assert p.alter > vorher
            assert p.alter == 19
        
            p.altern(-100)  # Das sollte nicht funktionieren dürfen
    >       assert p.alter > 0, "Die Person hat ein negatives Alter!"
    E       AssertionError: Die Person hat ein negatives Alter!
    E       assert -81 > 0
    E        +  where -81 = <person.Person object at 0x7f5341e4bdd8>.alter
    
    person.py:20: AssertionError
    =========================== 1 failed in 0.04 seconds ===========================


Wir korrigieren nun erneut die Methode `altern` und ändern das Alter nur, wenn der Änderungswert positiv ist.


```python

class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
        
    def altern(self, jahre):
        if jahre >= 0:  # Korrektur
            self.alter += jahre  
        
def test_person():
    p = Person("Hans", 18)
        
    vorher = p.alter
    p.altern(1)
    
    assert p.alter > vorher
        
    assert p.alter == 19

    p.altern(-100)  # Das sollte nicht funktionieren dürfen
    assert p.alter > 0, "Die Person hat ein negatives Alter!"        
```




```python
pytest person.py
```

    ============================= test session starts ==============================
    platform linux -- Python 3.5.2, pytest-3.8.2, py-1.6.0, pluggy-0.7.1
    rootdir: /home/marco/proj/software-101/testing, inifile:
    collected 1 item                                                               
    
    person.py .                                                              [100%]
    
    =========================== 1 passed in 0.02 seconds ===========================


Nun sind die Tests erfolgreich durchgelaufen.

Doch wie testet man, ob ein Fehler auftritt? Wenn das Ändern des Alters mit einem negativen Wert zu einem Fehler führen soll, kann auch dies getestet werden. Dafür wird der Teil, der einen Fehler erzeugen soll, in einen try-except-Block platziert.


```python

class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
        
    def altern(self, jahre):
        if jahre >= 0:
            self.alter += jahre  
        else:
            raise ValueError("Keine negativen Werte erlaubt") # Fehler erzeugen
        
def test_person_mit_Fehler():
    p = Person("Hans", 18)
        
    try:
        p.altern(-100)  # Fehler soll auftreten -> Sprung in Except-Zweig
        assert False  # Diese Zeile schlägt immer fehl
    except ValueError:
        assert p.alter > 0, "Die Person hat ein negatives Alter!"        
    
```




```python
pytest person.py
```

    ============================= test session starts ==============================
    platform linux -- Python 3.5.2, pytest-3.8.2, py-1.6.0, pluggy-0.7.1
    rootdir: /home/marco/proj/software-101/testing, inifile:
    collected 1 item                                                               
    
    person.py .                                                              [100%]
    
    =========================== 1 passed in 0.02 seconds ===========================


Die Tests waren erfolgreich, da die Exception wie erwartet aufgetreten ist.

## Testabdeckung

Die Anweisungs und Zweigabdeckung von Testfällen kann mit dem
Pythonpaket [coverage.py](https://coverage.readthedocs.io/) ermittelt werden.

Es wird wie gewohnt mit pip installiert: 
* `pip3 install coverage` (Linux, MacOS)
* `py -m pip install coverage` (Windows).

Für die Testabdeckung verwenden wir wieder die Klasse Person.


```python

class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
        
    def altern(self, jahre):
        if jahre >= 0:
            self.alter += jahre  
        else:
            raise ValueError("Keine negativen Werte erlaubt")
        
def test_person():
    p = Person("Hans", 18)
    p.altern(1)
    assert p.alter == 19
        
test_person()
```



Mit dem Kommando `run` können die Tests ausgeführt werden.


```python
!coverage run person.py
```

Anschließend werden die Ergebnisse mit `report` angezeigt.


```python
!coverage report
```

    Name        Stmts   Miss  Cover
    -------------------------------
    person.py      13      1    92%


Eine Zweigabdeckung wird mit der Option `--branch` ermöglicht.


```python
!coverage run --branch person.py
```

Nun tauchen auch Informationen zur Zweigabdeckung auf.


```python
!coverage report
```

    Name        Stmts   Miss Branch BrPart  Cover
    ---------------------------------------------
    person.py      13      1      2      1    87%


Mit dem Kommando `html` kann eine übersichtliche Darstellung erzeugt
werden.


```python
!coverage html
```

Das Ergebnis steht in dem Unterordner [htmlcov](htmlcov/index.html) zur
Verfügung.


```python
!ls htmlcov
```

    coverage_html.js                   jquery.tablesorter.min.js
    index.html                         keybd_closed.png
    jquery.ba-throttle-debounce.min.js keybd_open.png
    jquery.hotkeys.js                  person_py.html
    jquery.isonscreen.js               status.json
    jquery.min.js                      style.css

