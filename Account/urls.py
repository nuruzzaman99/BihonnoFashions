from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login.as_view(), name='login'),
    path('registration', views.registration.as_view(), name='registration'),
    path('logout', views.logout, name='logout'),
]