from django.contrib import admin
from apps.character.models.character import Character

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_year', 'gender', 'height', 'mass', 'is_active' )


