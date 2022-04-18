from django.urls import path

from . import views

app_name = 'poi'
urlpatterns = [
    # ex: /poi
    path('', views.list_of_pois, name='list_of_pois'),
    # ex: /poi/5
    path('<int:poi_id>/', views.poi_details, name='poi_details'),
    # ex: /poi/create
    path('create/', views.create_poi, name='create_poi'),
    # ex: /poi/update/1
    path('update/<int:poi_id>/', views.update_poi, name='update_poi'),
    
    # Generic views
    # Reference: https://docs.djangoproject.com/en/4.0/intro/tutorial04/#use-generic-views-less-code-is-better
    path('gen/', views.ListView.as_view(), name='gen_list'),
    path('gen/<int:pk>/', views.DetailsView.as_view(), name='gen_details'),
    path('gen/create/', views.CreateView.as_view(), name='gen_create'),
    path('gen/update/<int:pk>/', views.UpdateView.as_view(), name='gen_update'),
    path('gen/delete/<int:pk>/', views.DeleteView.as_view(), name='gen_delete'),
]
