from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def say_hello(request):
    return HttpResponse("Hello, world from Django!")


def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()} from the world of Django!!")


def render_hello(request):
    return render(request, "hello/render_hello.html")


def render_greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
