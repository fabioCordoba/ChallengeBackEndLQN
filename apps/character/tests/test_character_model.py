from django.test import TestCase
from apps.character.models.character import Character
from apps.film.models.film import Film
from apps.planet.models.planet import Planet


class CharacterModelTest(TestCase):

    def test_creation_character(self):
        character = Character.objects.create(
            name="Luke Skywalker",
            birth_year="19BBY",
            gender="male",
            height="172",
            mass="77",
        )

        self.assertEqual(character.name, "Luke Skywalker")
        self.assertEqual(character.birth_year, "19BBY")
        self.assertEqual(character.gender, "male")
        self.assertEqual(character.height, "172")
        self.assertEqual(character.mass, "77")

    def test_blank_fields(self):
        character = Character.objects.create(name="Unknown")

        self.assertEqual(character.birth_year, "")
        self.assertEqual(character.gender, "")
        self.assertEqual(character.height, "")
        self.assertEqual(character.mass, "")
        self.assertIsNone(character.homeworld)

    def test_str(self):
        character = Character.objects.create(name="Han Solo")
        self.assertEqual(str(character), "Character: Han Solo")

    def test_ordering_by_name(self):
        c1 = Character.objects.create(name="Yoda")
        c2 = Character.objects.create(name="Anakin")
        c3 = Character.objects.create(name="Ben Kenobi")

        characters = list(Character.objects.all())

        self.assertEqual(characters, [c2, c3, c1])

    def test_relation_many_to_many_with_films(self):
        f1 = Film.objects.create(title="A New Hope")
        f2 = Film.objects.create(title="The Empire Strikes Back")
        character = Character.objects.create(name="Luke Skywalker")

        character.films.add(f1, f2)

        self.assertIn(f1, character.films.all())
        self.assertIn(f2, character.films.all())
        self.assertEqual(character.films.count(), 2)

    def test_relatio_homeworld_with_planet(self):
        planet = Planet.objects.create(name="Tatooine")
        character = Character.objects.create(name="Anakin Skywalker", homeworld=planet)

        self.assertEqual(character.homeworld, planet)
        self.assertIn(character, planet.residents.all())
