import random
import json
import time
import requests

# URL endpoint POST server Flask
url = "http://localhost:5000/api/data"  # Gantilah dengan URL server Anda

def send_sensor_data():
    while True:
        # Menyusun payload dengan data acak
        payload = {
            "charts": [
                {"chart_name": "Temperature", "value": random.randint(15, 30)},  # Temperatur acak antara 15-30
                {"chart_name": "Humidity", "value": random.randint(40, 80)},     # Kelembaban acak antara 40-80
                {"chart_name": "LDR", "value": random.randint(10, 100)}           # LDR acak antara 10-100
            ]
        }

        # Mengirim data ke server dengan metode POST
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                print(f"Sent data: {json.dumps(payload)}")
            else:
                print(f"Failed to send data: {response.status_code}, {response.text}")
        except Exception as e:
            print(f"Error sending data: {e}")
        
        # Tunggu selama 2 detik sebelum mengirim data berikutnya
        time.sleep(2)

# Menjalankan simulasi pengiriman data
send_sensor_data()
