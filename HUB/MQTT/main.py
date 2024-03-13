from Application import Application
import Request
import MQTTConfig

import json
from paho.mqtt import client as mqtt_client

def connect_mqtt() -> mqtt_client:
    def on_connect(client:mqtt_client, userdata, flags, rc):
        if rc == 0:
            print("Local |    Connected to MQTT")
        else:
            print("Local |    Failed to connect : %d\n", rc)

    client = mqtt_client.Client(MQTTConfig.client_id)

    client.on_connect = on_connect
    client.connect(MQTTConfig.broker, MQTTConfig.port)
    return client


def publish(client, message, topic):
    result = client.publish(topic, message)
    status = result[0]
    if status == 0:
        pass
        #print(f"Local |    Send `{message}` to topic `{topic}`")
    else:
        print(f"Local |    Failed to send message to topic {topic}")



def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        request = str(msg.payload.decode("utf-8"))
        print(f"{msg.topic}  |    {request}")
        needResponse, response, dest = Request.processRequest(request, msg.topic)
        print(needResponse)
        if needResponse:
            for to in dest:
                if to not in MQTTConfig.currentSubscription:
                    try:
                        client.subscribe(to)
                    except:
                        pass
                    finally:
                        MQTTConfig.currentSubscription.append(to)
                
                publish(client, response, to)

                if "disponible" in response:
                    publish(client, Request.getRequest_HubOK(), to)

            
    try:
        client.subscribe(MQTTConfig.topicApp)
    except:
        pass
    finally:
        MQTTConfig.currentSubscription.append(MQTTConfig.topicApp)
    
    client.on_message = on_message





def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    run()