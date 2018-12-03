
# MQTT

[MQTT](https://de.wikipedia.org/wiki/MQTT) ist ein u.a. von IBM entwickeltes offenes Protokoll, das auf Port 1883 und 8883 (mit Verschlüsselung) läuft und für die Übertragung von Sensordaten zwischen Maschinen entwickelt wurde. Ein [Artikel bei heise](https://heise.de/-2168152) und ein [Artikel bei dzone](https://dzone.com/articles/mqtt-the-nerve-system-of-iot) beschreiben das Protokoll ausführlich.

## Broker

Bei der Kommunikation ist ein Broker beteiligt, der die Nachrichten empfangen und verteilen kann. Eine Implementierung für einen solchen Broker ist "mosquitto". Er kann über den Paket-Manager installiert werden.

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

Als Client-Bibliothek für Python nutzen wir [paho-mqtt](https://pypi.python.org/pypi/paho-mqtt/). Diese lässt sich einfach installieren. 

- Windows: `python -m pip install paho-mqtt` oder `py -m pip install paho-mqtt`
- Linux, MacOS: `python3 -m pip install paho-mqtt`

## Subscriber

Wir beginnen mit einem Client, der ein Topic abonniert und bei neuen Nachrichten eine Ausgabe auf die Konsole macht. Hierfür geben wir zwei callback-Methoden an.

1. `my_connect_method` soll aufgerufen werden, sobald eine Verbindung zum Broker zustande gekommen ist.
2. `my_message_method` soll bei jeder neuen Nachricht aufgerufen werden.


```python
import paho.mqtt.client as mqtt

def my_connect_method(client, userdata, flags, rc):
    print("Connected. Subscribing to topic", TOPIC)
    client.subscribe(TOPIC)
    
def my_message_method(client, userdata, msg):
    print("Message received:", msg.topic, msg.payload)
```

Nun erstellen wir einen Client und legen die eben erstellten Callback-Methoden fest.


```python
client = mqtt.Client()
client.on_connect = my_connect_method
client.on_message = my_message_method
```

Schließlich verbinden wir den Client mit dem Broker und warten auf neue Nachrichten.


```python
client.connect(MQTT_BROKER, MQTT_PORT, keepalive=60)
```




    0



Wenn der Client verbunden ist, wird eine Endlosschleife gestartet, die regelmäßig neue Nachrichten abruft. Es gibt verschiedene Varianten, diese Netzwerkschleife zu starten, die [hier](https://pypi.org/project/paho-mqtt/#network-loop) genauer beschrieben werden.

- `loop_start` startet den Abruf im Hintergrund, 
- `loop_forever` startet die Netzwerkschleife im Fordergrund und blockiert damit die Anwendung ab diesem Aufruf.


```python
client.loop_start()
```

    Connected. Subscribing to topic Ergeschoss/Wohnzimmer/Temp


## Publisher

Erstellen wir nun einen weiteren Client, der in dem Topic Nachrichten veröffentlicht.


```python
publisher = mqtt.Client()
publisher.connect(MQTT_BROKER, MQTT_PORT)
publisher.loop_start()
```

Nun können wir eine Nachricht veröffentlichen. Wir sehen die Ausgabe aus unseren definierten Callback-Methoden, sobald die Nachricht eintrifft. 


```python
publisher.publish(topic=TOPIC, payload=22)
```




    <paho.mqtt.client.MQTTMessageInfo at 0x7f1172eb3318>



    Message received: Ergeschoss/Wohnzimmer/Temp b'22'


## Dashboard

Ein Dahsboard für MQTT ermöglicht es, Werte im Broker zu visualisieren. [Node-RED](https://nodered.org/) ist eine IOT-Plattform, die mit dem Raspberry Pi ausgeliefert wird. Es kann um ein [Dahboard](https://flows.nodered.org/node/node-red-dashboard) erweitert werden. Hierzu wird in Node-RED im Menü "Manage Palette" > "Install" aufgerufen. In der Suchmaske kann mit `node-red-dashboard` ein solches Dashboard hinzugefügt werden.
