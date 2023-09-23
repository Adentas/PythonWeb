import os
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import socket

app = Flask(__name__)

# Функція для обробки форми на сторінці message.html
def handle_form(username, message):
    timestamp = str(datetime.now())
    data = {
        timestamp: {
            "username": username,
            "message": message
        }
    }
    return data

# Відправлення даних на Socket сервер
def send_to_socket_server(data):
    server_ip = '127.0.0.1'  # IP адреса Socket сервера
    server_port = 5000  # Порт Socket сервера

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.sendto(data.encode(), (server_ip, server_port))
    except Exception as e:
        print(f"Error sending data to Socket server: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message', methods=['GET', 'POST'])
def message():
    if request.method == 'POST':
        username = request.form['username']
        message = request.form['message']

        data = handle_form(username, message)
        send_to_socket_server(str(data))

        return redirect(url_for('index'))
    return render_template('message.html')

@app.errorhandler(404)
def not_found(e):
    return render_template('error.html'), 404

if __name__ == '__main__':
    app.run(port=3000, threaded=True)  # Запуск HTTP сервера на порту 3000
