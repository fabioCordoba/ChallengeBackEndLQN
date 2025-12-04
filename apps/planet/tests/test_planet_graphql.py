from django.test import TestCase
from apps.planet.models.planet import Planet
from apps.planet.schema import PlanetQuery, CreatePlanet
import graphene
from graphene.relay import Node


class PlanetGraphQLTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        class Mutation(graphene.ObjectType):
            create_planet = CreatePlanet.Field()

        cls.schema = graphene.Schema(
            query=PlanetQuery,
            mutation=Mutation
        )
        
    # QUERIES
    def test_query_all_planets(self):
        Planet.objects.create(name="Tatooine")
        Planet.objects.create(name="Naboo")

        query = """
        query {
            allPlanets {
                name
            }
        }
        """

        executed = self.schema.execute(query)
        nombres = [p["name"] for p in executed.data["allPlanets"]]

        self.assertEqual(nombres, ["Naboo", "Tatooine"])

    def test_query_planet_by_id(self):
        planeta = Planet.objects.create(name="Endor")
        expected_id = Node.to_global_id("PlanetNode", str(planeta.id))

        query = f"""
        query {{
            planetById(id: "{planeta.id}") {{
                id
                name
            }}
        }}
        """

        executed = self.schema.execute(query)
        data = executed.data["planetById"]

        self.assertEqual(data["name"], "Endor")
        self.assertEqual(data["id"], expected_id)

    def test_query_planet_by_id_not_found(self):
        query = """
        query {
            planetById(id: "00000000-0000-0000-0000-000000000000") {
                id
                name
            }
        }
        """

        executed = self.schema.execute(query)
        self.assertIsNone(executed.data["planetById"])

    # MUTATIONS
    def test_mutation_create_planet(self):
        mutation = """
        mutation {
            createPlanet(
                name: "Hoth",
                climate: "Frigid",
                terrain: "Tundra",
                population: "Unknown"
            ) {
                planet {
                    name
                    climate
                    terrain
                    population
                }
            }
        }
        """

        executed = self.schema.execute(mutation)
        planet_data = executed.data["createPlanet"]["planet"]

        self.assertEqual(planet_data["name"], "Hoth")
        self.assertEqual(planet_data["climate"], "Frigid")
        self.assertEqual(planet_data["terrain"], "Tundra")
        self.assertEqual(planet_data["population"], "Unknown")

        self.assertTrue(Planet.objects.filter(name="Hoth").exists())

