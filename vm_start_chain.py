import paho.mqtt.client as mqtt
import time

# Define callback function for connection
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

# Define callback function for publishing
def on_publish(client, userdata, mid):
    print("Message published with ID: " + str(mid))

# Define MQTT client instance
client = mqtt.Client()

# Set the username and password for the MQTT client
client.username_pw_set(username="password", password="password")

# Set the callback functions
client.on_connect = on_connect
client.on_publish = on_publish

# Connect to the MQTT broker
client.connect("172.20.10.2", 1883, 60)

# Loop until connection is established
client.loop_start()

while True:
    # Publish a message with topic "YOUR_USERNAME/ping" and an integer number as payload
    message = input("Enter a number to publish: ")
    client.publish("YOUR_USERNAME/ping", message)
    print("Message published: " + message)
    time.sleep(1)

# Disconnect from the MQTT broker
client.loop_stop()
client.disconnect()
