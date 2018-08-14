# Datenbankzugriff

## Sqlite

Mit dem Python-Paket [sqlite3](https://docs.python.org/library/sqlite3.html)
kann auf  sqlite-Datenbanken direkt zugegriffen werden. Es muss daher nicht
installiert werden und ist bei jeder Python-Installation vorhanden.

Die Beispielanwendung [dbdemo.py](dbdemo.py) erstellt eine Beispieltabelle,
fügt ein paar Daten ein und gibt diese wieder aus.

## MySQL

Für den Zugriff auf eine MySQL-Datenbank muss zusätzlich ein 
[Connector für 
MySQL](https://dev.mysql.com/doc/connector-python/en/connector-python-installation-binary.html)
installiert werden. Dies kann z.B. mit dem folgenden Aufruf geschehen.

    $ pip install mysql-connector-python

Die weitere Dokumentation von MySQL enthält verschiedene [Beispiele, die
den Umgang mit einer MySQL-Datenbank 
zeigen](https://dev.mysql.com/doc/connector-python/en/connector-python-examples.html).
Der wesentliche Unterschied besteht darin, wie eine Verbindung aufgebaut wird.
Nach dem Erzeugen eines Cursors mit ``cursor = eine_connection.cursor()`` kann
mit einem Aufruf von ``cursor.execute(...)`` wie im Falle von sqlite auf die 
Datenbank zugegriffen werden.

Das sehr ausführliche [Python MySQL-Tutorial](https://pynative.com/python-mysql-tutorial/)
geht auf viele Details genauer ein.
