import random
import json
from paho.mqtt import client as mqtt_client
from uuid import getnode as get_mac

# --------------------------------------------------

class Application:
    def __init__(self, identity, topic):
        self.identity = identity
        self.topic = topic

global APPLICATIONS
APPLICATIONS = []



broker = "test.mosquitto.org"
port = 1883
# HASH MD5 de App
topicApp = "ac863f346e618f9a959b5c95d5d28941/#"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'

identity = {
    "name":"Hub",
    "mac": str(get_mac())
}


obj = {
    "1234": {
        "name":"Joseph",
        "topic":"fffff",
        "state":"0",
        "value":"0",
    }
}

request = {
    "identity":identity,
    "content":{
        "type":"response",
        "what":"connection",
        "response":"ok",
        "data":json.dumps(obj)
        
    }
}

requestDisponible = {
    "identity":identity,
    "content":{
        "type":"response",
        "what":"connection",
        "response":"disponible",
    }
}

# --------------------------------------------------

def connect_mqtt() -> mqtt_client:
    def on_connect(client:mqtt_client, userdata, flags, rc):
        if rc == 0:
            print("Local |    Connected to MQTT Broker!")
        else:
            print("Local |    Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

# --------------------------------------------------

def publish(client, message, topic):

    result = client.publish(topic, message)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        pass
        #print(f"Local |    Send `{message}` to topic `{topic}`")
    else:
        print(f"Local |    Failed to send message to topic {topic}")


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        s = str(msg.payload.decode("utf-8"))
        print(f"MQTT  |    {s} | {msg.topic}")
        try:
            re = json.loads(s)

            if (re['content']['type'] == "connection"):
                publish(client, json.dumps(requestDisponible), msg.topic)
                
                publish(client, json.dumps(request), msg.topic)
                APPLICATIONS.append(Application(re["identity"], msg.topic))
        except:
            pass
        

    client.subscribe(topicApp)
    client.on_message = on_message

# --------------------------------------------------

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


# --------------------------------------------------

if __name__ == '__main__':
    run()

# --------------------------------------------------