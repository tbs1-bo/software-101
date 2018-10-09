
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

