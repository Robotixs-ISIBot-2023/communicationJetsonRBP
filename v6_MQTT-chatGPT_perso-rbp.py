import asyncio
import json
import time
import random
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe

# Configurations
BROKER_HOST = "172.30.16.20"
BROKER_PORT = 1883
TOPIC = "main_move"
TOPIC2 = "main_captor_laser"

# Fonction de callback appelée lorsqu'un message est reçu pour le topic abonné
def on_message(client, userdata, message):
    print(f"Message reçu sur le topic {message.topic}: {message.payload.decode()}")
    # Pour prendre qu'une donnée d'un topic choisi
    """
    if (message.topic == "main_move") :
        global Commande
        Commande = int(message.payload.decode())
    """
    
# Connexion au broker MQTT
client = mqtt.Client()
client.connect(BROKER_HOST, BROKER_PORT)

# Configuration du callback pour la réception de messages
#client.on_message = on_message

# Abonnement au topic
#client.subscribe(TOPIC)
subscribe.callback(on_message, TOPIC, hostname=BROKER_HOST, port=BROKER_PORT)

# Initialisation de la variable pour stocker la dernière valeur reçue
#last_payload = None

# Boucle principale
while True:
    # Envoi de données
    data = {"temperature": random.uniform(20.0, 25.0), "humidity": random.uniform(40.0, 50.0)}
    payload = json.dumps(data)
    client.publish(TOPIC2, payload)
    print(f"Données envoyées: {payload}")

        