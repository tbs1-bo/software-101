# Bottle

[Bottle](https://bottlepy.org) ist ein Webframework, das leicht mit pip
installiert werden kann.


## Installation


- Linux, MacOS: `pip3 install bottle`
- Windows: `pip install bottle` oder `python -m pip install bottle` oder `py -m pip install bottle`

## Einfacher Webserver

Für jeden Pfad, der aufgerufen werden kann, muss eine Route in Bottle deklariert
werden. Diese Methode muss einfaches HTML an den Browser liefern.


```python
import bottle
```

Wir beginnen mit der Route für `/`.


```python
@bottle.route("/")  # bindung route to a method
def index():
    return "OK"
```

Zum Starten des Webservers wird schließlich die Methode `bottle.run` verwendet.
Neben dem Parameter für den `host` und `port` gibt es die Option `reloader=True`.
Sie startet den Server automatisch neu, sobald sich eine der Python-Dateien geändert
hat. Bei der Entwicklung ist dies besonders hilfreich.


```python
bottle.run(host="127.0.0.1", port=8081)
```

    Bottle v0.12.13 server starting up (using WSGIRefServer())...
    Listening on http://127.0.0.1:8081/
    Hit Ctrl-C to quit.
    
    127.0.0.1 - - [30/Sep/2018 09:30:53] "GET / HTTP/1.1" 200 2


Unter http://127.0.0.1:8081 ist die Seite nun erreichbar. Ein Blick in den Quelltext zeigt, dass der Text `OK` genau so auftaucht, wie er in der Methode angelegt wurde.

## HTML

Unser Browser kann jedoch mehr als nur Text anzeigen. Er kann [HTML](https://www.w3schools.com/html) interpretieren. Passen wir die Methode also an und lassen valides HTML zurückgeben.


```python
@bottle.route("/")
def index():
    html = """
        <!DOCTYPE html>
        <html>
          <head><title>Bottle Demo</title></head>
          <body>
            <h1>Bottle-Demo</h1>
          </body>
        </html>
        """

    return html
```


```python
bottle.run(host="127.0.0.1", port=8081)
```

    Bottle v0.12.13 server starting up (using WSGIRefServer())...
    Listening on http://127.0.0.1:8081/
    Hit Ctrl-C to quit.
    
    127.0.0.1 - - [30/Sep/2018 09:31:00] "GET / HTTP/1.1" 200 182


## Dynamische Webseiten

Nun soll die Seite etwas dynamischer werden und einen Zeitstempel ausgeben, der sich bei jedem Aufruf ändert.


```python
import time

@bottle.route("/")
def index():
    html = """
        <!DOCTYPE html>
        <html>
          <head><title>Bottle Demo</title></head>
          <body>
            <h1>Bottle-Demo</h1>
            {sekseit1970} Sekunden seit dem 1.1.1970. 
          </body>
        </html>
        """

    # return HTML but replace variable in string before
    t = time.time()
    return html.format(sekseit1970=t)
```

Wenn wir den Server nun starten, wird bei jedem Aufruf der Zeitstempel im Ergebnis ersetzt.


```python
bottle.run(host="127.0.0.1", port=8081)
```

    Bottle v0.12.13 server starting up (using WSGIRefServer())...
    Listening on http://127.0.0.1:8081/
    Hit Ctrl-C to quit.
    
    127.0.0.1 - - [30/Sep/2018 09:31:06] "GET / HTTP/1.1" 200 242


## Bilder ausgeben

Schließlich soll noch ein Bild auf der Webseite erscheinen. Wir legen das folgende Bild neben die Python-Datei.

![Bild](ball.gif)


```python
@bottle.route("/")
def index():
    html = """
        <!DOCTYPE html>
        <html>
          <head><title>Bottle Demo</title></head>
          <body>
            <h1>Bottle-Demo</h1>
            <img src="/img/ball.gif" />
          </body>
        </html>
        """

    return html
```

In einem ersten Schritt schlägt die Anzeige jedoch fehl. Der Statuscode 404 hinter `/img/ball.gif` weist auf eine fehlende Route für das Bild hin.


```python
bottle.run(host="127.0.0.1", port=8081)
```

    Bottle v0.12.13 server starting up (using WSGIRefServer())...
    Listening on http://127.0.0.1:8081/
    Hit Ctrl-C to quit.
    
    127.0.0.1 - - [30/Sep/2018 09:35:42] "GET / HTTP/1.1" 200 222
    127.0.0.1 - - [30/Sep/2018 09:35:42] "GET /img/ball.gif HTTP/1.1" 404 744


In dem HTML-Dokument taucht eine Route `/img/` auf, für die bisher noch 
keine Methode angegeben wurde. Dies holen wir nun nach. Diese Methode 
soll jedoch kein HTML, sondern eine Bilddatei `/img/ball.gif` liefern.

Hierfür können wir die Methode `static_file` im bottle-Modul verwenden. Mit `root` wird das Wurzelverzeichnis für Bilder angegeben - in diesem Falle mit `.` das aktuelle Verzeichnis.


```python
@bottle.route("/img/ball.gif")
def image():
    return bottle.static_file(filename="ball.gif", root=".")
```

Wir testen auch diese Methode einmal und rufen sie direkt auf. Es fällt auf, dass nun kein HTML, sondern eine Binärdatei ausgeliefert wird.


```python
image()
```




    Content-Type: image/gif
    Content-Length: 5015
    Last-Modified: Thu, 09 Aug 2018 17:57:30 GMT
    Accept-Ranges: bytes



Starten wir den Webserver nun erneut.


```python
bottle.run(host="127.0.0.1", port=8081)
```

    Bottle v0.12.13 server starting up (using WSGIRefServer())...
    Listening on http://127.0.0.1:8081/
    Hit Ctrl-C to quit.
    
    127.0.0.1 - - [30/Sep/2018 09:31:44] "GET / HTTP/1.1" 200 222


## Dynamische Routen

Da es umständlich ist, für jedes Bild eine eigene Route festzulegen, können Routen auch dynamisch sein und einen Parameter enthalten - z.B. einen Dateiname für ein Bild. Dieser Parameter taucht dann auch in der Methode auf.


```python
@bottle.route("/img/<dateiname>")  # dynamic route
def image(dateiname):
    return bottle.static_file(filename=dateiname,  # parameter from method
                              root=".")
```

Die Parameter von dynamischen Routen können sogar an einen Datentyp gebunden werden. Dies wird in der [Dokumentation von Bottle zu "Request Routing"](http://bottlepy.org/docs/dev/tutorial.html#request-routing) beschrieben.

## Formulare

In HTML können mit Formularen Daten an den Webserver übertragen werden. Hierfür wird das [form-tag](https://wiki.selfhtml.org/wiki/HTML/Formulare/form) genutzt. Das `action`-Attribut gibt das Ziel des Formulares an, mit `method` kann die HTTP-Methode für die Übertragung gesetzt werden.


```python
@bottle.route("/formular")
def fomular():
    return """
    <!DOCTYPE html>
    <html>
      <head><title>Bottle Demo</title></head>
      <body>
        <h1>Bottle-Formular</h1>

        <form action="/formularauswerter" method="POST">
            <input type="textfield" name="eingabefeld"><br>
            <input type="submit" value="Absenden">
        </form>
        
      </body>
    </html>
    """
```

Das Formular leitet an die Route `/formularauswerter` weiter. Und zwar mit einem `POST`-Request. Hierfür muss noch eine Methode angegeben werden. Diesmal wird `bottle.post` als Dekorator verwendet.


```python
@bottle.post("/formularauswerter")
def fomularauswerter():
    html = """
    <!DOCTYPE html>
    <html>
      <head><title>Bottle Demo</title></head>
      <body>
        <h1>Bottle-Formular-Auswerter</h1>
        Es wurde "{req}" eingegeben.
      </body>
    </html>
    """
    formulareingabe = bottle.request.forms["eingabefeld"]

    return html.format(req=formulareingabe)
```


```python
bottle.run(host="127.0.0.1", port=8081)
```

    Bottle v0.12.13 server starting up (using WSGIRefServer())...
    Listening on http://127.0.0.1:8081/
    Hit Ctrl-C to quit.
    
    127.0.0.1 - - [30/Sep/2018 09:32:01] "GET /formular HTTP/1.1" 200 348
    127.0.0.1 - - [30/Sep/2018 09:32:05] "POST /formularauswerter HTTP/1.1" 200 199


Nun ist das Formular unter http://localhost:8081/formular erreichbar.

## Templates

Damit der HTML-Quelltext nicht mit dem Python-Quelltext verschmischt wird, trennt man beide. Dadurch können Änderungen am Design durchgeführt werden, ohne den Quelltext dafür ändern zu müssen.

[Templates](http://bottlepy.org/docs/dev/tutorial.html#templates) werden im Ordner `views` abgelegt. Dort legen wir folgende einfache HTML-Datei `index.tpl` ab. Sie enthält den Platzhalter `{{mein_text}}`, der noch ersetzt werden muss. (Die erste Zeile mit writefile ist nicht Teil der Datei.)


```python

<!DOCTYPE html>
    <html>
    <head><title>Bottle Demo</title></head>
    <body>
        <h1>Bottle-Template</h1>
        Hallo {{mein_text}}
    </body>
</html>
```



Das Template kann nun angezeigt und die Variable `mein_text` darin ersetzt werden. Dies erledigt die Methode `template`.


```python
@bottle.route('/')
def index():
    return bottle.template('index', mein_text='Welt')
```

Nach einem Start wird das Template angezeigt und die Variable darin ersetzt.


```python
bottle.run(host='127.0.0.1', port=8081)
```

    Bottle v0.12.13 server starting up (using WSGIRefServer())...
    Listening on http://127.0.0.1:8083/
    Hit Ctrl-C to quit.
    
    127.0.0.1 - - [14/Nov/2018 08:58:36] "GET / HTTP/1.1" 200 154
    127.0.0.1 - - [14/Nov/2018 08:58:37] "GET /favicon.ico HTTP/1.1" 404 742


## Templates mit Kontrollstrukturen

Innerhalb des Templates können nicht nur Variablen angezeigt, sondern auch Kontrollstrukturen wie Schleifen verwendet werden. Das ist besonders nützlich, wenn eine Liste mit Werten angezeigt werden soll.

Das nächste Beispiel zeigt ein Template, in dem eine Liste durchlaufen wird. Hierfür wird Python-Quelltext mit einem vorangestellten `%` im Python-Quelltext eingetragen. Da die sonst bei Python wichtige Einrückung im Template keine Rolle spielt, muss das Ende der Schleife mit einem `end` gekennzeichnet werden.


```python

<!DOCTYPE html>
    <html>
    <head><title>Bottle Demo</title></head>
    <body>
        <h1>Bottle-Template</h1>
        Eine Liste mit {{ len(meine_liste) }} Elementen
        <ul>
        % for eintrag in meine_liste:
            <li>{{ eintrag }}</li>
        % end
        </ul>
    </body>
</html>
```



Beim Aufruf der Webseite wird nun eine Liste übergeben.


```python
@bottle.route('/')
def index():
    return bottle.template('index', 
                           meine_liste=["eins", "zwei", "drei"])
```


```python
bottle.run(host='127.0.0.1', port=8081)
```

    Bottle v0.12.13 server starting up (using WSGIRefServer())...
    Listening on http://127.0.0.1:8082/
    Hit Ctrl-C to quit.
    
    127.0.0.1 - - [14/Nov/2018 09:18:29] "GET / HTTP/1.1" 200 275
    127.0.0.1 - - [14/Nov/2018 09:18:29] "GET /favicon.ico HTTP/1.1" 404 742


## Cheat-Sheet

In einem [Cheat-Sheet](bottle-cheatsheet.pdf) werden die wichtigsten Dinge
zusammenfasst.

