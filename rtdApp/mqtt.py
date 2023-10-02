import paho.mqtt.client as mqtt
import json
import time

# Define MQTT broker details
broker_address = "broker.hivemq.com"
broker_port = 1883
# broker_address = "127.0.0.1"
# broker_port = 5672
topic = "mqtt_data_topic"

# Create an MQTT client instance
client = mqtt.Client()

# Connect to the MQTT broker
client.connect(broker_address, broker_port)

while True:
    # Simulate data from your IoT device
    data = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime()),
        "value": 42.0  # Replace with your actual data
    }

    # Publish the data as a JSON string to the specified topic
    client.publish(topic, json.dumps(data))
    # client.publish(json.dumps(data))

    # Sleep for a second before sending the next data
    time.sleep(1)

# Keep the MQTT client running or use an appropriate exit strategy
# client.loop_forever()
