from django.urls import path

from . import views

app_name = 'poi'
urlpatterns = [
    # ex: /poi/
    path('', views.list_of_pois, name='list_of_pois'),
    # ex: /poi/5/
    path('<int:poi_id>/', views.poi_details, name='poi_details')
]