from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # route to view all comics
    path('comics/', views.comics_index, name='index'),  
    # route to view single comic's details
    path('comics/<int:comic_id>/', views.comics_detail, name='detail'),  
    # route to create a comic
    path('comics/create/', views.ComicCreate.as_view(), name='comics_create'),
    # route to update comic
    path('comics/<int:pk>/update/', views.ComicUpdate.as_view(), name='comics_update'),
    # route to delete comic
    path('comics/<int:pk>/delete/', views.ComicDelete.as_view(), name='comics_delete'),
    #add a purchase
    path('comics/<int:comic_id>/add_purchase/', views.add_purchase, name='add_purchase'),
]