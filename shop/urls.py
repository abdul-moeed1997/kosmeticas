from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('products/', views.products, name='products'),
    path('products/<int:myid>', views.product_details, name='product-details'),
    path('aboutUs/', views.about, name='AboutUs'),
    path('search/', views.search, name='Search'),
    path('checkout/', views.checkout, name='checkout'),
    path('contactUs/', views.contact, name='ContactUs'),
    path('tracker/', views.tracker, name='tracker'),
    path('checkout/', views.checkout, name='checkout')
]