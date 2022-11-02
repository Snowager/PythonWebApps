from ast import alias
from pydoc import describe
from unicodedata import name

from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from kiwisolver import strength

from .models import Hero, Article

def user():
    return dict(username='fake', password='alsoFake')

def test_user():
    return get_user_model().objects.create_user(**user)

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

        def create_test_hero():
            return dict(name = "Wolf",
            alias = "Bigby",
            strength = "Strong",
            weakness = "Drinking",
            description = "n/a",
            )

        def create_test_hero2():
            return dict(name = "John",
            alias = "Johnson",
            strength = "mind",
            weakness = "human",
            description = "n/a",
            )

        def login(self):
            username = user()['username']
            password = user()['password']
            response = self.client.login(username=username, password=password)
            self.assertEqual(response, True)

        def test_hero_list_view(self):
            self.assertEqual(reverse("Hero_list"), "Hero/")

        def test_hero_add_view(self):
            self.login()
            a = Hero.objects.create(**self.create_test_hero)
            response = self.client.post(reverse("Hero_add"), a)
            self.assertEqual(len(Hero.objects.all()), 1)

        def test_hero_edit_view(self):
            self.login()
            Hero.objects.create(**self.create_test_hero)
            Hero.objects.create(**self.create_test_hero2)
            response = self.client.post(
                reverse('Hero_edit', args='1'), self.create_test_hero)
            self.assertEqual(response.status_code, 302)
            response = self.client.get(response.url)
            hero = Hero.objects.get(pk=1)
            self.assertEqual(hero.name, self.create_test_hero2['name'])

        def test_hero_delete_view(self):
            self.login()
            Hero.objects.create(**self.create_test_hero)
            self.assertEqual(reverse('Hero_delete', args='1'), 'Hero/1/delete')
            response = self.client.post('Hero/1/delete')
            self.assertEqual(response.status_code, 302)
            self.assertEqual(len(Hero.objects.all()), 0)

    class HeroDataTest(TestCase):
        def test_article(self):
            self.assertEqual(len(Article.objects.all()), 0)
            Article.objects.create(
                title = "Test",
                created_by = "tester",
                content = "text here",
            )
            Article.objects.create(
                title = "Test2",
                created_by = "tester2",
                content = "text here as well",
            )
            self.assertEqual(len(Article.objects.all()), 2)

            a = Article.objects.get(pk=1)
            self.assertEqual(a.title, "Test")

            a.content = "Blah"
            a.save()
            self.assertEqual(a.content, "Blah")

            a.delete()
            self.assertEqual(len(Article.objects.all()), 1)

    class ArticleViewsTest(TestCase):

        def create_test_article():
            return dict(title = "Test",
            created_by = "tester",
            content = "text here",
            )

        def create_test_article2():
            return dict(title = "Test2",
            created_by = "tester2",
            content = "text here as well",
            )

        def login(self):
            username = user()['username']
            password = user()['password']
            response = self.client.login(username=username, password=password)
            self.assertEqual(response, True)

        def test_article_list_view(self):
            self.assertEqual(reverse("article_list"), "articles/")

        def test_article_add_view(self):
            self.login()
            a = Article.objects.create(**self.create_test_article)
            response = self.client.post(reverse("article_add"), a)
            self.assertEqual(len(Article.objects.all()), 1)

        def test_article_edit_view(self):
            self.login()
            Article.objects.create(**self.create_test_article)
            Article.objects.create(**self.create_test_article2)
            response = self.client.post(
                reverse('article_edit', args='1'), self.create_test_article)
            self.assertEqual(response.status_code, 302)
            response = self.client.get(response.url)
            article = Article.objects.get(pk=1)
            self.assertEqual(article.title, self.create_test_article2['title'])

        def test_article_delete_view(self):
            self.login()
            Article.objects.create(**self.create_test_article)
            self.assertEqual(reverse('article_delete', args='1'), 'articles/1/delete')
            response = self.client.post('articles/1/delete')
            self.assertEqual(response.status_code, 302)
            self.assertEqual(len(Article.objects.all()), 0)

