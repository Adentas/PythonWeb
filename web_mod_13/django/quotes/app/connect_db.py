import configparser
from pymongo import MongoClient

def connect_url():
    config = configparser.ConfigParser()
    config.read("./utils/config.ini")

    mongo_user = config.get('MongoDB', 'mongo_user')
    mongodb_pass = config.get('MongoDB', 'mongodb_pass')
    domain = config.get('MongoDB', 'domain')

    uri = MongoClient(f"mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/?retryWrites=true&w=majority""", ssl=True)

    return uri

uri = connect_url()
db = uri.mongodb