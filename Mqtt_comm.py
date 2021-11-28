# subscriber.py
import paho.mqtt.client as mqtt
import Data_database
import CSV_handler as ch
from datetime import datetime

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # subscribe, which need to put into on_connect
    # if reconnect after losing the connection with the broker, it will continue to subscribe to the raspberry/topic topic
    device_data = ch.showDevices()
    device_topics = device_data.Topic_pub
    for i in device_topics:
        client.subscribe(i)
        print(f"Subscribed to : {i}")

# the callback function, it will be triggered when receiving messages
def on_message(client, userdata, msg):
    print(f"{msg.topic} {msg.payload}")
    #Filter messages by topic and return payload into db
    if "TEMP" in msg.topic:
        now = datetime.now()
        dt_string = now.strftime("%d:%m:%Y:%H:%M:%S")
        return Data_database.log_data(dt_string,msg.topic,"97%",msg.payload)

def start_comm():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    # set the will message, when the Raspberry Pi is powered off, or the network is interrupted abnormally, it will send the will message to other clients
    client.will_set('raspberry/status', b'{"status": "Off"}')

    # create connection, the three parameters are broker address, broker port number, and keep-alive time respectively
    client.connect("192.168.0.29", 1883, 60)

    # set the network loop blocking, it will not actively end the program before calling disconnect() or the program crash
    client.loop_forever()

if __name__ == "__main__":
    start_comm()

#start_comm()