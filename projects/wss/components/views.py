from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

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
        "tanks": scheme.list_tanks.all(),
        "treatment_processes": scheme.list_treatments.all(),
        "unavailable_tanks": Tank.objects.exclude(sch_tanks=scheme).all(),
    })


def add_tank(request, scheme_id):
    if request.method == "POST":
        scheme = Scheme.objects.get(id=scheme_id)

        tank_id = int(request.POST["selected_tank"])
        new_tank = Tank.objects.get(id=tank_id)
        new_tank.sch_tanks.add(scheme)

        return HttpResponseRedirect(reverse("components:scheme", args=(scheme_id,)))
