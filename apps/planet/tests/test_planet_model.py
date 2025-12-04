from django.test import TestCase
from apps.planet.models.planet import Planet
from django.db import IntegrityError

class PlanetModelTest(TestCase):

    def planet_creation_test(self):
        planet = Planet.objects.create(
            name="Tatooine",
            climate="Arid",
            terrain="Desert",
            population="200000"
        )

        self.assertEqual(planet.name, "Tatooine")
        self.assertEqual(planet.climate, "Arid")
        self.assertEqual(planet.terrain, "Desert")
        self.assertEqual(planet.population, "200000")

    def test_blank_fields(self):
        planet = Planet.objects.create(name="Unknown")

        self.assertEqual(planet.climate, "")
        self.assertEqual(planet.terrain, "")
        self.assertEqual(planet.population, "")

    def test_unique_name(self):
        Planet.objects.create(name="Hoth")
        with self.assertRaises(IntegrityError):
            Planet.objects.create(name="Hoth")

    def test_str(self):
        planet = Planet.objects.create(name="Naboo")
        self.assertEqual(str(planet), "Planet: Naboo")

    def test_ordering_by_name(self):
        p1 = Planet.objects.create(name="Yavin")
        p2 = Planet.objects.create(name="Alderaan")
        p3 = Planet.objects.create(name="Dagobah")

        planets = Planet.objects.all()

        self.assertEqual(list(planets), [p2, p3, p1])
