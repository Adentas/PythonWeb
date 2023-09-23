import socket
import json
from datetime import datetime

# Ім'я файлу для зберігання даних
data_file = 'storage/data.json'

# Функція для зберігання даних у файлі JSON
def save_data(data):
    try:
        with open(data_file, 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {}
    
    existing_data.update(data)

    with open(data_file, 'w') as file:
        json.dump(existing_data, file, indent=2)

def main():
    # IP адреса та порт для прослуховування
    server_ip = '0.0.0.0'
    server_port = 5000

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((server_ip, server_port))

        print(f"Socket server is running on {server_ip}:{server_port}")

        while True:
            data, addr = s.recvfrom(1024)
            data = data.decode()

            # Обробка даних та збереження їх
            try:
                data = json.loads(data)
            except json.JSONDecodeError:
                print("Invalid JSON data received.")
                continue

            save_data(data)

if __name__ == '__main__':
    main()
