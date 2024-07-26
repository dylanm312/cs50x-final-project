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
    
class VehicleDetailView(generic.DetailView):
    template_name = "ui/edit_vehicle.html"
    context_object_name = "vehicle"
    
    def get_object(self) -> Vehicle:
        return get_object_or_404(Vehicle, pk=self.kwargs["pk"])
        # return VehicleEvent.objects.filter(vehicle_id=vehicle.id).order_by("timestamp")
        