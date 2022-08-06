from django.contrib import admin
from .models import Category, Product


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name', 'total_item']

# Register your models here.
admin.site.register(Category, AdminCategory)
admin.site.register(Product, AdminProduct)
