from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.email