
# Persistenz

Unter Persistenz versteht man das dauerhafte Speichern von Daten. Hierfür existieren grob zwei Möglichkeiten: Daten in einer Datenbank oder in einer Datei speichern. Hier soll es um die Persistenz in Dateien gehen.

Wir wollen verschiedene Messdaten speichern und erzeugen dafür zunächst ein paar Testdaten. Die bestehen aus einem Zeitstempel wie er von `time.time()` erzeugt wird und einem Messwert - z.B. ein Temperaturwert.


```python
EXAMPLE_DATA = [
    (1548573684.800749, 25),
    (1548573685.810749, 24.8),
    (1548573686.820749, 24)
]
```

Die Daten können nun z.B. in einer einfachen Klasse `Datastore` verwaltet werden.


```python
class Datastore:
    def __init__(self):
        self.data = []
```

Nun erzeugen wir ein Objekt und fügen die Testdaten hinzu.


```python
ds = Datastore()
ds.data = EXAMPLE_DATA
```

## CSV

Die Daten sollen nun in einer CSV-Datei gespeichert werden. Hierbei handelt es sich um ein Tesxtformat, das einzelne Datensätze in Zeilen speichert. Jedes Datum im Datensatz wird über ein Zeichen getrennt: wir verwenden das Semikolon, da es selten in Daten vorkommt.


```python
class Datastore:
    def __init__(self):
        self.data = []

    def save_csv(self, filename):
        'Save data to CSV file.'
        with open(filename, "wt") as file:
            for timeval, tempval in self.data:
                file.write(str(timeval) + ";" + str(tempval) + "\n")

    def load_csv(self, filename):
        'Load content of CSV-file into data attribute.'
        self.data = []
        with open(filename, "rt") as file:
            lines = file.readlines()
            
        for line in lines:
            time, temp = line.strip().split(";")
            self.data.append( (float(time), float(temp)) )
```

Ein Datastore-Objekt kann nun mit den Testdaten befüllt und gespeichert werden.


```python
ds = Datastore()
ds.data = EXAMPLE_DATA
print('Writing data:', ds.data)
ds.save_csv("data.csv")
```



Nun wurde eine Datei geschrieben, deren Inhalt wir uns einmal anschauen.


```python
!cat data.csv
```

    1548573684.800749;25
    1548573685.810749;24.8
    1548573686.820749;24


Anschließend können die Daten wieder geladen werden.


```python
ds2 = Datastore()
ds2.load_csv('data.csv')
print('Loaded data:', ds2.data)
```

    Loaded data: [(1548573684.800749, 25.0), (1548573685.810749, 24.8), (1548573686.820749, 24.0)]


## Pickle

Mit der Bibliothek `pickle`, können ganze Objekte in Python in einer Binärdatei gespeichert und wieder geladen werden. pickle muss nicht extra installiert werden. Wir müssen es aber zu Beginn importieren. Die Datastoreklasse wird nun um Methoden für das Speichern und Laden ergänzt.


```python
import pickle

class Datastore:
    def __init__(self):
        self.data = []

    def save_pickle(self, filename):
        'Save object to a file (binary pickle format).'
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load_pickle(filename):
        'Load Datastore object from file and return it.'
        with open(filename, 'rb') as file:
            ds = pickle.load(file)
            return ds
```

Man beachte den Dekorator `@staticmethod` bei der Methode `load_pickle`. Er bewirkt, dass die Methode nicht auf dem Objekt, sondern auf der Klasse aufgerufen wird. Das ist sinnvoll, da wir beim Laden noch kein Objekt haben. 

Doch speichern wir zunächst die Testdaten.


```python
ds = Datastore()
ds.data = EXAMPLE_DATA
print('Write data', ds.data)
ds.save_pickle('data.pickle')
```

    Write data [(1548573684.800749, 25), (1548573685.810749, 24.8), (1548573686.820749, 24)]


Es wurde eine Datei `data.pickle` angelegt, die man sich mit einem Hexeditor anschauen kann. Darin kann man Teile der Klasse erkennen. Es ist aber schwieriger, die Daten zu überprüfen als dies bei einer Textdatei der Fall ist.


```python
!xxd data.pickle
```

    00000000: 8003 635f 5f6d 6169 6e5f 5f0a 4461 7461  ..c__main__.Data
    00000010: 7374 6f72 650a 7100 2981 7101 7d71 0258  store.q.).q.}q.X
    00000020: 0400 0000 6461 7461 7103 5d71 0428 4741  ....dataq.]q.(GA
    00000030: d713 56fd 333f 794b 1986 7105 4741 d713  ..V.3?yK..q.GA..
    00000040: 56fd 73e3 5047 4038 cccc cccc cccd 8671  V.s.PG@8.......q
    00000050: 0647 41d7 1356 fdb4 8727 4b18 8671 0765  .GA..V...'K..q.e
    00000060: 7362 2e                                  sb.


Nun werden die Dateien wieder geladen. Wir rufen die Methoden zum Laden direkt auf der Klasse auf und erhalten ein Objekt, so wie es vor dem Speichern ausgehen hat.


```python
ds2 = Datastore.load_pickle('data.pickle')
print('Loaded data', ds2.data)
```

    Loaded data [(1548573684.800749, 25), (1548573685.810749, 24.8), (1548573686.820749, 24)]

