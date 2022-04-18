# main_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('drinks/', views.drinks_index, name='drinks_index'),
]