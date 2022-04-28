from django.http import HttpResponse
from django.shortcuts import render

from django.http import HttpRequest

# Create your views here.

# request -> response
# request handler
# action


def say_hello(request):
    # return HttpResponse("Hi Parvej")
    return render(request, 'hello.html', {'name1': 'Parvej'})
