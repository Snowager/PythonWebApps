from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Hero


class HeroView(RedirectView):
    url = reverse_lazy( 'Hero_list')


class HeroListView(ListView):
    template_name =  "Hero/list.html"
    model = Hero
    context_object_name =  'Heros'


class HeroDetailView(DetailView):
    template_name =  "Hero/detail.html"
    model = Hero
    context_object_name =  'Hero'


class HeroCreateView(CreateView):
    template_name =  "Hero/add.html"
    model = Hero
    fields = '__all__'


class HeroUpdateView(UpdateView):
    template_name =  "Hero/edit.html"
    model = Hero
    fields = '__all__'


class HeroDeleteView(DeleteView):
    model = Hero
    template_name =  "Hero/delete.html"
    success_url = reverse_lazy( 'Hero_list')