from django.urls import path

from sport import views

urlpatterns = [
    path('personal_area/add_sport', views.AddSport, name='add_sport'),
    path('personal_area/sport_diary', views.SportDiary, name='sport_diary'),
]