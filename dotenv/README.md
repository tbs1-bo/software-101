# python dotenv

Es macht einen Unterschied, ob eine Anwendung auf dem lokalen Rechner des Entwicklers
oder in einem Produktivsystem auf einem Server läuft. Die Frage, wo Konfigurationswerte
abgelegt werden ...

https://12factor.net/config

https://pypi.org/project/python-dotenv/


```python
!cat .env
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
```


```python
ADMIN_EMAIL = os.environ['ADMIN_EMAIL']
```


```python
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



```python

```
