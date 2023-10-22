import redis
import re
from models import Author, Quotes
from redis_lru import RedisLRU

client = redis.StrictRedis(host='localhost', port=6379, password=None)
cache = RedisLRU(client)

@cache
def search_by_name(name):
    authors = Author.objects(fullname=name)
    if not authors:
        return []
    author = authors[0]
    return Quotes.objects(author=author)

@cache
def search_by_tag(tag):
    return Quotes.objects(tags=tag)

@cache
def search_by_set_tags(tags_list):
    return Quotes.objects(tags__in=tags_list)

@cache
def search_by_name_partial(name):
    pattern = re.compile(f'^{name}', re.IGNORECASE)
    authors = Author.objects(fullname=pattern)
    if not authors:
        return []
    author = authors[0]
    return Quotes.objects(author=author)

@cache
def search_by_tag_partial(tag):
    pattren = re.compile(f'^{tag}', re.IGNORECASE)
    return Quotes.objects(tags=pattren)