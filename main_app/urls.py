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
    # associate a shop with a comic (M:M)
    path('comics/<int:comic_id>/assoc_shop/<int:shop_id>/', views.assoc_shop, name='assoc_shop'),
    # unassociate a shop and comic
    path('comics/<int:comic_id>/unassoc_shop/<int:shop_id>/', views.unassoc_shop, name='unassoc_shop'),
    # Submiting a phot
    path('comics/<int:comic_id>/add_photo/', views.add_photo, name='add_photo'),
    path('shops/', views.ShopList.as_view(), name='shops_index'),
    path('shops/<int:pk>/', views.ShopDetail.as_view(), name='shops_detail'),
    path('shops/create/', views.ShopCreate.as_view(), name='shops_create'),
    path('shops/<int:pk>/update/', views.ShopUpdate.as_view(), name='shops_update'),
    path('shops/<int:pk>/delete/', views.ShopDelete.as_view(), name='shops_delete'),
]