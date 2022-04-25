from django.shortcuts import render

from django.http import HTTpResponse 

from .models import book

def index(request):
    return HTTpResponse('Hello world')

def book_by_id(request, book_id):
    book = book.objects.get(pk=book_id)
    return HTTpResponse(f"Book: {book.title}, published on {book.pub_date}")
