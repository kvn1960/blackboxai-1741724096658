from django.contrib import admin
from .models import VehicleBreakdown

@admin.register(VehicleBreakdown)
class VehicleBreakdownAdmin(admin.ModelAdmin):
    list_display = ('vehicle_make', 'vehicle_model', 'license_plate', 
                   'status', 'reported_time')
    list_filter = ('status', 'reported_time', 'vehicle_make')
    search_fields = ('vehicle_make', 'vehicle_model', 'license_plate', 
                    'breakdown_location', 'description')
    date_hierarchy = 'reported_time'
