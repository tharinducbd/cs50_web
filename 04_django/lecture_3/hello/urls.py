from django.urls import path

from . import views

urlpatterns = [
    path("", views.say_hello, name="index"),
    path("<str:name>", views.greet, name="greet"),
]
