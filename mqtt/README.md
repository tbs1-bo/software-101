
# MQTT

[MQTT](https://de.wikipedia.org/wiki/MQTT) ist ein u.a. von IBM entwickeltes offenes Protokoll, das auf Port 1883 und 8883 (mit Verschlüsselung) läuft und für die Übertragung von Sensordaten zwischen Maschinen entwickelt wurde. Ein [Artikel bei heise](https://heise.de/-2168152) und ein [Artikel bei dzone](https://dzone.com/articles/mqtt-the-nerve-system-of-iot) beschreiben das Protokoll ausführlich.

## Broker

Bei der Kommunikation ist ein Broker beteiligt, der die Nachrichten empfangen und verteilen kann. Eine Implementierung ist "mosquitto", die über den Paket-Manager installiert werden kann.

    sudo apt install mosquitto
    
Für Testzwecke kann auch ein öffentlicher Broker von Eclipse verwendet werden.


```python
MQTT_BROKER = "iot.eclipse.org"
MQTT_PORT = 1883
```

## Clients

Mit dem Broker können nun verschiedene Clients kommunizieren. Hierbei kann ein Client ein Topic abonnieren oder Nachrichten in ein Topic schreiben.

Ein Topic ist ähnlich einer URL oder einem Dateipfad aufgebaut und verweist z.B. auf einen Sensor an einem bestimmten Ort.


```python
TOPIC = "Ergeschoss/Wohnzimmer/Temp"
```

Als Client-Bibliothek nutzen wir [paho-mqtt](https://pypi.python.org/pypi/paho-mqtt/). Diese lässt sich einfach installieren. 

- Windows: `pip install paho-mqtt` oder `python -m pip install paho-mqtt` oder `py -m pip install paho-mqtt`
- Linux, MacOS: `pip3 install paho-mqtt`

## Subscriber

Wir beginnen mit einem Client, der ein Topic abonniert und bei neuen Nachrichten eine Ausgabe auf die Konsole macht. Hierfür geben wir zwei Methoden an: eine, die aufgerufen wird, sobald eine Verbindung zum Broker zustande gekommen ist und eine, die bei jeder neuen Nachricht aufgerufen wird.


```python
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected. Subscribing to topic", TOPIC)
    client.subscribe(TOPIC)
    
def on_message(client, userdata, msg):
    print("Message received:", msg.topic, msg.payload)
```

Nun erstellen wir einen Client und legen die eben erstellten Callback-Methoden fest.


```python
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
```

Schließlich verbinden wir den Client mit dem Broker und warten auf neue Nachrichten.


```python
client.connect(MQTT_BROKER, MQTT_PORT, keepalive=60)
```




    0



Wenn der Client verbunden ist, wird eine Endlosschleife gestartet, die regelmäßig neue Nachrichten abruft. Es gibt verschiedene Varianten, diese Netzwerkschleife zu starten, die [hier](https://pypi.org/project/paho-mqtt/#network-loop) genauer beschrieben werden - `loop_start` startet den Abruf im Hintergrund, `loop_forever` startet die Netzwerkschleife im Fordergrund und blockiert damit die Anwendung ab diesem Aufruf.


```python
client.loop_start()
```

## Publisher

Erstellen wir nun einen weiteren Client, der in das Topic Nachrichten veröffentlicht.


```python
publisher = mqtt.Client()
publisher.connect(MQTT_BROKER, MQTT_PORT)
publisher.loop_start()
```

    Connected


Nun können wir eine Nachricht veröffentlichen. Wir sehen die Ausgabe aus unseren definierten Callback-Methoden, sobald die Nachricht eintrifft. 


```python
publisher.publish(topic=TOPIC, payload=22)
```




    <paho.mqtt.client.MQTTMessageInfo at 0x7f0f480732c8>



    Message received: Ergeschoss/Wohnzimmer/Temp b'22'

