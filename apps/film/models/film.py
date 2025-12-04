from django.db import models
from apps.core.models.base_model import BaseModel
from apps.planet.models.planet import Planet

class Film(BaseModel):
    title = models.CharField(max_length=300)
    episode_id = models.IntegerField(null=True, blank=True)
    opening_crawl = models.TextField(blank=True)
    director = models.CharField(max_length=200, blank=True)
    producers = models.CharField(max_length=300, blank=True)
    release_date = models.DateField(null=True, blank=True)
    planets = models.ManyToManyField(Planet, related_name='films', blank=True)

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return f"Film: {self.title} (Episode {self.episode_id})"
