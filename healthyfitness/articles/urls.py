from django.conf.urls.static import static
from django.urls import path

from healthyfitness import settings
from . import views

urlpatterns = [
    path('articles', views.allArticles, name='articles'),
    path('articles/health', views.healthArticles, name='articles_health'),
    path('articles/devices', views.devicesArticles, name='articles_devices'),
    path('articles/food', views.foodArticles, name='articles_food'),
    path('articles/sport', views.sportArticles, name='articles_sport'),
    path('articles/<slug:art_slug>', views.showCertainArticle, name='certainArticle'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)