import datetime
from django.db import models
from Product.models import Product
from Account.models import Customer

# Create your models here.

class Order(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
