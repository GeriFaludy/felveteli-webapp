from django.shortcuts import render

from django.http import HttpResponse 

from APP.models import Book

def index(request):
    return HttpResponse('Hello world')

def book_by_id(request, book_id):
    book = book.objects.get(pk=book_id)
    return HttpResponse(f"Book: {book.title}, published on {book.pub_date}")
