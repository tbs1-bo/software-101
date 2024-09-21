# subscriber

import paho.mqtt.client as mqtt

MQTT_BROKER = "localhost" # "test.mosquitto.org"
TOPIC = "Erdgeschoss/Wohnzimmer/Temp"

def my_connect_method(client, userdata, flags, rc, properties):
    print("Connected. Subscribing to topic", TOPIC)
    client.subscribe(TOPIC)
    
def my_message_method(client, userdata, msg):
    msg_str = msg.payload.decode("UTF8")
    print(f"Message received. topic: {msg.topic} payload: {msg_str}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = my_connect_method
client.on_message = my_message_method

client.connect(MQTT_BROKER)

# client.loop_start()
client.loop_forever()
