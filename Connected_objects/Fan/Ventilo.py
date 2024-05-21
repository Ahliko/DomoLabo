from machine import Pin
from network import WLAN, STA_IF
from umqtt.simple import MQTTClient
from motor import Motor
from time import sleep
from json import dumps, loads

class Ventilo:
    broker_address = "test.mosquitto.org"
    client_id = "esp32"
    topic = "1234"

    wifi_ssid = False
    wifi_password = False

    def __init__(self):
        self.wlan_sta = WLAN(STA_IF)
        self.wlan_sta.active(True)
        self.wlan_mac = str(self.wlan_sta.config('mac'))

        self.identity = {
            "name": "ventilo",
            "mac": self.wlan_mac
        }
        
        self.data_str = {
            "state": "0",
            "value": "0"
        }

        self.connection_response = {
            "identity": self.identity,
            "content": {
                "type": "response",
                "what": "add",
                "data": self.data_str
            }
        }

        self.data = {
            "identity": self.identity,
            "content": {
                "type": "response",
                "what":"data",
                "data": self.data_str
            }
        }

        self.motor = Motor(17, 18)

        # Initialize WiFi connection
        self.wifi = WLAN(STA_IF)
        self.wifi.active(True)

        while not Ventilo.wifi_ssid or not Ventilo.wifi_password:
            pass

        self.wifi.connect(Ventilo.wifi_ssid, Ventilo.wifi_password)
        while not self.wifi.isconnected():
            pass
        print("Connected to WiFi")

        self.client = MQTTClient(Ventilo.client_id, Ventilo.broker_address)
        self.client.set_callback(self.on_message)
        self.client.connect()
        self.client.subscribe(Ventilo.topic)

    def on_message(self, topic, message):
        print("Message reçu sur le topic {}: {}".format(topic, message))
        message = loads(message)
        print(message)
        
        if self.identity != message["identity"]:
            if message["content"]["type"] == "add":
                self.client.publish(topic, dumps(self.connection_response))

            elif message["content"]["type"] == "data":
                self.data_str = loads(message["content"]["data"])
                
                self.data["content"]["data"] = self.data_str
                print(int(self.data_str["value"]))
                print(dumps(self.data))
                self.client.publish(topic, dumps(self.data))
                self.motor.start(int(self.data_str["value"]))

    def main(self):
        while True:
            try:
                self.client.check_msg()
                sleep(0.1)
            except Exception as e:
                print("Exception occurred:", e)

