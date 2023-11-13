from django.urls import path

from . import views

urlpatterns = [
    path("", views.say_hello, name="index"),
    path("render", views.render_hello, name="render"),
    path("greet/<str:name>", views.greet, name="greet"),
]
