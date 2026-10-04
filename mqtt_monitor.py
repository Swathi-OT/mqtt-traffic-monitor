import paho.mqtt.client as mqtt
from datetime import datetime

BROKER = "localhost"
PORT = 1883
LOG_FILE = "mqtt_traffic.log"

SUSPICIOUS_KEYWORDS = ["shutdown", "override", "emergency", "stop", "reset"]

def on_message(client, userdata, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    topic = message.topic
    payload = message.payload.decode("utf-8", errors="ignore")
    
    log_entry = f"[{timestamp}] TOPIC: {topic} | PAYLOAD: {payload}"
    print(log_entry)
    
    # Check for suspicious keywords
    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword.lower() in payload.lower():
            alert = f"[ALERT] Suspicious keyword '{keyword}' detected!"
            print(alert)
            with open(LOG_FILE, "a") as f:
                f.write(alert + "\n")
    
    with open(LOG_FILE, "a") as f:
        f.write(log_entry + "\n")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Connected to MQTT Broker at {BROKER}")
        client.subscribe("#")  # Subscribe to ALL topics
        print("Subscribed to all topics — monitoring started")
    else:
        print(f"Connection failed with code {rc}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

print("MQTT Traffic Monitor — Swathi S")
print("Starting monitoring...")
client.connect(BROKER, PORT, 60)
client.loop_forever()
