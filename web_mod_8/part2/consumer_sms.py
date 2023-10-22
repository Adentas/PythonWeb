import pika
from models import Contact
from connect import connect_url

def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials)
    )
    
    channel = connection.channel()
    channel.queue_declare(queue='sms')
    
    def callback(ch, method, properties, body):
        contact_id = body.decode('utf-8')
        contact = Contact.objects(id=contact_id).first()
        if contact:
            contact.sent_sms = True
            contact.save()
            print(f"Sent sms to {contact.fullname} - {contact.phone}")
            
    channel.basic_consume(queue='sms', on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for sms messages. To exit press CTRL+C')
    channel.start_consuming()
    
if __name__ == "__main__":
    connect_url()
    main()