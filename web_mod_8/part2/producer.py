import pika
from models import *
    
from connect import connect_url

def send_contact_queue(contact_id, method):
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    queue_name = "emails" if method == "email" else "sms"

    channel.queue_declare(queue=queue_name)
    channel.basic_publish(exchange='', routing_key=queue_name, body=str(contact_id))
    print(f"Sent Contact ID {contact_id} to {queue_name} queue")
    
    connection.close()
    
if __name__ == "__main__":
    connect_url()
    for _ in range(10):
        contact = create_fake_task()
        send_contact_queue(str(contact.id), contact.preferred_contact_method)