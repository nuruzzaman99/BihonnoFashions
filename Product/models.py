from tkinter import CASCADE
from django.db import models

# Create your models here.
class Category(models.Model):
    image = models.ImageField(upload_to = 'image/categories')
    name = models.CharField(max_length=100)
    total_item = models.IntegerField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to = 'image/products')
    image2 = models.ImageField(upload_to = 'image/products')
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    price = models.IntegerField()
    offerprice = models.IntegerField()
    code = models.IntegerField()
    trendy = models.BooleanField(default=False)
