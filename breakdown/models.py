from django.db import models

class VehicleBreakdown(models.Model):
    STATUS_CHOICES = [
        ('reported', 'Reported'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]

    vehicle_make = models.CharField(max_length=100)
    vehicle_model = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=20)
    breakdown_location = models.TextField()
    description = models.TextField()
    reported_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='reported'
    )

    def __str__(self):
        return f"{self.vehicle_make} {self.vehicle_model} - {self.license_plate}"

    class Meta:
        ordering = ['-reported_time']
