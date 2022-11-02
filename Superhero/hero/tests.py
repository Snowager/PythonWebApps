from ast import alias
from pydoc import describe
from unicodedata import name
from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from kiwisolver import strength

from .models import Hero, Article

class HeroAppTest(SimpleTestCase):

    def test_django(self):
        self.assertTrue(True)


class HeroDataTest(TestCase):
    def test_Hero(self):
        self.assertEqual(len(Hero.objects.all()), 0)
        Hero.objects.create(
            name = "Wolf",
            alias = "Bigby",
            strength = "Strong",
            weakness = "Drinking",
            description = "n/a",
        )
        Hero.objects.create(
            name = "John",
            alias = "Johnson",
            strength = "mind",
            weakness = "human",
            description = "n/a",
        )
        self.assertEqual(len(Hero.objects.all()), 2)

        a = Hero.objects.get(pk=1)
        self.assertEqual(a.name, "Wolf")

        a.strength = "Speed"
        a.save()
        self.assertEqual(a.strength, "Speed")

        a.delete()
        self.assertEqual(len(Hero.objects.all()), 1)

    class HeroViewsTest(TestCase):
        def test_hero_list_view(self):
            self.assertEqual(reverse("Hero_list"), "Hero/")

        def test_hero_add_view(self):
            a = Hero.objects.create(
            name = "Wolf",
            alias = "Bigby",
            strength = "Strong",
            weakness = "Drinking",
            description = "n/a",
            )
            b = Hero.objects.create(
                name = "John",
                alias = "Johnson",
                strength = "mind",
                weakness = "human",
                description = "n/a",
            )
            response = self.client.post(reverse("Hero_add"), a)
            response = self.client.post(reverse("Hero_add"), b)
            self.assertEqual(len(Hero.objects.all()), 2)

