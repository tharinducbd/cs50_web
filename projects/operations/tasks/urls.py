from django.urls import path

from . import views


app_name = 'tasks'

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_task, name="add_task"),
    path("add2/", views.add_task_2, name="add_task_2"),
    path("add_component/", views.add_component, name="add_component"),
    path("task/<int:task_id>/", views.view_task, name="view_task"),
    path("task/<int:task_id>/append_comp", views.append_task_comp, name="append_comp_to_task")
]
