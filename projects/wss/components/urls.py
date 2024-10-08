from django.urls import path

from . import views


app_name = "components"

urlpatterns = [
    path("", views.index, name="index"),
    path("tanks/<int:tank_id>/", views.tank, name="tank"),
    path("schemes/<int:scheme_id>/", views.scheme, name="scheme"),
    path("schemes/<int:scheme_id>/add_tank/", views.add_tank, name="add_tank"),
]
