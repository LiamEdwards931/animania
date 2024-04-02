from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('amendProducts', views.amendProducts, name='amendProducts'),
    path('newProduct', views.newProduct, name='newProduct'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('update_product/<int:product_id>/', views.update_product, name='update_product'),
    path('newSize/<int:product_id>', views.productSize, name='newSize'),
    path('updateSize/<int:product_id>', views.updateProductSize, name='updateSize'),
    path('new_banner', views.new_banner, name="newBanner"),
    path('amendbanners', views.amend_banner, name='amendbanners'),
    path('updatebanner/int<banner_id>',views.update_banner,name='updatebanner'),
    path('deletebanner/<int:banner_id>', views.delete_banner, name='deletebanner'),
    path('all_products', views.all_products, name='allproducts'),
    path('<product_id>', views.product_detail, name='product_details'),
    path('<int:product_id>/', views.product_review, name='productreview'),
]