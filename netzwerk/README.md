
## Netzwerkprogrammierung

Die Netzwerkprogrammierung auf der Ebene von Sockets wird in Python über das Modul 
[socket](https://docs.python.org/3/library/socket.html)
realisiert. Ein 
[HOWTO socket programming](https://docs.python.org/3/howto/sockets.html)
beschreibt weitere Details.

Wir benötigen daher zunächst einen Import für das Modul `socket`.


```python
import socket
```

Ein Socket besteht immer aus eine IP-Adresse und einem Port. Für den Server wählen wir eine lokale Adresse und einen hohen Port.


```python
SERVER = ("127.0.0.1", 8181)
```

## Echo-Server

Der Echo-Server funktioniert ganz einfach. Er soll die Anfrage des Clients entgegennehmen und wieder zurücksenden.


```python
def run_server():
    # Creating socket and binding to IP, PORT
    server_socket = socket.socket()
    server_socket.bind(SERVER)
    server_socket.listen(5)  # 5 is a backlog of this many hanging connections
    
    print("SRV-THREAD: Waiting for connection")
    client_socket, address_info = server_socket.accept()  # wait until connection

    print("SRV-THREAD: Client connected from", address_info)
    data = client_socket.recv(128)
 
    print("SRV-THREAD: Recevied:", data)
    # Data is a bytes stream. Must be converted to a UTF8-String
    payload = "SERVER RECEIVED: " + str(data, "utf8")
    client_socket.send(bytes(payload, "utf8"))
    print("SRV-THREAD: finished")
    # closing server. Usually this will be run in a loop.
    server_socket.close()
```

Gewöhnlich wird der Server in einer eigenen Datei oder auf einem anderen Computer ausgeführt. Aus technischen Gründen wählen wir einen eigenen Thread, in dem der Server laufen soll.


```python
import threading
server_thread = threading.Thread(target=run_server)
server_thread.start()
```

    SRV-THREAD: Waiting for connection


## Client

Der Client verbindet sich zu IP und Port des Servers. In der Ausgabe ist der Port des Clients zu sehen, über den der Server mit diesem kommuniziert. Er wird zufällig gewählt. Die Ausgabe stammt vom Server-Thread.


```python
client_socket = socket.socket()
client_socket.connect(SERVER)
```

    SRV-THREAD: Client connected from ('127.0.0.1', 49662)


Die Daten müssen als Bytes gesendet und empfanden werden. Die Methode `bytes` hilft bei der Kovertierung von Zeichen in Bytes. Es sind Ausgaben des Servers und auch die Länge der gesendeten Daten in Bytes zu sehen.


```python
payload = bytes("Hallo Server", "utf8")
client_socket.send(payload)
```

    SRV-THREAD: Recevied:




    12



     b'Hallo Server'
    SRV-THREAD: finished


Der Server antwortet nun. Wir empfangen die Daten und geben sie aus.


```python
data = client_socket.recv(1024)
print("Client received from server:", data)
```

    Client received from server: b'SERVER RECEIVED: Hallo Server'


Schließlich wird der Socket geschlossen.


```python
client_socket.close()
```


```python

```
