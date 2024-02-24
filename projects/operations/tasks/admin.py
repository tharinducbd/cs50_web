from django.contrib import admin

from .models import Component_Type, Component, Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ("task_name", "task_responsibility", "task_interval")
    filter_horizontal = ("component",)

# Register your models here.
admin.site.register(Component_Type)
admin.site.register(Component)
admin.site.register(Task, TaskAdmin)
