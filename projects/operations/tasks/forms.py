from django import forms

from .models import Component, Component_Type, Task
from .models import INTERVALS, RESPONSIBILITY


class AddComponentForm(forms.Form):
    list_ctypes = Component_Type.objects.all().order_by('component_type')
    list_ctypes_formatted = []
    for item in list_ctypes:
        temp_tuple = (item.id, item)
        list_ctypes_formatted.append(temp_tuple)

    component_type = forms.ChoiceField(choices=list_ctypes_formatted)
    component = forms.CharField(label="Component name",
                                max_length=64,
                                widget=forms.TextInput(attrs={
                                    'placeholder': 'Enter component name',
                                    'columns': 64,
                                }))


class AddTaskForm(forms.Form):
    list_components = Component.objects.all().order_by('component_type', 'component')
    list_components_formatted = []
    for item in list_components:
        temp_tuple = (item.id, item)
        list_components_formatted.append(temp_tuple)

    # component = forms.ModelChoiceField(queryset=list_components,
    #                                    label="Component",
    #                                    empty_label="Select component")
    components = forms.MultipleChoiceField(choices=list_components_formatted)
    task_name = forms.CharField(label="Task",
                                max_length=200,
                                # initial="Enter task", << 'delete n enter' kind of placeholder.
                                widget=forms.Textarea(attrs={
                                    'placeholder': 'Enter task',
                                    'rows': 3, 'columns': 70,}),)
    task_interval = forms.ChoiceField(choices=INTERVALS, label="Task interval")
    task_responsibility = forms.ChoiceField(choices=RESPONSIBILITY, label="Responsibility")
