from django.db import models

# Create your models here.
class PointOfInterest(models.Model):
    """
    Point of Interest
    """
    name = models.CharField(max_length=200)
    lat = models.FloatField('Latitude (degrees)')
    lon = models.FloatField('Longitude (degrees)')
    alt = models.FloatField('Altitude (meters)')
    
