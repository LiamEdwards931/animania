from django.urls import path, include
from .import views


urlpatterns = [
    path('checkout', views.checkout, name='checkout'),
    path('checkout_success/<order_number>',
         views.checkout_success, name='checkoutSuccess')
]
