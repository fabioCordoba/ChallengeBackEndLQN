from apps.film.models.film import Film
import graphene
from graphene_django.types import DjangoObjectType


class FilmType(DjangoObjectType):
    class Meta:
        model = Film
        fields = "__all__"

class FilmQuery(graphene.ObjectType):
    all_films = graphene.List(FilmType)
    film_by_id = graphene.Field(FilmType, id=graphene.UUID(required=True))

    def resolve_all_films(root, info):
        return Film.objects.all()

    def resolve_film_by_id(root, info, id):
        print(id)
        try:
            return Film.objects.get(id=id)
        except Film.DoesNotExist:
            return None
