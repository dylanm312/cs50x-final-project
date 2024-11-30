from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Vehicle(models.Model):
    """Represents a motor vehicle"""
    
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=10)
    license_plate_state = models.CharField(max_length=2)
    vin = models.CharField(max_length=17)
    mileage = models.DecimalField(default=0, max_digits=9, decimal_places=1) # type: ignore
    # TODO: add photo field
    
    def __str__(self) -> str:
        return f"{self.name} ({self.license_plate})"
    
    def get_absolute_url(self):
        return reverse('edit_vehicle', kwargs={'pk': self.pk})

class MaintenanceItem(models.Model):
    """
    Represents a possible maintenance item that could be performed on a Vehicle (e.g. oil change, brake job, etc).
    Does not represent an actual instance of a maintenance action (that would be a VehicleEvent)."""
    
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    # TODO: add photo field
    
    def __str__(self) -> str:
        return f"{self.name}: {self.description}"
    
class VehicleEvent(models.Model):
    """
    Represents something that has occurred to a vehicle. E.g. "on XX date at YY mileage, ZZ MaintenanceItem was performed."
    
    Can also represent non-maintenance items, e.g. modifications performed. The maintenance_item field is nullable to allow this behavior.
    """
    
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    maintenance_item = models.ForeignKey(MaintenanceItem, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self) -> str:
        return f"{self.name} was performed on {self.vehicle} on {self.timestamp.strftime("%Y-%m-%d")} at {self.vehicle.mileage} miles."


