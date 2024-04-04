from django.urls import path
from .import views


urlpatterns = [
    path('news', views.news, name='news'),
    path('create_news', views.create_news, name='create_news'),
    path('news_detail/<int:news_id>', views.news_detail, name='news_detail'),
]