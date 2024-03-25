from django.urls import path
from . import views

urlpatterns = [
   path('basket/', views.basket, name="basket"),
   path('add/<item_id>', views.add_to_basket, name='add_to_basket'),
   path('update/<item_id>',views.adjust_bag, name='update_basket'),
   path('delete/<item_id>', views.remove_from_bag, name='delete_basket'),
]