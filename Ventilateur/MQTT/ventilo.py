from machine import Pin
from simple import MQTTClient
import time
import network
import json

# Remplacez ces informations par celles de votre broker MQTT
BROKER_ADDRESS = "test.mosquitto.org"
CLIENT_ID = "esp32"
TOPIC = "mytopicObject"

# Configurations Wi-Fi
WIFI_SSID = "Manon"
WIFI_PASSWORD = "lollollol"

wlan_sta = network.WLAN(network.STA_IF)
wlan_sta.active(True)
wlan_mac = wlan_sta.config('mac')

identity = {
        "name" : "ventilo",
        "mac": str(wlan_mac)
    }

connection_response = {
    "identity" : identity,
    "content": {
    "type":"response",
        "what":"connection",
        "response":"disponible",
    }
}

data_str = {
            "state":"0",
            "value":"0"
        }

data = {
    "identity" : identity,
    "content":{
        "type":"data",
        "data":json.dumps(data_str)
    }
}

# Initialise le client MQTT
client = MQTTClient(CLIENT_ID, BROKER_ADDRESS, port=1883)

motor=Pin(26,Pin.OUT)

# Fonction de callback lors de la réception d'un message
def on_message(topic, message):
    print("Message reçu sur le topic {}: {}".format(topic, message))
    message = message.decode()
    message = json.loads(message)
    if not (message["identity"] == identity) : 
        if (message["content"]["type"] == "connection"):
            client.publish(topic, json.dumps(connection_response))
            client.publish(topic, json.dumps(data))
        elif (message.decode() == "1"):
            client.publish(topic, json.dumps("ventilo running"))
            motor.value(1)
            data_str["state"] = "1"
            data_str["value"] = "1"
            data['content']['data'] = json.dumps(data_str)
            client.publish(topic, json.dumps(data))
        elif (message.decode() == "0"):
            client.publish(topic, json.dumps("ventilo stopped"))
            motor.value(0)
            data_str["state"] = "1"
            data_str["value"] = "0"
            data['content']['data'] = json.dumps(data_str)
            client.publish(topic, json.dumps(data))



# Configure la fonction de callback
client.set_callback(on_message)

# Connexion Wi-Fi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASSWORD)
while not wifi.isconnected():
    pass

# Connexion MQTT
client.connect()
client.subscribe(TOPIC)

try:
    while True:
        client.check_msg()
        time.sleep(1)
except KeyboardInterrupt:
    print("Arrêt de la connexion MQTT.")
    client.disconnect()
