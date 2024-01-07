from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from .models import Flight, Passenger


# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    # 'pk' is same as 'id', which is a django's sqlite feature
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(), # 'passengers' is the related name!
    })

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
