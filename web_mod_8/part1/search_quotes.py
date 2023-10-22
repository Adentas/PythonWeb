from connect import *
from commands import *

def search_by_name(name):
    authors = Author.objects(fullname=name)
    if not authors:
        return []
    author = authors[0]
    return Quotes.objects(author=author)

def search_by_tag(tag):
    return Quotes.objects(tags=tag)

def search_by_set_tags(tags_list):
    return Quotes.objects(tags__in=tags_list)


def search_by_name_partial(name):
    pattern = re.compile(f'^{name}', re.IGNORECASE)
    authors = Author.objects(fullname=pattern)
    if not authors:
        return []
    author = authors[0]
    return Quotes.objects(author=author)

def search_by_tag_partial(tag):
    pattren = re.compile(f'^{tag}', re.IGNORECASE)
    return Quotes.objects(tags=pattren)

def main_search_loop():
    while True:
        command_input = input("Enter search command: ")
        if command_input == "exit":
            break
        command, value = command_input.split(":", 1)
        
        if ":" not in command_input:
            print("Invalid command format. Please use 'command:value'.")
        
        if command == "name":
            quotes = search_by_name_partial(value)
        elif command == "tag":
            quotes = search_by_tag_partial(value)
        elif command == "tags":
            tags = value.split(",")
            quotes = search_by_set_tags(tags)
        else:
            print("Unkown command.")
            continue
        
        if not quotes:
            print("Qoutes not found.")
        
        for quote in quotes:
            print(quote.quote.encode('utf-8').decode('utf-8'))           
            
connect_url()
main_search_loop()