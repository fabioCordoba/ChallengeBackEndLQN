import graphene
from graphene_django.types import DjangoObjectType
from graphene import relay
from apps.planet.models.planet import Planet

class PlanetNode(DjangoObjectType):
    class Meta:
        model = Planet
        interfaces = (relay.Node,)
        fields = "__all__"

class PlanetQuery(graphene.ObjectType):
    all_planets = graphene.List(PlanetNode)
    planet_by_id = graphene.Field(PlanetNode, id=graphene.UUID(required=True))

    def resolve_all_planets(root, info):
        return Planet.objects.all()

    def resolve_planet_by_id(root, info, id):
        try:
            return Planet.objects.get(id=id)
        except Planet.DoesNotExist:
            return None
        
class CreatePlanet(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        climate = graphene.String()
        terrain = graphene.String()
        population = graphene.String()

    planet = graphene.Field(PlanetNode)

    @classmethod
    def mutate(cls, root, info, name, climate=None, terrain=None, population=None):
        planet = Planet.objects.create(name=name, climate=climate or '', terrain=terrain or '', population=population or '')
        return CreatePlanet(planet=planet)