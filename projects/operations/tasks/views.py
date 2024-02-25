from django.shortcuts import render

from .models import Component, Task


def index(request):
    list_components = Component.objects.all().order_by('component_type', 'component')

    return render(request, 'tasks/index.html', {
        "comps": list_components,
    })
