from django.db.models.query import QuerySet
from django.views import generic

from .models import Vehicle, VehicleEvent

# Create your views here.
class IndexView(generic.ListView):
    template_name = "ui/index.html"
    context_object_name = "vehicle_list"
    
    def get_queryset(self) -> QuerySet[Vehicle]:
        return Vehicle.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["messages"] = VehicleEvent.objects.filter(vehicle__in=context["vehicle_list"]).order_by("-timestamp")[:5]
        for message in context["messages"]:
            message.type = "primary"
        return context
    
class VehicleCreateView(generic.edit.CreateView):
    model = Vehicle
    fields = ["name", "year", "make", "model", "color", "license_plate", "license_plate_state", "vin", "mileage"]
    template_name_suffix = "_form"
    success_url = "/"
    
class VehicleUpdateView(generic.edit.UpdateView):
    model = Vehicle
    fields = ["name", "year", "make", "model", "color", "license_plate", "license_plate_state", "vin", "mileage"]
    template_name_suffix = "_form"
    success_url = "/"
    
class VehicleDetailView(generic.DetailView):
    model = Vehicle
    template_name_suffix = "_detail"
    success_url = "/"
    
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    
class VehicleDeleteView(generic.DeleteView):
    model = Vehicle
    success_url = "/"