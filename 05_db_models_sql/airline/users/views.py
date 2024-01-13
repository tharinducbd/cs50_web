from django.shortcuts import render, HttpResponsePermanentRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponsePermanentRedirect(reverse("login"))


def login_request(request):
    return render(request, "user/login.html")
