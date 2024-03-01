from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Component, Component_Type, Task
from .models import INTERVALS, RESPONSIBILITY


def index(request):
    list_components = Component.objects.all().order_by('component_type', 'component')
    list_tasks = Task.objects.all().order_by('task_name', 'task_responsibility')
    return render(request, 'tasks/index.html', {
        "comps": list_components,
        "tasks": list_tasks,
    })


# Method 1: Using HTML forms
def add_task(request):
    if request.method == "POST":
        if 'clear_fields' in request.POST:
            return HttpResponseRedirect(reverse("tasks:add_task"))

        comp_ids = request.POST.getlist("comp_ids")
        task_name = request.POST["task_name"]
        task_interval = request.POST["task_interval"]
        task_responsibility = request.POST["task_responsibility"]

        new_task = Task(task_name=task_name,
                        task_interval=task_interval,
                        task_responsibility=task_responsibility)
        new_task.save()

        for x in comp_ids:
            comp = Component.objects.get(id=int(x))
            new_task.component.add(comp)
        new_task.save()

        if 'save_task' in request.POST:
            return HttpResponseRedirect(reverse("tasks:index"))
        if 'save_and_add' in request.POST:
            return HttpResponseRedirect(reverse("tasks:add_task"))

    list_components = Component.objects.all().order_by('component_type', 'component')
    return render(request, 'tasks/add_task.html', {
        "components": list_components,
        "intervals": dict(INTERVALS),
        "responsibilities": dict(RESPONSIBILITY),
    })


# Method 2: Using forms.Form
class AddTaskForm(forms.Form):
    list_components = Component.objects.all().order_by('component_type', 'component')

    component = forms.ModelChoiceField(queryset=list_components,
                                       label="Component",
                                       empty_label="Select component")
    task_name = forms.CharField(label="Task",max_length=200, initial="Enter task")
    task_interval = forms.ChoiceField(choices=INTERVALS, label="Task interval")
    task_responsibility = forms.ChoiceField(choices=RESPONSIBILITY, label="Responsibility")


def add_task_2(request):
    return render(request, 'tasks/add_task_2.html',{
        "form": AddTaskForm()
    })


# Method 3: Model forms?