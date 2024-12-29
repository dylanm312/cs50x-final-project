from datetime import datetime
from django.db.models.query import QuerySet
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin

from vehicle_maintenance_tracker import settings

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
    success_message = "Deleted vehicle"
    
    
    
    
class VehicleEventCreateView(SuccessMessageMixin, generic.edit.CreateView):
    model = VehicleEvent
    fields = ["name", "description", "timestamp", "mileage", "maintenance_item"]
    template_name_suffix = "_form"
    success_message = "Added maintenance event %(name)s."
    
    def get_success_url(self):
        return reverse("view_vehicle", kwargs={"pk": self.object.vehicle.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        maintenance_options = MaintenanceItem.objects.all()
        context.update({
            "maintenance_options": maintenance_options,
            "vehicle": Vehicle.objects.get(pk=self.kwargs["pk"]),
            "now": datetime.now(),
        })
        return context
    
    # Add foreign key relationship upon submission
    def form_valid(self, form):
        form.instance.vehicle = Vehicle.objects.get(pk=self.kwargs["pk"])
        form.save()
        return super().form_valid(form)
    
class VehicleEventUpdateView(SuccessMessageMixin, generic.edit.UpdateView):
    model = VehicleEvent
    fields = ["name", "description", "timestamp", "mileage", "maintenance_item"]
    template_name_suffix = "_form"
    success_message = "Updated maintenance event '%(name)s'"
    
    def get_success_url(self):
        return reverse("view_vehicle", kwargs={"pk": self.object.vehicle.pk})
    
    def get_object(self):
        return VehicleEvent.objects.get(pk=self.kwargs["event_pk"])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        maintenance_options = MaintenanceItem.objects.all()
        context.update({
            "maintenance_options": maintenance_options,
            "selected_maintenance_item": self.object.maintenance_item,
            "vehicle": self.object.vehicle,
        })
        return context
    
    # Add foreign key relationship upon submission
    def form_valid(self, form):
        form.instance.vehicle = self.object.vehicle
        form.save()
        return super().form_valid(form) 
    
class VehicleEventDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = VehicleEvent
    success_message = "Deleted maintenance event"
    
    def get_success_url(self):
        return reverse("view_vehicle", kwargs={"pk": self.object.vehicle.pk})
    
    def get_object(self):
        return VehicleEvent.objects.get(pk=self.kwargs["event_pk"])