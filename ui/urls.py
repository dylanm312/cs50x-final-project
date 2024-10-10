from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("vehicle/<pk>", views.VehicleUpdateView.as_view(), name="edit_vehicle")
]