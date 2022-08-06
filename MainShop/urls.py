from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('shop', views.shop.as_view(), name='shop'),
    path('shopDetail', views.shopDetail.as_view(), name='shopDetail'),
    path('contact', views.contact.as_view(), name='contact'),
    path('profile', views.profile.as_view(), name='profile'),
]