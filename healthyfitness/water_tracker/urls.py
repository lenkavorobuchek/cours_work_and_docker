from django.urls import path

from water_tracker import views

urlpatterns = [
    path('personal_area/add_water', views.AddWater, name='add_water'),
    path('personal_area/water_tracker', views.WaterTracker, name='water_tracker'),
]
