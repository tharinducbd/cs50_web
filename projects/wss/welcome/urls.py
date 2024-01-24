from django.urls import path

from . import views


urlpatterns = [
    path("hello", views.hello, name='hello'),
    path("hello/<str:name>", views.greet, name='greet'),
    path("", views.index, name='index'),
    path("scope/<str:name>", views.greet_2, name='greet_2'),
]
