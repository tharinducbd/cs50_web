from django.http import HttpResponse
from django.shortcuts import render

from .models import Scheme, Tank, TreatmentProcess


# Create your views here.
def index(request):
    return render(request, "components/index.html", {
        "tanks": Tank.objects.all(),
        "schemes": Scheme.objects.all(),
        "treatment_processes": TreatmentProcess.objects.all()
    })


def tank(request, tank_id):
    tank = Tank.objects.get(id=tank_id)
    return render(request, "components/tank.html", {
        "tank": tank,
        "schemes": tank.schemes.all()
    })
