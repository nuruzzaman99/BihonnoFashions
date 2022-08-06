from django.db import models

# Create your models here.
class Intro(models.Model):
    image = models.ImageField(upload_to = 'image/intro')
    name = models.CharField(max_length=500)
    offer = models.CharField(max_length=500)

    def __str__(self):
        return self.name
