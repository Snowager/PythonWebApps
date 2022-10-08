from urllib import request
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from hero.forms import HeroForm
from django.shortcuts import render

from .models import Author, Hero

class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "registration/account_edit.html"
    model = User
    fields = ['first_name', 'last_name', 'username', 'email']
    success_url = reverse_lazy('Hero_list')


class HeroView(RedirectView):
    url = reverse_lazy( 'Hero_list')


class HeroListView(ListView):
    template_name =  "Hero/list.html"
    model = Hero
    context_object_name =  'heroes'


class HeroDetailView(DetailView):
    template_name =  "Hero/detail.html"
    model = Hero
    context_object_name =  'hero'


class HeroCreateView(CreateView):
    template_name =  "Hero/add.html"
    model = Hero
    fields = '__all__'
    success_url = reverse_lazy('Hero_list')

class HeroUpdateView(UpdateView):
    template_name = "Hero/edit.html"
    model = Hero
    fields = '__all__'
    success_url = reverse_lazy('Hero_list')


class HeroDeleteView(DeleteView):
    model = Hero
    template_name = 'Hero/delete.html'
    success_url = reverse_lazy('Hero_list')


def list_heroes(author):
    return dict(articles=Hero.objects.filter(author=author))


def get_author(user):
    return Author.objects.get_or_create(user=user)[0]


class AuthorHomeView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_anonymous:
            return '/article/'
        return f'/author/{get_author(self.request.user).pk}'


class AuthorListView(ListView):
    template_name = 'author_list.html'
    model = Author

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        return kwargs


class AuthorDetailView(DetailView):
    template_name = 'author_detail.html'
    model = Author

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs.update(list_heroes(kwargs.get('object')))
        return kwargs


class AuthorAddView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/account_add.html'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "registration/account_edit.html"
    model = User
    fields = ['first_name', 'last_name', 'username', 'email']
    success_url = reverse_lazy('author_home')


class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "author_edit.html"
    model = Author
    fields = '__all__'


class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    model = Author
    template_name = 'author_delete.html'
    success_url = reverse_lazy('author_list')


