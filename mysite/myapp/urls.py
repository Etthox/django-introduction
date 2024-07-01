from django.contrib import admin
from django.urls import path,include
from myapp import views

app_name= 'myapp'

urlpatterns = [
    path('', views.index,name='index'),
    path('products/', views.products,name='products'),
    path('book/<int:book_id>/', views.details, name='details'),
    path('add/', views.add_book, name='add_book')
]
    

