from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


ideas = [
    "Including every possible component",
    "An option to incorporate the size at least approximately",
    "Auto-generate the inputs required",
    "The ability to define new components",
    "The ability to define new inputs for the defined components",
]


class NewIdeaForm(forms.Form):
    new_idea = forms.CharField(label="New Idea")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)


# Create your views here.
def index(request):
    return render(request, "idea_logger/index.html", {
        "ideas": ideas
    })


def add(request):
    return render(request, "idea_logger/add.html")


def add_2(request):
    if request.method == "POST":
        form = NewIdeaForm(request.POST)
        if form.is_valid():
            idea = form.cleaned_data["new_idea"]
            print(idea)
            ideas.append(idea)
            return HttpResponseRedirect(reverse("idea_logger:index"))
        else:
            return render(request, "idea_logger/add_2.html", {
                "form": form
            })

    return render(request, "idea_logger/add_2.html", {
        "form": NewIdeaForm()
    })
