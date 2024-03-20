from django.urls import path
from . import views
from .views import register

urlpatterns = [
   path('accounts/', views.profile, name='profile'),
   path("signup/", register, name="signup"),
   path("changepassword/", views.changePassword, name="changepassword"),
   path("addaddress/", views.addAddress, name="addaddress"),
   path('address/delete/<int:address_id>/', views.delete_address, name='delete_address'),
   path('update_address/<int:address_id>/', views.update_address, name='update_address'),
   path('review/delete/<int:review_id>/', views.delete_review, name='delete_review'),
]


