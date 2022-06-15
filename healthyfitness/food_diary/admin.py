from django.contrib import admin
from .models import Type_of_food
from .models import Food
from .models import Diary_of_food


class Type_of_foodAdmin(admin.ModelAdmin):
    list_display = ('id', 'type')
    list_display_links = ('id', 'type')
    search_fields = ('type',)


class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_of_product', 'kkal', 'proteins', 'fats', 'carbohydrates', 'type_of_food')
    list_display_links = ('id', 'name_of_product')
    search_fields = ('name_of_product',)
    list_filter = ('type_of_food',)


class Diary_of_foodAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_users', 'id_food', 'day_create', 'grams', 'consumed_kkal', 'consumed_proteins', 'consumed_fats', 'consumed_carbohydrates')
    list_display_links = ('id', 'id_users', 'day_create')
    search_fields = ('id_users', 'day_create')


admin.site.register(Type_of_food, Type_of_foodAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Diary_of_food, Diary_of_foodAdmin)

