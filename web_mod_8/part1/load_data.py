import json
from models import Author, Quotes
from connect import *

with open('../data/authors.json', 'r') as f:
    authors_data = json.load(f)
    
with open('../data/quotes.json', 'r') as f:
    quotes_data = json.load(f)
    
authors_map = {}
for author in authors_data:
    author_doc = Author(**author).save()
    authors_map[author['fullname']] = author_doc
    
for quote in quotes_data:
    quote['author'] = authors_map[quote['author']]
    Quotes(**quote).save()

# if __name__ == "__main__":      
print("All data loaded successfully!")