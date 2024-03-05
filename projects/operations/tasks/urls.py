from django.urls import path

from . import views


app_name = 'tasks'

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_task, name="add_task"),
    path("add2/", views.add_task_2, name="add_task_2"),
    path("task/<int:task_id>/", views.view_task, name="view_task")
]
