from django.urls import path

from . import views

urlpatterns = [
    path("", views.say_hello, name="index"),
    path("greet/<str:name>", views.greet, name="greet"),
    path("render", views.render_hello, name="render_hello"),
    path("greet2/<str:name>", views.render_greet, name="render_greet")
]
