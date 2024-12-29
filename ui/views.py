from django.db.models.query import QuerySet
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin

from .models import MaintenanceItem, Vehicle, VehicleEvent

# Create your views here.
class IndexView(generic.ListView):
    template_name = "ui/index.html"
    context_object_name = "vehicle_list"
    
    def get_queryset(self) -> QuerySet[Vehicle]:
        return Vehicle.objects.all()
    
class VehicleCreateView(SuccessMessageMixin, generic.edit.CreateView):
    model = Vehicle
    fields = ["name", "year", "make", "model", "color", "license_plate", "license_plate_state", "vin", "mileage"]
    template_name_suffix = "_form"
    success_url = reverse_lazy("index")
    success_message = "Added vehicle '%(name)s'"
    
class VehicleUpdateView(SuccessMessageMixin, generic.edit.UpdateView):
    model = Vehicle
    fields = ["name", "year", "make", "model", "color", "license_plate", "license_plate_state", "vin", "mileage"]
    template_name_suffix = "_form"
    success_url = reverse_lazy("index")
    success_message = "Updated vehicle '%(name)s'"
    
class VehicleDetailView(generic.DetailView):
    model = Vehicle
    template_name_suffix = "_detail"
    success_url = "/"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["events"] = VehicleEvent.objects.filter(vehicle=context["vehicle"]).order_by("-timestamp")
        return context
    
class VehicleDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = Vehicle
    success_url = reverse_lazy("index")
    success_message = "Deleted vehicle '%(name)s'"
    
class VehicleEventCreateView(SuccessMessageMixin, generic.edit.CreateView):
    model = VehicleEvent
    fields = ["name", "description", "timestamp", "mileage", "maintenance_item"]
    template_name_suffix = "_form"
    success_url = reverse_lazy("index")
    success_message = "Added maintenance event for %(vehicle)s at %(timestamp)s with %(maintenance_item)s."
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        maintenance_options = MaintenanceItem.objects.all()
        context.update({"maintenance_options": maintenance_options})
        return context
    # def get(self, request, *args, **kwargs):
    #     maintenance_options = MaintenanceItem.objects.all()
    #     context = {
    #         "vehicle": Vehicle.objects.get(pk=kwargs["pk"]),
    #         "maintenance_options": maintenance_options
    #     }
    #     return render(request, "ui/maintenance_event_form.html", context)
    
    # def post(self, request, *args, **kwargs):
    #     name = request.POST["name"]
    #     description = request.POST["description"]
    #     vehicle = Vehicle.objects.get(pk=kwargs["pk"])
    #     maintenance_item = MaintenanceItem.objects.get(pk=request.POST["maintenance_item"])
    #     timestamp = request.POST["timestamp"]
    #     mileage = round(int(request.POST["mileage"]), 1)
    #     event = VehicleEvent(
    #         name=name,
    #         description=description,
    #         vehicle=vehicle,
    #         maintenance_item=maintenance_item,
    #         timestamp=timestamp,
    #         mileage=mileage)
    #     event.save()
        
    #     messages.success(request, f"Added maintenance event for {vehicle} at {timestamp} with {maintenance_item}.")
        
    #     return redirect("index")
    
class VehicleEventUpdateView(SuccessMessageMixin, generic.edit.UpdateView):
    model = VehicleEvent
    fields = ["name", "description", "timestamp", "mileage", "maintenance_item"]
    template_name_suffix = "_form"
    success_url = reverse_lazy("index")
    success_message = "Updated maintenance event '%(name)s'"
    
    def get_object(self):
        return VehicleEvent.objects.get(pk=self.kwargs["event_pk"])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        maintenance_options = MaintenanceItem.objects.all()
        context.update({"maintenance_options": maintenance_options})
        
        # Mark selected maintenance option if any
        context.update({"selected_maintenance_item": self.object.maintenance_item})
        return context
    
class VehicleEventDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = VehicleEvent
    success_url = reverse_lazy("index")
    success_message = "Deleted maintenance event '%(name)s'"