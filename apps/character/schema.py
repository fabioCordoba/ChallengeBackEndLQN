from apps.character.models.character import Character
from apps.film.models.film import Film
from apps.planet.models.planet import Planet
import graphene
from graphene_django.types import DjangoObjectType
from graphene import relay
from django_filters import FilterSet, CharFilter
from graphene_django.filter import DjangoFilterConnectionField

class CharacterFilter(FilterSet):
    name = CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Character
        fields = ["name"]

class CharacterNode(DjangoObjectType):
    class Meta:
        model = Character
        interfaces = (relay.Node,)
        # fields = "__all__"
        filterset_class = CharacterFilter


class CharacterQuery(graphene.ObjectType):
    all_characters = graphene.List(CharacterNode)
    character_by_id = graphene.Field(CharacterNode, id=graphene.UUID(required=True))
    characters = DjangoFilterConnectionField(CharacterNode)

    def resolve_all_characters(root, info):
        return Character.objects.all()
    
    def resolve_character_by_id(root, info, id):
        try:
            return Character.objects.get(id=id)
        except Character.DoesNotExist:
            return None

class CreateCharacter(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        birth_year = graphene.String()
        gender = graphene.String()
        height = graphene.String()
        mass = graphene.String()
        film_ids = graphene.List(graphene.ID)
        homeworld_id = graphene.ID()

    character = graphene.Field(CharacterNode)

    @classmethod
    def mutate(cls, root, info, name, birth_year=None, gender=None, height=None, mass=None, film_ids=None, homeworld_id=None):
        homeworld = None
        if homeworld_id:
            try:
                homeworld = Planet.objects.get(pk=homeworld_id)
            except Planet.DoesNotExist:
                pass
        character = Character.objects.create(name=name, birth_year=birth_year or '', gender=gender or '', height=height or '', mass=mass or '', homeworld=homeworld)
        if film_ids:
            for fid in film_ids:
                try:
                    film = Film.objects.get(pk=fid)
                except Film.DoesNotExist:
                    continue
                character.films.add(film)
        return CreateCharacter(character=character)