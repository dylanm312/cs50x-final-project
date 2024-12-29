from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("vehicle/create", views.VehicleCreateView.as_view(), name="create_vehicle"),
    path("vehicle/<pk>/edit", views.VehicleUpdateView.as_view(), name="edit_vehicle"),
    path("vehicle/<pk>", views.VehicleDetailView.as_view(), name="view_vehicle"),
    path("vehicle/<pk>/delete", views.VehicleDeleteView.as_view(), name="delete_vehicle"),
    path("vehicle/<pk>/event/new", views.VehicleEventCreateView.as_view(), name="create_vehicle_event"),
    path("vehicle/<pk>/event/<event_pk>/edit", views.VehicleEventUpdateView.as_view(), name="edit_vehicle_event"),
    path("vehicle/<pk>/event/<event_pk>/delete", views.VehicleEventDeleteView.as_view(), name="delete_vehicle_event"),
]