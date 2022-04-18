from django.urls import reverse_lazy
from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from django.views import generic

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
    :param request: The incoming request. If it is a POST, it contains input data.
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

def update_poi(request, poi_id):
    """
    Update an existing point of interest in the database based on 
    user input collected in a form
    :param request: The incoming request. If it is a GET, it contains
    original date; if it is a POST, it contains updated data.
    """
    # Reference: https://docs.djangoproject.com/en/4.0/ref/forms/api/#django.forms.Form
    # get existing POI to update from database
    poi = get_object_or_404(PointOfInterest, pk=poi_id)
    if request.method == 'GET':
        # routed via HTTP GET (write in navigator bar or click on link):
        # populate new form with data from the database
        data = { 
            'name': poi.name, 
            'lat': poi.lat, 
            'lon': poi.lon,
            'alt': poi.alt
        }
        form = PointOfInterestForm(data)
    elif request.method == 'POST':
        # routed via HTTP POST (click on submit button in create page):
        # create an instance of form using the POST data, just to validate
        form = PointOfInterestForm(request.POST)
        if form.is_valid():
            # update all fields of poi, the object retrieved from the database
            poi.name = form.cleaned_data['name']
            poi.lat = form.cleaned_data['lat']
            poi.lon = form.cleaned_data['lon']
            poi.alt = form.cleaned_data['alt']
            # save updated poi into the database
            poi.save()
            return redirect('poi:list_of_pois')
    return render(request, 'poi/update_poi.html', locals())


# References:
# - https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-display
# - https://docs.djangoproject.com/en/4.0/ref/class-based-views/
# - https://docs.djangoproject.com/en/4.0/ref/class-based-views/generic-display

class ListView(generic.ListView):
    template_name = 'poi/list_of_pois.html'
    context_object_name = 'list_of_pois' # default name passed to template is 'object_list'
    
    def get_queryset(self):
        return PointOfInterest.objects.all()


class DetailsView(generic.DetailView):
    model = PointOfInterest
    template_name = 'poi/poi_details.html'
    context_object_name = 'poi' # default name passed to template is 'object'


# Following view use as much defaults as possible

class CreateView(generic.CreateView):
    model = PointOfInterest
    fields = ['name', 'lat', 'lon', 'alt']
    success_url = reverse_lazy('poi:gen_list')


class UpdateView(generic.UpdateView):
    model = PointOfInterest
    fields = ['name', 'lat', 'lon', 'alt']
    success_url = reverse_lazy('poi:gen_list')
    template_name_suffix = '_update_form'


class DeleteView(generic.DeleteView):
    model = PointOfInterest
    success_url = reverse_lazy('poi:gen_list')
