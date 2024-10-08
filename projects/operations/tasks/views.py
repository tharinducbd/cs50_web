from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Component, Component_Type, Task
from .models import INTERVALS, RESPONSIBILITY

from .forms import AddComponentForm, AddTaskForm

def index(request):
    list_components = Component.objects.all().order_by('component_type', 'component')
    list_tasks = Task.objects.all().order_by('task_name', 'task_responsibility')
    return render(request, 'tasks/index.html', {
        "comps": list_components,
        "tasks": list_tasks,
    })


def add_component(request):
    if request.method == 'POST':
        c_type = request.POST["component_type"]
        c_name = request.POST["component"]

        new_comp = Component(component_type = Component_Type.objects.get(id=int(c_type)),
                             component = c_name)
        new_comp.save()

        if 'save_comp' in request.POST:
            return HttpResponseRedirect(reverse("tasks:index"))
        if 'save_and_add' in request.POST:
            return HttpResponseRedirect(reverse("tasks:add_component"))

    return render(request, 'tasks/add_component.html', {
        'form': AddComponentForm()
    })


# Method 1: Using HTML forms
def add_task(request):
    if request.method == "POST":
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
            new_task.components.add(comp)
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
def add_task_2(request):
    if request.method == 'POST':
        comp_ids = request.POST.getlist("components")
        task_name = request.POST["task_name"]
        task_interval = request.POST["task_interval"]
        task_responsibility = request.POST["task_responsibility"]

        new_task = Task(task_name=task_name,
                        task_interval=task_interval,
                        task_responsibility=task_responsibility)
        new_task.save()

        for x in comp_ids:
            comp = Component.objects.get(id=int(x))
            new_task.components.add(comp)
        new_task.save()

        if 'save_task' in request.POST:
            return HttpResponseRedirect(reverse("tasks:index"))
        if 'save_and_add' in request.POST:
            return HttpResponseRedirect(reverse("tasks:add_task"))

    return render(request, 'tasks/add_task_2.html',{
        "form": AddTaskForm()
    })


def view_task(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'tasks/task.html', {
        'task': task,
        'comps': task.components.all().order_by('component_type', 'component'),
        'non_comps': Component.objects.exclude(tasks=task).all().order_by('component_type', 'component')
    })


def append_task_comp(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(id=task_id)
        
        comp_id = int(request.POST['selected_comp'])
        comp = Component.objects.get(id=comp_id)
        comp.tasks.add(task)
        
        return HttpResponseRedirect(reverse("tasks:view_task", args=(task_id,)))
