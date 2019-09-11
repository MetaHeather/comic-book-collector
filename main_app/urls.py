from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # route to view all comics
    path('comics/', views.comics_index, name='index'),    
]