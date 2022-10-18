from urllib import request
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from .models import Article, Hero

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




class ArticleListView(ListView):
    template_name = 'articles/list.html'
    model = Article
    context_object_name = 'articles'


class ArticleDetailView(DetailView):
    template_name = 'articles/detail.html'
    model = Article
    context_object_name = 'article'


class ArticleAddView(LoginRequiredMixin, CreateView):
    template_name = 'articles/add.html'
    model = Article
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ArticleEditView(LoginRequiredMixin, UpdateView):
    template_name = 'articles/edit.html'
    model = Article
    fields = ['title', 'content']


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'articles/delete.html'
    model = Article
    success_url = reverse_lazy('article_list')
