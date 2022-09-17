from pathlib import Path
from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HeroDetailView(TemplateView):
    template_name: str = 'hero.html'

    def get_context_data(self, **kwargs):
        name = kwargs['name']
        image = f"/static/images/{name}"
        hero = hero_list(name)
        return {
            'photo': image,
            'title': hero['title'],
            'body' : hero['body'],
        }

class HeroListView(TemplateView):
    template_name = 'index.html'


    def get_context_data(self, **kwargs):
        heroes = Path('static/images').iterdir()
        heroes = [f for f in heroes]
        return dict(heroes=heroes)

def hero_list(name):
    if name == "bigByWolf.jpg":
        return {
            'title' : "Bigby Wolf",
            'body' : "My name is Bigby Wolf, and I work to secure and protect Fables.",
            # 'image' : '/static/images/bigbyWolf.jpg'
        }
    elif name == "jackFrost.jpg":
        return {
            "title" : "Jack Frost",
            "body" : "My name is Jack Frost, and I might just be Buddha incarnate.",
            # "image" : '/static/images/jackFrost.jpg',
        }
    elif name == "spawn.jpg":
        return {
        "title" : "Spawn",
        "body" : "My name is Spawn, and I fight in Hell",
        # "image" : '/static/images/spawn.jpg',
        }