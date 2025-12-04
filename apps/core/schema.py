import graphene
from apps.character.schema import CharacterQuery, CreateCharacter
from apps.film.schema import CreateFilm, FilmQuery
from apps.planet.schema import CreatePlanet, PlanetQuery

class Query(
    PlanetQuery,
    FilmQuery,
    CharacterQuery, 
    graphene.ObjectType
):
    pass

class Mutation(graphene.ObjectType):
    create_planet = CreatePlanet.Field()
    create_film = CreateFilm.Field()
    create_character = CreateCharacter.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
