# ESP32-EnvMonitor

A project for reading environmental data from an ESP32 and sending it to a Flask server.

## ESP32 Setup

1. Flash MicroPython firmware to your ESP32.
2. Upload `main.py` to your ESP32.

### Libraries Required

- `micropython-urequests`
- `micropython-dht`

### main.py

This script reads temperature and humidity data from a DHT22 sensor and sends it to a Flask server over WiFi.

## Flask Server Setup

1. Install Flask:
   ```bash
   pip install flask
