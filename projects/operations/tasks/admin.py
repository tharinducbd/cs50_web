from django.contrib import admin

from .models import Component_Type, Component, Task


class TaskAdmin(admin.ModelAdmin):
    ordering = ("task_name", "task_responsibility",)
    list_display = ("task_name", "task_responsibility", "task_interval")
    filter_horizontal = ("components",)


class Component_TypeAdmin(admin.ModelAdmin):
    ordering = ("component_type",)
    list_display = ("component_type","id",)


class ComponentAdmin(admin.ModelAdmin):
    ordering = ("component_type", "component",)
    list_display = ("component", "component_type",)


# Register your models here.
admin.site.register(Component_Type, Component_TypeAdmin)
admin.site.register(Component, ComponentAdmin)
admin.site.register(Task, TaskAdmin)
