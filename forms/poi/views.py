from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import PointOfInterest

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