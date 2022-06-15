from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('registration.urls')),
    path('', include('main.urls')),
    path('', include('articles.urls')),
    path('', include('calculator.urls')),
    path('', include('personal_area.urls')),
    path('', include('food_diary.urls')),
    path('', include('water_tracker.urls')),
    path('', include('weight.urls')),
    path('', include('sport.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
