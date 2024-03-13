from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('amendProducts', views.amendProducts, name='amendProducts'),
    path('newProduct', views.newProduct, name='newProduct'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('update_product/<int:product_id>/', views.update_product, name='update_product'),
]