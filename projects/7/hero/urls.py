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
from xml.dom.minidom import Document
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.views.generic import RedirectView
from .views import HeroDetailView, HeroCreateView, HeroListView, HeroView, HeroDeleteView, HeroUpdateView, UserCreationForm, UserUpdateView, UpdateView
from .views import Author, AuthorAddView, AuthorDeleteView, AuthorDetailView, AuthorHomeView, AuthorListView, AuthorUpdateView, get_author
from users import views as user_views

urlpatterns = [

    # Home
    path('',                        HeroView.as_view(), name='home'),

    # Admin
    path('admin/', admin.site.urls),

    # User
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/<int:pk>/',          UserUpdateView.as_view(),  name='user_edit'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),

    # Author
    path('',                           RedirectView.as_view(url='author/home')),
    path('author/',                    AuthorListView.as_view(),    name='author_list'),
    path('author/home',                AuthorHomeView.as_view(),    name='author_home'),
    path('author/<int:pk>',            AuthorDetailView.as_view(),  name='author_detail'),
    path('author/add/',                AuthorAddView.as_view(),     name='author_add'),
    path('author/<int:pk>/',           AuthorUpdateView.as_view(),  name='author_edit'),
    path('author/<int:pk>/delete',     AuthorDeleteView.as_view(),  name='author_delete'),

    # Hero
    path('Hero/',                HeroListView.as_view(),    name='Hero_list'),
    path('Hero/<int:pk>',        HeroDetailView.as_view(),  name='Hero_detail'),
    path('Hero/add',             HeroCreateView.as_view(),  name='Hero_add'),
    path('Hero/<int:pk>/',       HeroUpdateView.as_view(),  name='Hero_edit'),
    path('Hero/<int:pk>/delete', HeroDeleteView.as_view(),  name='Hero_delete'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)