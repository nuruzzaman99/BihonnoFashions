from django.urls import path
from . import views

urlpatterns = [
    path('by_category', views.by_category.as_view(), name='by_category'),
    path('by_id', views.by_id.as_view(), name='by_id'),
]