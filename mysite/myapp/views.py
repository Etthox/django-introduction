from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book
from .forms import BookForm


def index(request):
    book_list = Book.objects.all()
    context = {
        'book_list':book_list
    }
    return render(request, 'myapp/index.html',context)

def details(request,id):
    book = Book.objects.get(id=id)
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

def update_book(request,id):
    book = Book.objects.get(id=id)
    form = BookForm(request.POST or None, request.FILES, instance=book)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'myapp/edit_book.html',{'form':form,'book':book})

def delete_book(request,id):
    book = Book.objects.get(id=id)
    if request.method == "POST":
        book.delete()
        return HttpResponseRedirect('/')  
    return render(request, 'myapp/delete.html')