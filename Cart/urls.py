from django.urls import path
from . import views

urlpatterns = [
    path('cartDetail', views.cartDetail.as_view(), name='cartDetail'),
    path('checkout', views.checkout.as_view(), name='checkout'),
    path('orderHistory', views.orderHistory.as_view(), name='orderHistory'),
]