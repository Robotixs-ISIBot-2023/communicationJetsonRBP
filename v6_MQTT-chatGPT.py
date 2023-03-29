import asyncio
import json
import time
import random
import paho.mqtt.client as mqtt

# Configurations
BROKER_HOST = "172.30.16.20"
BROKER_PORT = 1883
TOPIC = "test"

# Fonction de callback appelée lorsqu'un message est reçu pour le topic abonné
def on_message(client, userdata, message):
    print(f"Message reçu sur le topic {message.topic}: {message.payload.decode()}")

# Fonction principale
async def main():
    # Connexion au broker MQTT
    client = mqtt.Client()
    client.connect(BROKER_HOST, BROKER_PORT)

    # Configuration du callback pour la réception de messages
    client.on_message = on_message

    # Abonnement au topic
    client.subscribe(TOPIC)

    # Initialisation de la variable pour stocker la dernière valeur reçue
    last_payload = None

    # Boucle principale
    while True:
        # Envoi de données
        data = {"temperature": random.uniform(20.0, 25.0), "humidity": random.uniform(40.0, 50.0)}
        payload = json.dumps(data)
        client.publish(TOPIC, payload)
        print(f"Données envoyées: {payload}")

        # Attente de 1 seconde
        await asyncio.sleep(1)

        # Vérification si de nouvelles données ont été reçues
        if last_payload != client.payload:
            # Affichage de la nouvelle valeur reçue
            print(f"Nouvelle donnée reçue: {client.payload}")
            last_payload = client.payload
