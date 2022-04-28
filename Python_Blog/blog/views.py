from django.shortcuts import render
from django.http import HttpResponse


def home1(request):
    return HttpResponse("<h1> Blog Home Page</h1>")


def home(request):
    return render(request, "blog/home.html")


def about1(request):
    return HttpResponse("<h1> Blog About Page</h1>")


def about(request):
    return render(request, "blog/about.html")
