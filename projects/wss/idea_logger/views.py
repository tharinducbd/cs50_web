from django.shortcuts import render


ideas = [
    "Including every possible component",
    "An option to incorporate the size at least approximately",
    "Auto-generate the inputs required",
    "The ability to define new components",
    "The ability to define new inputs for the defined components",
]


# Create your views here.
def index(request):
    return render(request, "idea_logger/index.html", {
        "ideas": ideas
    })


def add(request):
    return render(request, "tasks/add.html")
