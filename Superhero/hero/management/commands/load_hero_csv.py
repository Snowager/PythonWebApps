from csv import reader
from hero.models import Hero
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        load_hero_csv()

def load_hero_csv():
    Hero.objects.all().delete()

    with open('hero_csv') as f:
        file_read = reader(f)
        for row in file_read:
            Hero.objects.get_or_create(
                name=row[0],
                alias=row[1],
                strength=row[2],
                weakness=row[3],
                image=row[4],
                description=row[5],
            )

