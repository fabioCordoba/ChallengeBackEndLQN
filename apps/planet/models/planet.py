from django.db import models
from apps.core.models.base_model import BaseModel

class Planet(BaseModel):
    name = models.CharField(max_length=200, unique=True)
    climate = models.CharField(max_length=200, blank=True)
    terrain = models.CharField(max_length=200, blank=True)
    population = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Planet: {self.name}"
    
    class Meta:
        verbose_name = "Planet"
        verbose_name_plural = "Planets"
        ordering = ("name",)
    

