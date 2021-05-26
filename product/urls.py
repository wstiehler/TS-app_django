from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('product/', views.product, name='product'),
    path('product_form/', views.product_form, name='product_form'),
]
