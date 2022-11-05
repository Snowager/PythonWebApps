from json import loads
from pathlib import Path
from hero.models import Hero, Article
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        load_json()

def load_json():
    Hero.objects.all().delete()
    Article.objects.all().delete()

    path = Path("hero_objects.json")
    if path.exists():
        hero_objects = loads(path.read_text())

    path = Path("article_objects.json")
    if path.exists():
        article_objects = loads(path.read_text())

    for o in hero_objects:
        Hero.objects.get_or_create(**o)
    
    for o in article_objects:
        Article.objects.get_or_create(**o)

    for hero in Hero.objects.all().values():
        print(hero)
    
    for article in Hero.objects.all().values():
        print(hero)