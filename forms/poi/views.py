from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect

from .models import PointOfInterest
from .forms import PointOfInterestForm

def list_of_pois(request):
    """
    Get all points of interest from database
    :param request: The incoming request
    """
    list_of_pois = get_list_or_404(PointOfInterest)
    return render(request, 'poi/list_of_pois.html', locals())

def poi_details(request, poi_id):
    """
    Get the specified point of interest
    :param request: The incoming request
    :param poi_id: The point of interest ID
    """
    poi = get_object_or_404(PointOfInterest, pk=poi_id)
    return render(request, 'poi/poi_details.html', locals())

def create_poi(request):
    """
    Create a new point of interest in the database based on 
    user input collected in a form
    :param request: The incoming request. It it a POST, it contains input data.
    """
    # Reference: https://docs.djangoproject.com/en/4.0/topics/forms/
    if request.method == 'GET':
        # routed via HTTP GET (write in navigator bar or click on link):
        # create an empty form
        form = PointOfInterestForm()
    elif request.method == 'POST':
        # routed via HTTP POST (click on submit button in create page):
        # create an instance of form using the POST data, just to validate
        form = PointOfInterestForm(request.POST)
        if form.is_valid():
            # Get all data from validated form to make a new POI
            name = form.cleaned_data['name']
            lat = form.cleaned_data['lat']
            lon = form.cleaned_data['lon']
            alt = form.cleaned_data['alt']
            poi = PointOfInterest(name=name, lat=lat, lon=lon, alt=alt)
            # Save the poi into the database
            poi.save()
            # Job done, render another page: the list of all POIs
            return redirect('poi:list_of_pois')
        # if the form is not valid, the page is re-rendered with the data, the
        # template can show the invalid fields
    return render(request, 'poi/create_poi.html', locals())

