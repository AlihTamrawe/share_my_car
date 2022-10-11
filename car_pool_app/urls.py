from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index),  
    path('trips/', views.show_detials_trip),
    path('my-trips/', views.my_trip),
]