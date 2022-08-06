from django.contrib import admin
from .models import Order

class AdminOrder(admin.ModelAdmin):
    list_display = ['Customer', 'date', 'status']

# Register your models here.
admin.site.register(Order, AdminOrder)
