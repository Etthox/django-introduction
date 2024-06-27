from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def index(request):
    book_list = Book.objects.all()
    context = {
        'book_list':book_list
    }
    return render(request, 'myapp/index.html',context)

def details(request,book_id):
    book = Book.objects.get(id=book_id)
    return render(request, "myapp/detail.html",{'book': book})

def products(request):
    return HttpResponse('There are some Products:')
