"""confi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import HeroDetailView, HeroCreateView, HeroUpdateView, HeroDeleteView, HeroListView, HeroView

urlpatterns = [

    # Home
    path('',                        HeroView.as_view(), name='home'),

    # Hero
    path('Hero/',                HeroListView.as_view(),    name='Hero_list'),
    path('Hero/<int:pk>',        HeroDetailView.as_view(),  name='Hero_detail'),
    path('Hero/add',             HeroCreateView.as_view(),  name='Hero_add'),
    path('Hero/<int:pk>/',       HeroUpdateView.as_view(),  name='Hero_edit'),
    path('Hero/<int:pk>/delete', HeroDeleteView.as_view(),  name='Hero_delete'),
]