import json
from models import Author, Quotes
from connect_to_mongodb import connect_url

def load_data():
    with open('output/quotes.json', 'r', encoding='utf-8') as f:
        quotes_data = json.load(f)
    
    with open('output/authors.json', 'r', encoding='utf-8') as f:   
        authors_data = json.load(f)

    return quotes_data, authors_data

if __name__ == "__main__":
    connect_url()
    quotes_data, authors_data = load_data()
    
    for quote in quotes_data:
        Quotes(**quote).save()

    for author in authors_data:
        Author(**author).save()
    
    print("All data loaded successfully!")