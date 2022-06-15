from django.urls import path

from weight import views

urlpatterns = [
    path('personal_area/add_weight', views.AddWeight, name='add_weight'),
    path('personal_area/weight_tracker', views.WeightTracker, name='weight_tracker'),
]
