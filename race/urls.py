from django.urls import path

from . import views

app_name = "race"

urlpatterns = [
    path("", views.setup, name="setup"),
    path("race/", views.run_race, name="run_race"),
]
