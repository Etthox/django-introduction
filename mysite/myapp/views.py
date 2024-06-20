from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def index(request):
    book_list = Book.objects.all()
    return HttpResponse(book_list)


def products(request):
    return HttpResponse('There are some Products:')
