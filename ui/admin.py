from django.contrib import admin

from .models import Vehicle, MaintenanceItem, VehicleEvent

class VehicleEventInline(admin.TabularInline):
    model = VehicleEvent
    extra = 0
    
class VehicleAdmin(admin.ModelAdmin):
    inlines = [
        VehicleEventInline,
    ]

# Register your models here.
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(MaintenanceItem)
admin.site.register(VehicleEvent)