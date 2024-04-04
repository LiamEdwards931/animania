from django.urls import path
from .import views


urlpatterns = [
    path('news', views.news, name='news'),
    path('create_news', views.create_news, name='create_news')
]