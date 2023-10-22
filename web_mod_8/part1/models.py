from mongoengine import Document, StringField, ListField, ReferenceField

class Author(Document):
    fullname = StringField(required=True, max_length=100)
    born_date = StringField(required=True, max_length=50)
    born_location = StringField(required=True, max_length=150)
    description = StringField(required=True)
    
class Quotes(Document):
    tags = ListField(StringField(max_length=50))
    author = ReferenceField(Author, reverse_delete_rule=2)
    quote = StringField(required=True)