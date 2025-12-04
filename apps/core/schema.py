
import graphene
from apps.character.schema import CharacterQuery
from apps.planet.schema import PlanetQuery
from apps.film.schema import FilmQuery

class Query(
    CharacterQuery,
    PlanetQuery,
    FilmQuery,
    graphene.ObjectType
):
    pass

schema = graphene.Schema(query=Query)