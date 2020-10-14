import time

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect('10.175.1.155', 1883, 600) # 600为keepalive的时间间隔

for i in range(20):
    time.sleep(1)
    print("send msg %s", i)
    client.publish('fifa', payload=f"send msg {i}", qos=0)