# Custome create file to map all urls in 'blog' app

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="blog-home"),
    path('home/', views.home, name="blog-home"),
    path('about/', views.about, name="blog-about"),
]
