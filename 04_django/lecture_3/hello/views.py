from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def say_hello(request):
    return HttpResponse("Hello, world from Django!")


def greet(request, name):
    return HttpResponse(f"Hello, {name} from the world of Django!!")



