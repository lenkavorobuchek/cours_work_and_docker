from django.contrib import admin
from .models import Weight_trecker


class Weight_treckerAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_users', 'day_create', 'weight')
    list_display_links = ('id', 'id_users', 'day_create')
    search_fields = ('id_users', 'day_create')


admin.site.register(Weight_trecker, Weight_treckerAdmin)
