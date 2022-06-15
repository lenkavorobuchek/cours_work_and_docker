from django.conf.urls.static import static
from django.urls import path
from healthyfitness import settings
from . import views

urlpatterns = [
    path('personal_area/food_diary', views.UserFood, name='food_diary'),
    path('product_selection', views.ProductSelection, name='product_selection'),
    path('product_selection/bakery', views.Bakery, name='bakery'),
    path('product_selection/cereals', views.Cereals, name='cereals'),
    path('product_selection/meat', views.Meat, name='meat'),
    path('product_selection/vegFruit', views.VegFruit, name='vegFruit'),
    path('product_selection/seafood', views.Seafood, name='seafood'),
    path('product_selection/cookedMeals', views.CookedMeals, name='cookedMeals'),
    path('product_selection/milk', views.Milk, name='milk'),
    path('product_selection/sweets', views.Sweets, name='sweets'),
    path('product_selection/drinks', views.Drinks, name='drinks'),
    path('product_selection/nuts_and_oils', views.Nuts_and_oils, name='nuts_and_oils'),
    path('product_selection/herbs_and_spices', views.Herbs_and_spices, name='herbs_and_spices'),
    path('product_selection/fast_food', views.Fast_food, name='fast_food'),
    path('product_selection/search', views.Search, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
