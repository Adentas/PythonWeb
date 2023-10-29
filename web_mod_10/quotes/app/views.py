from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import RegisterAuthorForm, RegisterQuoteForm
from .connect_db import uri
from django.core.paginator import Paginator 

# Create your views here.
def quotes_view(request, page=1):
    db = uri.quotes_db
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'app/index.html', context={'quotes': quotes_on_page})

def author_detail(request, author_name_url):
    db = uri.quotes_db
    author_name = author_name_url.replace('%20', ' ')
    author = db.author.find_one({'fullname': author_name})
    return render(request, 'app/author.html', context={'author': author})



@login_required
def add_author(request):
    if request.method == 'POST':
        form = RegisterAuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='app:quotes_view')
        else:
            return render(request, 'app/add_author.html', {'form': form})
    return render(request, 'app/add_author.html', {'form': RegisterAuthorForm()})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = RegisterQuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save(commit=False)
            new_quote.save()
            return redirect(to='app:quotes_view')
        else:
            return render(request, 'app/add_quote.html', {'form': form})
    return render(request, 'app/add_quote.html', {'form': RegisterQuoteForm()})