import graphene
from django.test import TestCase
from graphene.relay import Node

from apps.character.models.character import Character
from apps.film.models.film import Film
from apps.planet.models.planet import Planet
from apps.character.schema import CharacterQuery, CreateCharacter


class CharacterGraphQLTest(TestCase):

    def setUp(self):
        class Query(CharacterQuery, graphene.ObjectType):
            pass

        class Mutation(graphene.ObjectType):
            create_character = CreateCharacter.Field()

        self.schema = graphene.Schema(query=Query, mutation=Mutation)

    # QUERY: all_characters
    def test_query_all_characters(self):
        Character.objects.create(name="Luke Skywalker")
        Character.objects.create(name="Leia Organa")

        query = """
        query {
            allCharacters {
                name
            }
        }
        """

        executed = self.schema.execute(query)
        data = executed.data["allCharacters"]

        names = [c["name"] for c in data]
        self.assertIn("Luke Skywalker", names)
        self.assertIn("Leia Organa", names)


    # QUERY: character_by_id
    def test_query_character_by_id(self):
        character = Character.objects.create(name="Darth Vader")

        expected_id = Node.to_global_id("CharacterNode", str(character.id))

        query = f"""
        query {{
            characterById(id: "{character.id}") {{
                id
                name
            }}
        }}
        """

        executed = self.schema.execute(query)
        data = executed.data["characterById"]

        self.assertEqual(data["name"], "Darth Vader")
        self.assertEqual(data["id"], expected_id)

    def test_query_character_by_id_not_found(self):
        query = """
        query {
            characterById(id: "12345678-1234-1234-1234-1234567890ab") {
                id
                name
            }
        }
        """
        executed = self.schema.execute(query)
        self.assertIsNone(executed.data["characterById"])

    # QUERY: characters with filter
    def test_query_characters_filter(self):
        Character.objects.create(name="Luke Skywalker")
        Character.objects.create(name="Leia Organa")

        query = """
        query {
            characters(name: "luke") {
                edges {
                    node {
                        name
                    }
                }
            }
        }
        """
        executed = self.schema.execute(query)

        if executed.errors:
            raise AssertionError(f"GraphQL errors: {executed.errors}")

        names = [edge["node"]["name"] for edge in executed.data["characters"]["edges"]]

        self.assertEqual(names, ["Luke Skywalker"])


    # MUTATION: create_character
    def test_mutation_create_character(self):
        homeworld = Planet.objects.create(name="Tatooine")
        film1 = Film.objects.create(title="A New Hope")
        film2 = Film.objects.create(title="Empire Strikes Back")

        mutation = f"""
        mutation {{
            createCharacter(
                name: "Luke Skywalker",
                birthYear: "19BBY",
                gender: "male",
                height: "172",
                mass: "77",
                homeworldId: "{homeworld.id}",
                filmIds: ["{film1.id}", "{film2.id}"]
            ) {{
                character {{
                    name
                    birthYear
                    homeworld {{
                        name
                    }}
                    films {{
                        edges {{
                            node {{
                                title
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

        character_data = executed.data["createCharacter"]["character"]

        self.assertEqual(character_data["name"], "Luke Skywalker")
        self.assertEqual(character_data["birthYear"], "19BBY")
        self.assertEqual(character_data["homeworld"]["name"], "Tatooine")

        film_titles = [edge["node"]["title"] for edge in character_data["films"]["edges"]]
        self.assertIn("A New Hope", film_titles)
        self.assertIn("Empire Strikes Back", film_titles)
