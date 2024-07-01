from django.db import models


class Book(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.IntegerField()
    book_image = models.ImageField(default='default_book.jpg',upload_to='book_images/')