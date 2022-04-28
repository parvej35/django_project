from django.urls import path
from . import views

# URL configuration
urlpatterns = [
    path('', views.say_hello),
    path('index/', views.say_hello),
    path('hello/', views.say_hello)
]
