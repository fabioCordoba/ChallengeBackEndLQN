from django.contrib import admin
from apps.planet.models.planet import Planet

@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    list_display = ('name', 'climate', 'terrain', 'population', 'is_active' )
