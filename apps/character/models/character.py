from django.db import models
from apps.core.models.base_model import BaseModel
from apps.film.models.film import Film
from apps.planet.models.planet import Planet

class Character(BaseModel):
    name = models.CharField(max_length=200)
    birth_year = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=50, blank=True)
    height = models.CharField(max_length=50, blank=True)
    mass = models.CharField(max_length=50, blank=True)
    films = models.ManyToManyField(Film, related_name='characters', blank=True)
    homeworld = models.ForeignKey(Planet, null=True, blank=True, on_delete=models.SET_NULL, related_name='residents')

    def __str__(self):
        return f"Character: {self.name}"

