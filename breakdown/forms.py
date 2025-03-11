from django import forms
from .models import VehicleBreakdown

class VehicleBreakdownForm(forms.ModelForm):
    class Meta:
        model = VehicleBreakdown
        fields = ['vehicle_make', 'vehicle_model', 'license_plate', 
                 'breakdown_location', 'description', 'status']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'breakdown_location': forms.Textarea(attrs={'rows': 2}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to form fields
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
