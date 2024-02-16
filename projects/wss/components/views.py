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
        "schemes": tank.sch_tanks.all()
    })


def scheme(request, scheme_id):
    scheme = Scheme.objects.get(id=scheme_id)
    return render(request, "components/scheme.html", {
        "scheme": scheme,
        "tanks": scheme.sch_tanks.all(),
        "treatment_processes": scheme.sch_treatments.all()
    })
