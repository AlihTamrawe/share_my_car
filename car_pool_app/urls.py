from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index), 
    path('proce-login',views.proc_login) ,
    path('success',views.success),
    path('registration/',views.registration ),
    path('regist_proc',views.regist_proc),
    path('wall/',views.wall),
    path('make_trip/',views.make_trip),
    path('trip_process',views.trip_process),
]