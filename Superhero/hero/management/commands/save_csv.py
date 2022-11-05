from csv import writer
from hero.models import Hero, Article
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        save_csv()

def save_csv():
    hero_table = [[h.name, h.alias, h.strength, h.weakness, h.image, h.description] for h in Hero.objects.all()]
    with open('hero_csv', 'w', newline='') as f:
        writer(f).writerows(hero_table)

    article_table = [[a.created_by, a.created, a.content] for a in Article.objects.all()]
    with open('article_csv', 'w', newline='') as f:
        writer(f).writerows(article_table)
