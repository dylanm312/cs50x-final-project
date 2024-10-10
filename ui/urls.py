from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("vehicle/create", views.VehicleCreateView.as_view(), name="create_vehicle"),
    path("vehicle/<pk>", views.VehicleUpdateView.as_view(), name="edit_vehicle"),
    path("vehicle/<pk>/delete", views.VehicleDeleteView.as_view(), name="delete_vehicle"),
]