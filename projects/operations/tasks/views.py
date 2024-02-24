from django.shortcuts import render

from .models import Component, Task


def index(request):
    list_components = Component.objects.all()
    list_tasks = Task.objects.all()

    return render(request, 'tasks/index.html', {
        "comps": list_components,
        "tasks": list_tasks
    })
