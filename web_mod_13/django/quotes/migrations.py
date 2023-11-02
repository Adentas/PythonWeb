import os
import django
import configparser
from pymongo import MongoClient

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quotes.settings")
django.setup()

from quotes_app.models import Author, Tag, Quotes

def connect_url():
    config = configparser.ConfigParser()
    config.read("../quotes/utils/config.ini")

    mongo_user = config.get('MongoDB', 'mongo_user')
    mongodb_pass = config.get('MongoDB', 'mongodb_pass')
    domain = config.get('MongoDB', 'domain')

    uri = MongoClient(f"mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/?retryWrites=true&w=majority""", ssl=True)

    return uri

uri = connect_url()
db = uri.quotes_db
authors = db.author.find()
for author in authors:
    Author.objects.get_or_create(
        fullname=author['fullname'],
        born=author['born'],
        location=author['location'],
        bio=author['bio']
    )

quotes = db.quotes.find()

for text in quotes:
    tags = []
    for tag in text['tags']:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)
    
    exist_quote = bool(len(Quotes.objects.filter(text=text['text'])))
    if not exist_quote:
        author = db.author.find_one({'_id': text['author']})
        if author:
            a = Author.objects.get(fullname=author['fullname'])
        else:
            a, created = Author.objects.get_or_create(fullname="Unknown Author")
        
        q = Quotes.objects.create(
            text=text['text'],
            author=a
        )
        for tag in tags:
            q.tags.add(tag)
            print(tag)