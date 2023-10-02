import os
import django

# import sys

# Add the path to your Django project's settings module to the Python path.
# sys.path.append('/path/to/your/django_project')

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rtd.settings")
django.setup()


# mqtt_listener.py
import paho.mqtt.client as mqtt
from django.conf import settings
from channels.layers import get_channel_layer
import json
from rtdApp.models import *
import websocket


websocket_url = "ws://127.0.0.1:8000/ws/dashboard/"

# Create a WebSocket connection
ws = websocket.WebSocket()
# Connect to the WebSocket 
print("before")
ws.connect(websocket_url)

def on_message(client, userdata, message):
    print("Received MQTT Message:")
    print("Topic:", message.topic)
    print("Payload:", message.payload.decode())
    try:
        payload = json.loads(message.payload.decode())
        timestamp = payload['timestamp']
        value = payload['value']
        print("Timestamp:", timestamp)
        print("Value:", value)
        print("after")

        # Define the data you want to send
        data = {
            "timestamp": timestamp,
            "value": value
        }

        # Convert the data to a JSON string
        data_json = json.dumps(data)

        # Send the data to the WebSocket server
        ws.send(data_json)

        # Close the WebSocket connection when done
        
        print("done")
        # channel_layer = get_channel_layer()
        # async_to_sync(channel_layer.group_send)("test_consumer_group", {"type": "send.notification", "value": camera_data_list})
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)

# client = mqtt.Client()

# def connect_mqtt():
#     # Connect to the MQTT broker and subscribe to the topic(s)
#     client.connect("broker.hivemq.com", 1883)
#     client.subscribe("mqtt_data_topic")
#     print("in")
#     client.on_message = on_message

# def start_mqtt_listener():
#     # Start the MQTT listener loop
#     client.loop_start()
#     connect_mqtt()

# start_mqtt_listener()
# while True:
#     client.on_message = on_message
client = mqtt.Client()
client.on_message = on_message

# Connect to the MQTT broker and subscribe to a topic
client.connect("broker.hivemq.com", 1883)
client.subscribe("mqtt_data_topic")

# Start the MQTT client loop to continuously listen for messages
client.loop_start()

# Keep the program running
try:
    while True:
        pass
except KeyboardInterrupt:
    ws.close()
    # Gracefully exit the program on Ctrl+C
    client.disconnect()