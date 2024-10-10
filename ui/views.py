from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404
from django.views import generic

from .models import Vehicle, VehicleEvent

# Create your views here.
class IndexView(generic.ListView):
    template_name = "ui/index.html"
    context_object_name = "vehicle_list"
    
    def get_queryset(self) -> QuerySet[Vehicle]:
        return Vehicle.objects.all()
    
class VehicleUpdateView(generic.edit.UpdateView):
    model = Vehicle
    fields = ["name", "year", "make", "model", "color", "license_plate", "license_plate_state", "vin", "mileage"]
    template_name_suffix = "_update_form"