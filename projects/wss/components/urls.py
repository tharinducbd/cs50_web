from django.urls import path

from . import views


app_name = "components"

urlpatterns = [
    path("", views.index, name="index"),
]