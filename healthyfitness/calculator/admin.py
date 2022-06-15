from django.contrib import admin

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'weight', 'gender', 'growth', 'Activity_level', 'user_aim', 'needed_kkal', 'needed_proteins', 'needed_fats', 'needed_carbohydrates')
    search_fields = ('user',)
    list_display_links = ('user',)


admin.site.register(Profile, ProfileAdmin)
