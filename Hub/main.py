from Application import Application
import Request
import time
import MQTTConfig
import json
from paho.mqtt import client as mqtt_client
from crud import Crud

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
    result = client.publish(str(topic), message)
    status = result[0]
    if status == 0:
        pass
    else:
        print(f"Local |    Failed to send message to topic {topic}")



def subscribe(client: mqtt_client, crud):
    def on_message(client, userdata, msg):
        request = str(msg.payload.decode("utf-8"))
        reply, response, dest, needResponse = Request.processRequest(request, msg.topic, crud)
        print(msg.topic)
        if reply:
            unique_dest = set(dest)

            for ta in unique_dest:
                if ta not in MQTTConfig.currentSubscription:
                    try:
                        client.subscribe(ta)
                    except:
                        pass
                    finally:
                        MQTTConfig.currentSubscription.append(ta)
                
                publish(client, response, ta)
                        

                if "disponible" in response:
                    publish(client, Request.getRequest_HubOK(), ta)
              
    try:
        client.subscribe(MQTTConfig.topicApp)
    except:
        pass
    finally:
        MQTTConfig.currentSubscription.append(MQTTConfig.topicApp)
    
    client.on_message = on_message

def on_start(client, objs):
    for obj in objs:
        publish(client=client , message=Request.getRequest_ObjData(), topic=obj)

def run():
    crud = Crud("db.db")
    crud.select_all_app()
    client = connect_mqtt()
    subscribe(client, crud)
    client.loop_forever()
    on_start(client, crud.select_all_obj())

if __name__ == '__main__':
    run()