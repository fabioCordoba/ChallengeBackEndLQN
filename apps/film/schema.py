from apps.planet.models.planet import Planet
import graphene
from graphene_django.types import DjangoObjectType
from graphene import relay
from apps.film.models.film import Film

class FilmNode(DjangoObjectType):
    class Meta:
        model = Film
        interfaces = (relay.Node,)
        fields = "__all__"

class FilmQuery(graphene.ObjectType):
    all_films = graphene.List(FilmNode)
    film_by_id = graphene.Field(FilmNode, id=graphene.UUID(required=True))

    def resolve_all_films(root, info):
        return Film.objects.all()

    def resolve_film_by_id(root, info, id):
        print(id)
        try:
            return Film.objects.get(id=id)
        except Film.DoesNotExist:
            return None

class CreateFilm(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        opening_crawl = graphene.String()
        director = graphene.String()
        producers = graphene.String()
        release_date = graphene.Date()
        planet_ids = graphene.List(graphene.ID)

    film = graphene.Field(FilmNode)

    @classmethod
    def mutate(cls, root, info, title, opening_crawl=None, director=None, producers=None, release_date=None, planet_ids=None):
        film = Film.objects.create(title=title, opening_crawl=opening_crawl or '', director=director or '', producers=producers or '', release_date=release_date)
        if planet_ids:
            for pid in planet_ids:
                try:
                    planet = Planet.objects.get(pk=pid)
                except Planet.DoesNotExist:
                    continue
                film.planets.add(planet)
        return CreateFilm(film=film)