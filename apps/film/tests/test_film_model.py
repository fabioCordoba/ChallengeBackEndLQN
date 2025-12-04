from django.test import TestCase
from django.db import IntegrityError
from datetime import date

from apps.film.models.film import Film
from apps.planet.models.planet import Planet


class FilmModelTest(TestCase):

    def test_Creation_film(self):
        film = Film.objects.create(
            title="A New Hope",
            episode_id=4,
            opening_crawl="It is a period of civil war...",
            director="George Lucas",
            producers="Gary Kurtz, Rick McCallum",
            release_date=date(1977, 5, 25)
        )

        self.assertEqual(film.title, "A New Hope")
        self.assertEqual(film.episode_id, 4)
        self.assertEqual(film.director, "George Lucas")
        self.assertEqual(film.producers, "Gary Kurtz, Rick McCallum")
        self.assertEqual(film.release_date, date(1977, 5, 25))

    def test_blank_fields(self):
        film = Film.objects.create(title="Film sin datos")

        self.assertEqual(film.episode_id, None)
        self.assertEqual(film.opening_crawl, "")
        self.assertEqual(film.director, "")
        self.assertEqual(film.producers, "")
        self.assertEqual(film.release_date, None)

    def test_single_title_not_required(self):
        Film.objects.create(title="Rogue One")
        Film.objects.create(title="Rogue One")

        self.assertEqual(Film.objects.filter(title="Rogue One").count(), 2)

    def test_relation_many_to_many_planets(self):
        film = Film.objects.create(title="The Empire Strikes Back")
        p1 = Planet.objects.create(name="Hoth")
        p2 = Planet.objects.create(name="Dagobah")

        film.planets.add(p1, p2)

        self.assertEqual(film.planets.count(), 2)
        self.assertIn(p1, film.planets.all())
        self.assertIn(p2, film.planets.all())

    def test_str(self):
        film = Film.objects.create(title="Return of the Jedi", episode_id=6)

        self.assertEqual(str(film), "Film: Return of the Jedi (Episode 6)")

    def test_ordering_by_title(self):
        f1 = Film.objects.create(title="C")
        f2 = Film.objects.create(title="A")
        f3 = Film.objects.create(title="B")

        films = Film.objects.all()
        self.assertEqual(list(films), [f2, f3, f1])
