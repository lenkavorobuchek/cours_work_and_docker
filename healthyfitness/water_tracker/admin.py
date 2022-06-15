from django.contrib import admin
from .models import Water_tracker

class Water_trackerAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_users', 'day_create', 'number_of_glasses')
    list_display_links = ('id', 'id_users', 'day_create')
    search_fields = ('id_users', 'day_create')


admin.site.register(Water_tracker, Water_trackerAdmin)
