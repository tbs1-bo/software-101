# publisher

import paho.mqtt.client as mqtt

MQTT_BROKER = "localhost" # "test.mosquitto.org"
TOPIC = "Erdgeschoss/Wohnzimmer/Temp"

publisher = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
publisher.connect(MQTT_BROKER)
publisher.loop_start()

input("Press Enter to publish message")
publisher.publish(topic=TOPIC, payload=22)

input("Press Enter for next message (retained)")
publisher.publish(topic=TOPIC, payload="23 ret", retain=True)

input("Press Enter to exit")
