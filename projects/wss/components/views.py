from django.http import HttpResponse
from django.shortcuts import render

from .models import Tank


# Create your views here.
def index(request):
    return render(request, "components/index.html", {
        "tanks": Tank.objects.all()
    })
