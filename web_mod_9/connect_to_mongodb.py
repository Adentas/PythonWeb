from mongoengine import connect
import configparser

def connect_url():
    config = configparser.ConfigParser()
    config.read('config.ini')

    mongo_user = config.get('MongoDB', 'mongo_user')
    mongodb_pass = config.get('MongoDB', 'mongodb_pass')
    mongodb_name = config.get('MongoDB', 'mongo_db')
    domain = config.get('MongoDB', 'domain')

    connect(host=f"""mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{mongodb_name}?retryWrites=true&w=majority""", ssl=True)