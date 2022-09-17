from pathlib import Path
from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HeroDetailView(TemplateView):
    template_name: str = 'hero.html'

    def get_context_data(self, **kwargs):
        link = kwargs['link']
        print(link)
        image = f"/static/images/{link}.jpg"
        new_value = {'photo' : image}
        hero = hero_list(link)
        hero.update(new_value)
        return hero

class HeroListView(TemplateView):
    template_name = 'index.html'


    def get_context_data(self, **kwargs):
        heroes = Path('static/images').iterdir()
        heroes = [str(f)[14:-4] for f in heroes]
        return dict(heroes=heroes)

def hero_list(name):
    if name == "bigbyWolf":
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