# MQTT Traffic Monitor

A beginner-friendly MQTT traffic monitoring tool developed as part of my OT/IoT Security learning journey.

## Overview

This project monitors MQTT traffic by subscribing to MQTT topics and analyzing incoming messages.

The tool displays MQTT messages with their timestamp, topic, and payload. It also uses simple keyword-based rules to detect potentially suspicious commands.

## Features

- Connects to an MQTT broker
- Subscribes to MQTT topics
- Monitors incoming MQTT messages
- Displays timestamp, topic, and payload
- Detects suspicious keywords
- Generates alerts for potentially suspicious commands
- Saves MQTT traffic to a log file

## Technologies Used

- Python 3
- MQTT
- Mosquitto MQTT Broker
- Paho MQTT
- Kali Linux

## Requirements

Before running the project, make sure you have:

- Python 3
- Mosquitto MQTT Broker
- Mosquitto MQTT Clients
- Paho MQTT Python library

## Installation

### 1. Install Mosquitto

```bash
sudo apt update
sudo apt install mosquitto mosquitto-clients -y
2. Start the MQTT Broker
sudo systemctl start mosquitto
3. Create a Python Virtual Environment
python3 -m venv venv

Activate the virtual environment:

source venv/bin/activate
4. Install Paho MQTT
pip install paho-mqtt
Usage
1. Run the MQTT Traffic Monitor
python3 mqtt_monitor.py

This starts the MQTT Traffic Monitor and allows it to receive MQTT messages from the broker.

2. Publish a Test MQTT Message

Open another terminal and run:

mosquitto_pub -t "sensor/temperature" -m "25.5"

The MQTT Traffic Monitor should receive and display the message.

3. Test Suspicious Commands

Test a shutdown command:

mosquitto_pub -t "plant/control" -m "shutdown"

Test an override command:

mosquitto_pub -t "factory/valve" -m "override pressure"

The monitor can identify suspicious keywords such as:

shutdown
override
emergency

and generate an alert.

Example

Example MQTT message:

TOPIC: sensor/temperature
PAYLOAD: 25.5

Example suspicious message:

TOPIC: plant/control
PAYLOAD: shutdown

Example alert:

[ALERT] Suspicious keyword 'shutdown' detected!
Detection Approach

The current version uses simple keyword-based rules to identify potentially suspicious MQTT commands.

This is a beginner-level implementation intended for learning about MQTT monitoring and basic Intrusion Detection System concepts.

Future Improvements
Add more detection rules
Detect abnormal MQTT message rates
Add MQTT authentication monitoring
Support MQTT over TLS
Add machine-learning-based anomaly detection
Develop a monitoring dashboard
Extend monitoring to other OT/ICS protocols such as Modbus
Project Purpose

This project is part of my learning journey in:

OT Cybersecurity
IoT Security
MQTT Security
Network Monitoring
Intrusion Detection Systems

Author

Swathi S

M.Tech IoT | OT/IoT Security Learner

