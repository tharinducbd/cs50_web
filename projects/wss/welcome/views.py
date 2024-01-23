from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def hello(request):
    return HttpResponse("Hello, world from WSS!")


def greet(request, name):
    return HttpResponse(f"Hi, {name.capitalize()}! \nWelcome to WSS App.")


def index(request):
    return render(request, "welcome/index.html")
