from django.db import models

# dd-mm-yyyy hh:mm:ss format in date fields
class Vehicle(models.Model):
    name = models.CharField(max_length=10, blank=False)
    alias = models.CharField(max_length=10, blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    company = models.CharField(max_length=100, blank=False)
    vehicle_type = models.CharField(max_length=250, default='(No specified)')
    gps_id = models.CharField(max_length=150, default='(No specified)')

    class Meta:
        ordering = ['name']
