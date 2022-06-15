from django.contrib import admin
from .models import Type_of_training
from .models import Training_trecker


class Type_of_trainingAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_training', 'kkal_in_hour')
    list_display_links = ('id', 'type_training', 'kkal_in_hour')
    search_fields = ('type_training',)


class Training_treckerAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_users', 'id_training', 'day_create', 'duration_training_min', 'burned_kkal')
    list_display_links = ('id', 'id_users', 'id_training')
    search_fields = ('id_users', 'id_training')
    list_filter = ('id_training', 'day_create')


admin.site.register(Type_of_training, Type_of_trainingAdmin)
admin.site.register(Training_trecker, Training_treckerAdmin)

