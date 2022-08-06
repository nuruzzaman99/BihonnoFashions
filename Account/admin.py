from django.contrib import admin

from .models import Customer


class AdminCustomer(admin.ModelAdmin):
    list_display = ['name', 'email']

# Register your models here.
admin.site.register(Customer, AdminCustomer)
