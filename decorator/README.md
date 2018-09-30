
# Decorator unter Python

Dekoratoren sind ein fortgeschrittenes Konzept in Python. Sie kommen an vielen unterschiedlichen Stellen zum Einsatz.


    @app.route("/home")
    def home():
        return render_template("index.html")

    @performance_analysis
    def foo():
        pass

    @property
    def total_requests(self):
        return self._total_requests


Wir können sie am besten verstehen, indem wir anschauen, was in Python mit Methoden alles möglich ist.


```python
def get_hello_function(punctuation):
    """Returns a hello world function, with or without punctuation."""

    def hello_world():
        print("Hello world")

    def hello_world_punctuated():
        print("Hello, world!")

    if punctuation:
        return hello_world_punctuated
    else:
        return hello_world
```

Die Funktion `get_hello_function` gibt eine Funktion zurück. Je nachdem, welchen Wert der Parameter `punctuation` hat.


```python
ready_to_call = get_hello_function(punctuation=True)

ready_to_call()
```

    Hello, world!


Die Methode, die wir bei dem Aufruf von `get_hello_function` erhalten, wird in einer Variablen gespeichert und kann dann aufgerufen werden. Wir testen es auch mit der anderen Variante:


```python
ready_to_call = get_hello_function(punctuation=False)

ready_to_call()
```

    Hello world


Nun schreiben wir eine Funktion, die eine weitere Funktion als Parameter besitzt. Diese Funktion wird in eine andere Funktion eingewickelt und dann als Ergebnis zurückgegeben. Durch das Einwickeln wird in diesem Beispiel der Aufruf um einige Sekunden verzögert, bevor die Funktion aufgerufen wird.


```python
from time import sleep

def delayed_func(func):
    """Return a wrapper which delays `func` by 10 seconds."""
    def wrapper():
        print("Waiting for some seconds...")
        sleep(3)
        # Call the function that was passed in
        func()

    return wrapper


def print_phrase(): 
    print("Fresh Hacks Every Day")
```


```python
delayed_print_function = delayed_func(print_phrase)
delayed_print_function()
```

    Waiting for some seconds...
    Fresh Hacks Every Day


Das sieht irgendwie verwirrend aus. Wichtig ist, dass wir die Funktionalität von `func` selbst nicht verändert haben. Sie wurde um eine weitere Funktionalität ergänzt - mit dieser *dekoriert*.

Im nächsten Schritt verschönern wir die Dekoration etwas. Python hat für das Einwickeln eine spezielle Notation mit einem @-Zeichen.


```python
from time import sleep

def delayed_fun(func):
    """Return `func`, delayed by 10 seconds."""
    def wrapper():
        print("Waiting for some seconds...")
        sleep(3)
        func()
        
    return wrapper

@delayed_func
def print_phrase():
    print("Fresh Hacks Every Day")
```


```python
print_phrase()
```

    Waiting for some seconds...
    Fresh Hacks Every Day


Durch die Annotation von `print_phrase` mit `@delayed_func` wird die Funktion `print_phrase` durch eine andere Funktion ersetzt, die eine verzögerte Ausführung bewirkt.

## Nützlich?!

Warum ist das nützlich? Dekoratoren können Funktionen nicht in ihrem Verhalten verändern; aber sie können sie um neues Verhalten erweitern. Hierfür gibt es viele verschiedene Anwendungen - z.B. für das Debugging.

Schreiben wir nun einen Dekorator, der eine Zeitmessung durchführt.


```python
import datetime
import time

def log_performance(func):
    def wrapper():
        now = datetime.datetime.now()
        print("Function called at " + str(now))
        start = time.time()
        func()
        delta = time.time() - start
        print("Execution took " + str(delta) + " seconds")
        
    return wrapper
```

Mit dem neuen Dekorator `log_performance` können Funktionsaufrufe nun gemessen werden.


```python
@log_performance
def calculate_squares():
    for i in range(10000000):
        i_sq = i**2
        
calculate_squares()
```

    Function called at 2018-09-02 16:44:03.682970
    Execution took 2.4941389560699463 seconds


## Parameter

Die bisherigen Beispiele haben Funktionen ohne Parameter verwendet. Der Dekorator `log_performance` soll aber mit beliebigen Funktionen umgehen können - also auch mit solchen, die Parameter entgegennehmen.


