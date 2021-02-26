# Datenbankzugriff

Für die folgenden Beispiele wollen wir eine Tabelle Personen(nr, name) mit den Attributen `nr` und `Name` erstellen und jeweils wieder abfragen.


```python
TESTDATEN = [[101, "Peter"], 
             [102, "Petra"], 
             [103, "Hans"], 
             [104, "Claudia"]]
```

## Sqlite

Mit dem Python-Paket [sqlite3](https://docs.python.org/library/sqlite3.html)
kann auf  sqlite-Datenbanken direkt zugegriffen werden. Es muss daher nicht
installiert werden und ist bei jeder Python-Installation vorhanden.

In der folgenden Beispielanwendung erstellen wir eine Beispieltabelle,
fügen ein paar Daten hinzu und geben diese wieder aus.


```python
import sqlite3
```

Nach dem Import des `sqlite3`-Moduls können nun Daten hinzugefügt und anschließend wieder ausgelesen werden.
Zunächst wird eine Verbindung erstellt und aus dieser ein `Cursor` generiert, mit dem auf die Datenbank zugegriffen werden kann.


```python
def insert_into_db():
    conn = sqlite3.connect("datenbank.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS 
        personen(nr int, name text)""")

    for nr, name in TESTDATEN:
        # use keyword paramters :nr, :name to avoid sql injection
        print("Füge Daten hinzu:", nr, name)
        c.execute(
            "INSERT INTO personen (nr, name) VALUES(:nr,:name)", 
            {'nr':nr, 'name':name})

    conn.commit()
    conn.close()

insert_into_db()
```

    Füge Daten hinzu: 101 Peter
    Füge Daten hinzu: 102 Petra
    Füge Daten hinzu: 103 Hans
    Füge Daten hinzu: 104 Claudia


Wir finden nun eine Datei `datenbank.db` im aktuellen Verzeichnis.


```python
ls datenbank.db
```

    datenbank.db


Die Daten können wieder aus der Datei gelesen werden.


```python
conn = sqlite3.connect("datenbank.db")
c = conn.cursor()
rows = c.execute("SELECT nr, name FROM personen")

print("Nr.\t Name")
for i, name in rows:
    print(i, "\t", name)

conn.close()
```

    Nr.	 Name
    101 	 Peter
    102 	 Petra
    103 	 Hans
    104 	 Claudia


### Fremdschlüssel (Foreign Keys) in SQLite

[Foreign Keys](https://sqlite.org/foreignkeys.html) werden in SQLite standardmäßig nicht
unterstützt und müssen pro Connection einmal über `PRAGMA foreign_keys = ON` aktiviert 
werden.


```python
conn = sqlite3.connect("datenbank.db")
c = conn.cursor()
c.execute("""
    CREATE TABLE freundschaft (
        person1 int, 
        person2 int,
        FOREIGN KEY (person1) REFERENCES personen(nr),
        FOREIGN KEY (person2) REFERENCES personen(nr),
        PRIMARY KEY (person1, person2)
    )
    """)
```




    <sqlite3.Cursor at 0x7f0280352490>



Wir befreunden die Personen Peter (101) und Petra (102) miteinander.


```python
c.execute("INSERT INTO freundschaft VALUES (101,102)")
conn.commit()
```

Leider wird nicht geprüft, ob die Personen, die befreundet werden sollen, überhaupt
existieren. 

So würden wir bei der nächsten Anweisung eine Fehlermeldung erwarten, da die Personen
mit den IDs -1 und -2 nicht existieren.


```python
c.execute("INSERT INTO freundschaft VALUES (-1,-2)")
conn.commit()
```

Wird die Unterstützung für Fremdschlüssel aktiviert, erfolgt die gewünschte Fehlermeldung.


```python
c.execute("PRAGMA foreign_keys = ON")
c.execute("INSERT INTO freundschaft VALUES (-3,-4)")
conn.commit()
```


    ---------------------------------------------------------------------------

    OperationalError                          Traceback (most recent call last)

    <ipython-input-9-d06c9f3b7f9e> in <module>
          1 c.execute("PRAGMA foreign_keys = ON")
    ----> 2 c.execute("INSERT INTO freundschaft VALUES (-3,-4)")
          3 conn.commit()


    OperationalError: foreign key mismatch - "freundschaft" referencing "personen"


Wir löschen zum Schluss die Datenbank-Datei.


```python
rm datenbank.db
```

## MySQL

Für den Zugriff auf eine MySQL-Datenbank muss zusätzlich ein 
[Connector für 
MySQL](https://dev.mysql.com/doc/connector-python/en/connector-python-installation-binary.html)
installiert werden. Dies kann z.B. mit dem folgenden Aufruf geschehen.

    $ pip install mysql-connector-python

Bei Rechteproblemen:

    $ pip install --user mysql-connector-python

Wenn alles geklappt hat, können wir im Anschluss das neue Modul importieren.


```python
import mysql.connector
```

Wie stellen eine Verbindung mit der Datenbank her. Diesmal müssen wir Zugangsdaten und die Datenbank angeben.


```python
conn = mysql.connector.connect(user='root', password='',
                               host='127.0.0.1',
                               database='test')
conn.close()
```

Nun können wir eine Tabelle `personen` in der Datenbank `test` erstellen.


```python
conn = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='test')
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS personen")
c.execute("""CREATE TABLE IF NOT EXISTS 
          personen(nr int, name text)""")

conn.close()
```

Wir benutzen das Kommandozeilentool `mysql` und lassen uns die Tabellen in der Datenbank `test` anzeigen.


```python
mysql -uroot --execute="SHOW TABLES;" test 
```

    +----------------+
    | Tables_in_test |
    +----------------+
    | personen       |
    +----------------+


Nun können wir neue Daten in die Tabelle einfügen.

**Achtung:** Die Platzhalter beim Einfügen werden unter MySQL anders angegeben.


```python
conn = mysql.connector.connect(user="root", password="",
                              host="127.0.0.1", database="test")
c = conn.cursor()
for nr, name in TESTDATEN:
    print("Füge Daten hinzu:", nr, name)
    c.execute(
        """INSERT INTO personen (nr, name) VALUES(%s,%s)""", 
        (nr, name))
conn.commit()
conn.close()
```

    Füge Daten hinzu: 101 Peter
    Füge Daten hinzu: 102 Petra
    Füge Daten hinzu: 103 Hans
    Füge Daten hinzu: 104 Claudia


Schließlich werden die Daten wieder mit einer SELECT-Anweisung aus der Datenbank abgefragt. Wir nutzen zunächst den Kommandozeilen-Client.


```python
mysql -uroot --execute="SELECT * FROM personen" test 
```

    +------+---------+
    | nr   | name    |
    +------+---------+
    |  101 | Peter   |
    |  102 | Petra   |
    |  103 | Hans    |
    |  104 | Claudia |
    +------+---------+


Die Daten können natürlich auch mit Python abgerufen werden. Auch hier gibt es einen Unterschied zu der Version mit sqlite: `execute` liefert auch für Abfragen keinen Rückgabewert. Stattdessen wird über den Cursor iteriert.


```python
conn = mysql.connector.connect(user="root", password="",
                               host="127.0.0.1", database="test")
c = conn.cursor()
c.execute("SELECT nr,name FROM personen")
for nr, name in c:
    print(nr, name)
    
conn.close()
```

    101 Peter
    102 Petra
    103 Hans
    104 Claudia


Die weitere Dokumentation von MySQL enthält verschiedene [Beispiele, die
den Umgang mit einer MySQL-Datenbank 
zeigen](https://dev.mysql.com/doc/connector-python/en/connector-python-examples.html).
Der wesentliche Unterschied besteht darin, wie eine Verbindung aufgebaut wird.
Nach dem Erzeugen eines Cursors mit ``cursor = eine_connection.cursor()`` kann
mit einem Aufruf von ``cursor.execute(...)`` wie im Falle von sqlite auf die 
Datenbank zugegriffen werden.

Das sehr ausführliche [Python MySQL-Tutorial](https://pynative.com/python-mysql-tutorial/)
geht auf viele Details genauer ein.

## NoSQL mit TinyDB

Jenseits von SQL gibt es noch verschiedene andere Ansätze, Daten in
Datenbanken zu verwalten - hierbei werden keine Tabellen verwendet. Einer
der Ansätze ist z.B. eine dokument-basierte Datenbank. Hier werden Daten
als Dokumente wie z.B. JSON abgelegt. 
[TinyDB](https://tinydb.readthedocs.io/) ist eine solche Datenbank für
Python.

### Installation

Die Installation erfolgt auch hier einfach mit Hilfe von pip:

    $ pip install tinydb


```python
import tinydb
```

Eine Datenbank kann mit der Klasse `TinyDB` leicht erzeugt werden. Wie bei sqlite werden die Daten direkt in einer Datei gespeichert.


```python
db = tinydb.TinyDB("db.json")
```

Die Datei `db.json` wurd als Textdatei angelegt. Wir können den Inhalt daher leicht betrachten und ggf. verändern.


```python
file db.json
```

    db.json: ASCII text, with no line terminators



```python
cat db.json
```

    {"_default": {}}

### Daten hinzufügen

Noch ist die Datenbank leer. Füllen wir sie also mir ein paar Daten. Die Daten können einfache Dictionaries seind.


```python
db.insert({"type": "apple", "count": 7})
```




    1




```python
db.insert({"type": "peach", "count": 3})
```




    2



Als Rückgabewert erhalten wir eine ID für den neuen Eintrag. Ein anschließender Blick in die Datei offenbart die neuen Inhalte.


```python
cat db.json
```

    {"_default": {"1": {"type": "apple", "count": 7}, "2": {"type": "peach", "count": 3}}}

Wir sehen einen Eintrag `_default`, der auf den Namen der Standardtabelle hinweist, mit der wir arbeiten. Dazu noch die hinzugefügten Einträge.

### Daten abfragen

Lassen wir uns alle Einträge einmal anzeigen.


```python
db.all()
```




    [{'type': 'apple', 'count': 7}, {'type': 'peach', 'count': 3}]



Über diese Liste aus Einzeleinträgen kann auch mit einer Schleife iteriert werden.


```python
for item in db:
    print(item, "Typ:", item["type"])
```

    {'type': 'apple', 'count': 7} Typ: apple
    {'type': 'peach', 'count': 3} Typ: peach


Bis jetzt haben wir noch nicht viel gewonnen gegenüber einer direkten Speicherung eines Dictionaries. Dokumentenbasierte Datenbanken wie TinyDB bieten jedoch die Möglichkeit komplexere Anfrage zu stellen.

Hierfür wird ein Query-Objekt erzeugt.


```python
query = tinydb.Query()
```

In der `search`-Methode kann das Query-Objekt für Abfragen genutzt werden.


```python
db.search(query.type == "apple")
```




    [{'type': 'apple', 'count': 7}]




```python
db.search(query.count < 5)
```




    [{'type': 'peach', 'count': 3}]



Mit `get` greifen wir auf das erste Ergebnis einer Suche zu. Jeder Eintrag in der Datenbank hat eine eindeutige ID, die über das Attribut `doc_id` abgefragt werden kann.


```python
apple = db.get(query.type == "peach")
apple.doc_id
```




    2



Mit der ID können Einträge auch direkt abgerufen werden.


```python
db.get(doc_id = 2)
```




    {'type': 'peach', 'count': 3}



### Daten aktualisieren

Auch Aktualisierungen werden über das Query-Objekt gemacht, wenn nicht alle Datensätze geändert werden sollen.


```python
db.update({"count": 10}, query.type == "apple")
```




    [1]



Wird keine Bedingung mit einem Query-Objekt verwendet, so werden alle Datensätze geändert.


```python
db.update({"new_key": "new_value"})
```




    [1, 2]




```python
db.all()
```




    [{'type': 'apple', 'count': 10, 'new_key': 'new_value'},
     {'type': 'peach', 'count': 3, 'new_key': 'new_value'}]



Schließlich löschen wir wieder alle Einträge.


```python
db.purge()
db.all()
```




    []



Und löschen auch die Datenbankdatei.


```python
rm db.json
```

Fortgeschrittene Anwendungen mit TinyDB werden im [Handbuch](https://tinydb.readthedocs.io/en/latest/usage.html) beschrieben. Hier werden Fragen zur Performance beantwortet und komplexere Anfragen beschrieben.
