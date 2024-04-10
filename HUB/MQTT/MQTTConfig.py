import random

broker = "test.mosquitto.org"
port = 1883
#topicApp="mytopicweather"
topicApp = "ac863f346e618f9a959b5c95d5d28941/#"
client_id = f'python-mqtt-{random.randint(0, 100)}'
currentSubscription = []