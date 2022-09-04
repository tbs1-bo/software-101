# python dotenv

Es macht einen Unterschied, ob eine Anwendung auf dem lokalen Rechner des Entwicklers
oder in einem Produktivsystem auf einem Server läuft. Unter Umständen gibt es 
unterschiedliche Werte für den Datenbank-Server oder Benutzerzugänge inklusive
Username und Passwort unterscheiden sich.

Es hat sich das Schema etabliert, Konfigurationswerte in Umgebungsvariablen abzulegen,
die von der Anwendung ausgelesen werden können - vgl dazu auch die Anforderungen an
eine [12factor](https://12factor.net/config)-Anwendung.

Für Python gibt es eine Unterstützung durch 
[python-dotenv](https://pypi.org/project/python-dotenv/).

Konfigurationen werden in `.env`-Dateien geschrieben, die nicht in der 
Versionsverwaltung abgelegt werden.


```python
cat .env
```

    DOMAIN=example.org
    ADMIN_EMAIL=admin@${DOMAIN}
    ROOT_URL=${DOMAIN}/app


Im nächsten Schritt wird die Datei geladen und die Einträge in Umgebungsvariablen abgelegt.


```python
from dotenv import load_dotenv

load_dotenv()
```




    True



Diese Werte können im Programm ausgelesen und genutzt werden.


```python
import os

DOMAIN = os.environ['DOMAIN']
ADMIN_EMAIL = os.environ['ADMIN_EMAIL']
ROOT_URL = os.environ['ROOT_URL']
```


```python
print(DOMAIN)
print(ADMIN_EMAIL)
print(ROOT_URL)
```

    example.org
    admin@example.org
    example.org/app

