from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('', views.quotes_view, name='quotes_view'),
    path("<int:page>", views.quotes_view, name="root_paginator"),
    path('author/<str:author_name_url>/', views.author_detail, name='author_detail'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_quote/', views.add_quote, name='add_quote'),
]