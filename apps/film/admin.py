from django.contrib import admin
from apps.film.models.film import Film

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'episode_id', 'director', 'producers', 'release_date', 'is_active' )