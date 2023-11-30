from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('restaurants/', views.list_restaurants, name='list_restaurants'),
    path('restaurants/<str:camis>/', views.restaurant_details, name='restaurant_details'),
    path('farmersmarkets/', views.farmers_market_list, name='list_farmers_market'),
    path('farmersmarkets/<str:fm>/', views.fm_details, name='fm_details'),
]