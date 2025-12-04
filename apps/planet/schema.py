from apps.planet.models.planet import Planet
import graphene
from graphene_django.types import DjangoObjectType


class PlanetType(DjangoObjectType):
    class Meta:
        model = Planet
        fields = "__all__"

class PlanetQuery(graphene.ObjectType):
    all_planets = graphene.List(PlanetType)
    planet_by_id = graphene.Field(PlanetType, id=graphene.UUID(required=True))

    def resolve_all_planets(root, info):
        return Planet.objects.all()

    def resolve_planet_by_id(root, info, id):
        try:
            return Planet.objects.get(id=id)
        except Planet.DoesNotExist:
            return None
