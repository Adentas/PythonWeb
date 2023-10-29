from django.forms import ModelForm, CharField, TextInput
from .models import Author, Quotes

class RegisterAuthorForm(ModelForm):

    fullname = CharField(min_length=5, max_length=50, required=True, widget=TextInput())
    born = CharField(min_length=10, required=True, widget=TextInput())
    location = CharField(min_length=10, required=True, widget=TextInput())
    bio = CharField(min_length=10, required=True, widget=TextInput())

    class Meta:
        model = Author
        fields = ['fullname','born','location', 'bio']
        
class RegisterQuoteForm(ModelForm):

    quote = CharField(min_length=5, required=True, widget=TextInput())
    author = CharField(min_length=5, required=True, widget=TextInput())
    tags = CharField(min_length=5, required=True, widget=TextInput())
    
    class Meta:
        model = Quotes
        fields = ['quote', 'author', 'tags']
        exclude = ['author','tags']