```python
import datetime
import time

def log_performance(func):
    def wrapper(*args, **kwargs):
        now = datetime.datetime.now()
        print("Function called at " + str(now))
        start = time.time()
        result = func(*args, **kwargs)
        delta = time.time() - start
        print("Execution took " + str(delta) + " seconds")

        return result
    
    return wrapper
```

Der wrapper wird nun mit einer Liste `args` oder einem Dictionary `kwargs` aufgerufen - `kw` steht hierbei für *keyword*.


```python
@log_performance
def calculate_squares(n):
    """Calculate the squares of the numbers 0 to n."""
    for i in range(n):
        i_squared = i**2

calculate_squares(10000000)
```

    Function called at 2018-09-02 16:44:06.205656
    Execution took 2.4768545627593994 seconds


## Validierung

Eine weitere sinnvolle Anwendung von Dekoratoren kann die Validierung von Rückgabewerten sein - z.B. von Ports für Netzwerkkonfigurationen.


```python
def get_server_addr():
    """Return IP address and port of server."""
    ...
    return ('192.168.1.0', 8080)

def get_proxy_addr():
    """Return IP address and port of proxy."""
    ...
    return ('127.0.0.1', 12253)
```


```python
get_server_addr()
```




    ('192.168.1.0', 8080)




```python
get_proxy_addr()
```




    ('127.0.0.1', 12253)



Die Validierung der Rückgabewerte dieser beiden Funktionen soll durch den folgenden Dekorator `validate_port` geprüft werden.


```python
PORTS_IN_USE = [1500, 1834, 7777, 8080]

def validate_port(func):
    def wrapper(*args, **kwargs):
        # Call `func` and store the result
        result = func(*args, **kwargs)
        ip_addr, port = result

        if port < 1024:
            raise ValueError("Cannot use priviledged ports below 1024")
        elif port in PORTS_IN_USE:
            raise RuntimeError("Port " + str(port) + " is already in use")

        # If there were no errors, return the result
        return result
    return wrapper
```

Nun können die beiden oben definierten Funktion mit dem neuen Dekorator versehen werden.


```python
@validate_port
def get_server_addr():
    """Return IP address and port of server."""
    ...
    return ('192.168.1.0', 8080)

@validate_port
def get_proxy_addr():
    """Return IP address and port of proxy."""
    ...
    return ('127.0.0.1', 12253)
```

Der Vorteil bei diesem Vorgehen: Die Validierung wird außerhalb der Kernfunktionalität der Netzwerkfunktionen durchgeführt.


```python
try:
    get_server_addr()
except RuntimeError as ve:
    print("Error:", ve)
```

    Error: Port 8080 is already in use



```python
get_proxy_addr()
```




    ('127.0.0.1', 12253)



## Dokumentation von Funktionen

Angenommen, wir wollen Metdaten zu unseren Funktionen abrufen - z.B. den Name oder die Dokumentation.


```python
get_server_addr.__name__
```




    'wrapper'




```python
get_server_addr.__doc__
```

Der Name der Funktion hat sich geändert und der Dokumentationsstring ist verschwunden. Das ist nicht, was wir erwarten. Es ist aber verständlich, da durch den Dekorator die Funktion ausgetauscht wurd. Leider wurden hierbei die Metadaten nicht ersetzt.

Gott sei Dank wurde dieses Problem schon im Modul `functools` gelöst. Hier gibt es eine Dekorator `wraps`, der alle Metadaten ergänzt.


```python
from functools import wraps

def validate_port(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        ip_addr, port = result
        
        if port < 1024:
            raise ValueError("Cannot use priviledged ports below 1024")
        elif port in PORTS_IN_USE:
            raise RuntimeError("Port " + str(port) + " is already in use")

        # If there were no errors, return the result
        return result
    
    return wrapper
```

Mit diesem neuen Dekorator können wir die Methoden erneut dekorieren. Die Metadaten bleiben nun erhalten.


```python
@validate_port
def get_server_addr():
    """Return IP address and port of server."""
    ...
    return ('192.168.1.0', 8080)

@validate_port
def get_proxy_addr():
    """Return IP address and port of proxy."""
    ...
    return ('127.0.0.1', 12253)
```


```python
get_server_addr.__name__
```




    'get_server_addr'




```python
get_server_addr.__doc__
```




    'Return IP address and port of server.'



## Quelle

Dieses Tutorial basiert auf einem [Artikel bei hackaday](https://hackaday.com/2018/08/31/an-introduction-to-decorators-in-python/).
