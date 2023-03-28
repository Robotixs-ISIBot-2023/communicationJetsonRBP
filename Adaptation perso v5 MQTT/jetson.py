import paho.mqtt.client as mqtt
import time

# MQTT broker address
broker_address = "localhost"

# Define the function to handle incoming messages
def on_message(client, userdata, message):
    print("Received message on topic {}: {}".format(message.topic, message.payload))
    print(int(message.payload.decode()))

# Create a client instance
client = mqtt.Client()

# Connect to the broker
client.connect(broker_address)

# Start the background thread for MQTT communication
client.loop_start()

# Send a message every 5 seconds
counter = 0
while True:
    # Send a message to topic "main_move"
    message = 10750 # Go forward 750 mm
    client.publish("main_move", message) # main & secondary | HERE : Main
    #message = -90
    #client.publish("main_move", message)

    # Wait 5 seconds
    time.sleep(5)

    # Check for new messages on topic "main_move_forward"
    client.subscribe("main_captor_laser")
    client.on_message = on_message  # Define the function to handle incoming messages

    # Increment the counter
    counter += 1
