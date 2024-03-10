from django.urls import path
from . import views
from .views import register

urlpatterns = [
   path('accounts/', views.profile, name='profile'),
   path("signup/", register, name="signup"),
]


