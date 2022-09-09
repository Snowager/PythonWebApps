from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'heroes.html'

class JackView(TemplateView):
    template_name = "hero.html"
    
    def get_context_data(self, **kwargs):
        return {
        "title" : "Jack Frost",
        "body" : "My name is Jack Frost, and I might just be Buddha incarnate.",
        "image" : '/static/images/jackFrost.jpg',
    }

class BigbyWolfView(TemplateView):
    template_name = "hero.html"
    
    def get_context_data(self, **kwargs):
        return {
        'title' : "Bigby Wolf",
        'body' : "My name is Bibgy Wolf, and I work to secure and protect Fables.",
        'image' : '/static/images/bigbyWolf.jpg'
    }

class SpawnView(TemplateView):
    template_name = "hero.html"
    
    def get_context_data(self, **kwargs):
        return {
        "title" : "Spawn",
        "body" : "My name is Spawn, and I fight in Hell",
        "image" : '/static/images/spawn.jpg',
    }