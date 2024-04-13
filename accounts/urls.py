from django.urls import path
from . import views
from .views import register

urlpatterns = [
   path('accounts/', views.profile, name='profile'),
   path("signup/", register, name="signup"),
   path("changepassword/", views.changePassword, name="changepassword"),
   path("addaddress/", views.addAddress, name="addaddress"),
   path('address/delete/<int:address_id>/',
        views.delete_address, name='delete_address'),
   path('update_address/<int:address_id>/',
        views.update_address, name='update_address'),
   path('myreviews', views.my_reviews, name='my_reviews'),
   path('review/delete/<int:review_id>/',
        views.delete_review, name='delete_review'),
   path('update_review/<int:review_id>/',
        views.update_review, name='update_review'),
]
