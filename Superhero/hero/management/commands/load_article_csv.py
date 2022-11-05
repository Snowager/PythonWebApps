from csv import reader
from hero.models import Article
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        load_article_csv()

def load_article_csv():
    with open('article_csv') as f:
        file_read = reader(f)
        for row in file_read:
            Article.objects.get_or_create(
                created_by=row[0],
                created=row[1],
                content=row[2],
            )