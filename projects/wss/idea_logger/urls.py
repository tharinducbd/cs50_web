from django.urls import path

from . import views


# app_name help avoid namespace conflicts if 'name' of paths are same in multiple apps!
app_name = "idea_logger"

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add_idea"),
    path("add2", views.add_2, name="add_idea_2"),
]
