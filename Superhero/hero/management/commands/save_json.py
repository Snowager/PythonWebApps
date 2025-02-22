from json import dump
from hero.models import Hero, Article
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        save_json()

def save_json():
    heroData = [h for h in Hero.objects.all().values()]
    articleData = [a for a in Article.objects.all().values()]

    with open("hero_objects.json", "w") as f:
        dump(heroData, f, indent=4, default=str)

    with open("article_objects.json", "w") as f:
        dump(articleData, f, indent=4, default=str)
            