import paho.mqtt.client as mqtt
import time

# MQTT broker address
broker_address = "172.30.40.78"

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
    # Send a message to topic "main_move_forward"
    message = 10
    client.publish("main_captor_laser", message)

    # Wait 5 seconds
    time.sleep(5)

    # Check for new messages on topic "main_move_forward"
    client.subscribe("main_move_forward")
    client.subscribe("main_move_turn")
    client.on_message = on_message  # Define the function to handle incoming messages

    # Increment the counter
    counter += 1
