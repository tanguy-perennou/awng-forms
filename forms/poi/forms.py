from django import forms

class PointOfInterestForm(forms.Form):
    name = forms.CharField(label='POI name', max_length=100)
    lat = forms.FloatField(label='Latitude in degrees', min_value=-90, max_value=90)
    lon = forms.FloatField(label='Longitude in degrees', min_value=-180, max_value=180)
    alt = forms.FloatField(label='Altitude in meters', min_value=-200, max_value=8848)
