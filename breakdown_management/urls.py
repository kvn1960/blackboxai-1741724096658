"""
URL configuration for breakdown_management project.
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='dashboard', permanent=False)),
    path('admin/', admin.site.urls),
    path('breakdown/', include('breakdown.urls')),
]

# Configure admin site
admin.site.site_header = 'Vehicle Breakdown Management'
admin.site.site_title = 'Vehicle Breakdown Management'
admin.site.index_title = 'Administration'
