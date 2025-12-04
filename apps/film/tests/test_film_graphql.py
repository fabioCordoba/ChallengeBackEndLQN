import graphene
from django.test import TestCase
from graphene.relay import Node

from apps.film.models.film import Film
from apps.planet.models.planet import Planet

from apps.film.schema import FilmQuery, CreateFilm


class FilmGraphQLTest(TestCase):

    def setUp(self):
        class Query(FilmQuery, graphene.ObjectType):
            pass

        class Mutation(graphene.ObjectType):
            create_film = CreateFilm.Field()

        self.schema = graphene.Schema(query=Query, mutation=Mutation)

    # QUERY: all_films
    def test_query_all_films(self):
        Film.objects.create(title="A New Hope")
        Film.objects.create(title="Empire Strikes Back")

        query = """
        query {
            allFilms {
                title
            }
        }
        """

        executed = self.schema.execute(query)
        data = executed.data["allFilms"]

        titles = [film["title"] for film in data]

        self.assertIn("A New Hope", titles)
        self.assertIn("Empire Strikes Back", titles)

    # QUERY: film_by_id
    def test_query_film_by_id(self):
        film = Film.objects.create(title="Return of the Jedi")

        expected_id = Node.to_global_id("FilmNode", str(film.id))

        query = f"""
        query {{
            filmById(id: "{film.id}") {{
                id
                title
            }}
        }}
        """

        executed = self.schema.execute(query)
        data = executed.data["filmById"]

        self.assertEqual(data["title"], "Return of the Jedi")
        self.assertEqual(data["id"], expected_id)

    def test_query_film_by_id_not_found(self):
        query = """
        query {
            filmById(id: "12345678-1234-1234-1234-1234567890ab") {
                id
                title
            }
        }
        """

        executed = self.schema.execute(query)
        self.assertIsNone(executed.data["filmById"])

    # MUTATION: create_film
    def test_mutation_create_film(self):
        planet1 = Planet.objects.create(name="Tatooine")
        planet2 = Planet.objects.create(name="Alderaan")

        mutation = f"""
        mutation {{
            createFilm(
                title: "A New Hope",
                openingCrawl: "It is a period of civil war...",
                director: "George Lucas",
                producers: "Gary Kurtz",
                planetIds: ["{planet1.id}", "{planet2.id}"]
            ) {{
                film {{
                    title
                    director
                    planets {{
                        edges {{
                            node {{
                                name
                            }}
                        }}
                    }}
                }}
            }}
        }}
        """

        executed = self.schema.execute(mutation)

        if executed.errors:
            raise AssertionError(f"GraphQL errors: {executed.errors}")

        film_data = executed.data["createFilm"]["film"]

        self.assertEqual(film_data["title"], "A New Hope")
        self.assertEqual(film_data["director"], "George Lucas")

        planet_names = [edge["node"]["name"] for edge in film_data["planets"]["edges"]]

        self.assertIn("Tatooine", planet_names)
        self.assertIn("Alderaan", planet_names)


