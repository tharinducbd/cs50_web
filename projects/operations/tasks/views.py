from django.shortcuts import render

from .models import Component, Component_Type, Task
from .models import INTERVALS, RESPONSIBILITY


def index(request):
    list_components = Component.objects.all().order_by('component_type', 'component')
    return render(request, 'tasks/index.html', {
        "comps": list_components,
    })


def add_task(request):
    components = Component.objects.all()
    return render(request, 'tasks/add_task.html', {
        "components": components,
        "intervals": dict(INTERVALS),
        "responsibilities": dict(RESPONSIBILITY),
    })
