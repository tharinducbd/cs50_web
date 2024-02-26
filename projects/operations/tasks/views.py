from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import Component, Component_Type, Task
from .models import INTERVALS, RESPONSIBILITY


def index(request):
    list_components = Component.objects.all().order_by('component_type', 'component')
    return render(request, 'tasks/index.html', {
        "comps": list_components,
    })


def add_task(request):
    list_components = Component.objects.all().order_by('component_type', 'component')
    return render(request, 'tasks/add_task.html', {
        "components": list_components,
        "intervals": dict(INTERVALS),
        "responsibilities": dict(RESPONSIBILITY),
    })


class AddTaskForm(forms.Form):
    list_components = Component.objects.all().order_by('component_type', 'component')

    component = forms.ModelChoiceField(queryset=list_components,
                                       label="Component")
    task_name = forms.CharField(label="Task",max_length=200, initial="Enter task")
    task_interval = forms.ChoiceField(choices=INTERVALS, label="Task interval")
    task_responsibility = forms.ChoiceField(choices=RESPONSIBILITY, label="Responsibility")
    # refer documentation on form fields!


def add_task_2(request):
    return render(request, 'tasks/add_task_2.html',{
        "form": AddTaskForm()
    })
