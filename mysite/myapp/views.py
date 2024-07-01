from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
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

def add_book(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        
        if 'book_image' in request.FILES:
            book_image = request.FILES['book_image']
        else:
            book_image = None  

        book = Book(name=name, description=description, price=price, book_image=book_image)

        book.save()

        return HttpResponseRedirect('/')  

    return render(request, 'myapp/add_book.html')