from django.urls import path

from . import views

app_name = 'newyear'    # helps avoid namespace conflicts in urls inside templates

urlpatterns = [
    path("", views.index, name="index")
]
