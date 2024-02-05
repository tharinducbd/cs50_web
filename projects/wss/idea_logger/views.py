from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


class NewIdeaForm(forms.Form):
    new_idea = forms.CharField(label="New Idea")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)
    main_subject_area = forms.CharField(label="Main Subject Area")
    sub_subject_area = forms.CharField(label="Secondary Subject Area")


# Create your views here.
def index(request):
    if "ideas" not in request.session:
        request.session["ideas"] = []
    return render(request, "idea_logger/index.html", {
        "ideas": request.session["ideas"]
    })


def add(request):
    return render(request, "idea_logger/add.html")


def add_2(request):
    if request.method == "POST":
        form = NewIdeaForm(request.POST)
        if form.is_valid():
            idea = form.cleaned_data["new_idea"]
            print(idea)
            request.session["ideas"] += [idea]
            return HttpResponseRedirect(reverse("idea_logger:index"))
        else:
            return render(request, "idea_logger/add_2.html", {
                "form": form
            })

    return render(request, "idea_logger/add_2.html", {
        "form": NewIdeaForm()
    })
