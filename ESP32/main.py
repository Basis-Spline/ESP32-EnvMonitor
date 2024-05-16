# main.py
import network
import urequests
import time
from machine import Pin
import dht

# Replace with your network credentials
SSID = 'your_SSID'
PASSWORD = 'your_PASSWORD'

# Replace with your Flask server IP and port
SERVER_URL = 'http://your_server_ip:5000/data'

# Initialize DHT22 sensor
dht_pin = Pin(4)
sensor = dht.DHT22(dht_pin)

# Connect to WiFi
def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    while not wlan.isconnected():
        time.sleep(1)
    
    print('Connected to WiFi')
    print('IP:', wlan.ifconfig()[0])

# Read from DHT22 and send data to the server
def read_and_send_data():
    try:
        sensor.measure()
        temperature = sensor.temperature()
        humidity = sensor.humidity()
        print(f'Temperature: {temperature} °C, Humidity: {humidity} %')

        data = {
            'temperature': temperature,
            'humidity': humidity
        }
        response = urequests.post(SERVER_URL, json=data)
        print('Response:', response.text)
        response.close()
    except Exception as e:
        print('Failed to read sensor or send data:', e)

def main():
    connect_wifi(SSID, PASSWORD)
    while True:
        read_and_send_data()
        time.sleep(10)

if __name__ == '__main__':
    main()
