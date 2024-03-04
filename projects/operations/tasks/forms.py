from django import forms

from .models import Component, Component_Type, Task
from .models import INTERVALS, RESPONSIBILITY


class AddTaskForm(forms.Form):
    list_components = Component.objects.all().order_by('component_type', 'component')

    my_list = []
    for item in list_components:
        temp_tuple = (item.id, item)
        my_list.append(temp_tuple)

    # component = forms.ModelChoiceField(queryset=list_components,
    #                                    label="Component",
    #                                    empty_label="Select component")
    components = forms.MultipleChoiceField(choices=my_list)
    task_name = forms.CharField(label="Task",
                                max_length=200,
                                # initial="Enter task", << 'delete n enter' kind of placeholder.
                                widget=forms.Textarea(attrs={
                                    'placeholder': 'Enter task',
                                    'rows': 3, 'columns': 70,}),)
    task_interval = forms.ChoiceField(choices=INTERVALS, label="Task interval")
    task_responsibility = forms.ChoiceField(choices=RESPONSIBILITY, label="Responsibility")
