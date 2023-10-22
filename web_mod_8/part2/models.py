from mongoengine import Document, StringField, BooleanField
from faker import Faker
import random

fake = Faker()

class Contact(Document):
    fullname = StringField(required=True)
    email = StringField(required=True)
    phone = StringField(required=True)
    preferred_contact_method = StringField(choices=["email", "sms"], required=True)
    sent_email = BooleanField(default=False)
    sent_sms = BooleanField(default=False)
    
    
def create_fake_task():
    method = fake.random_element(elements=('email', 'sms'))
    contact = Contact(
        fullname=fake.name(),
        email=fake.email(),
        phone=fake.phone_number(),
        preferred_contact_method=method
        
    )
    contact.save()
    return contact