from django.contrib import admin

from .models import Vehicle, MaintenanceItem, VehicleEvent

# Register your models here.
admin.site.register(Vehicle)
admin.site.register(MaintenanceItem)
admin.site.register(VehicleEvent)