from django.contrib import admin
from .models import Intro

class AdminIntro(admin.ModelAdmin):
    list_display = ['name', 'offer']


# Register your models here.
admin.site.register(Intro, AdminIntro)
