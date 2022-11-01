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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from hero.views import HeroDetailView, HeroCreateView, HeroListView, HeroView, HeroDeleteView, HeroUpdateView, UserUpdateView
from hero.views import ArticleAddView, ArticleDeleteView, ArticleDetailView, ArticleEditView, ArticleListView
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
    path('articles/', ArticleListView.as_view(), name='article_list'),
    path('articles/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('articles/add', ArticleAddView.as_view(), name='article_add'),
    path('articles/<int:pk>/', ArticleEditView.as_view(), name='article_edit'),
    path('articles/<int:pk>/delete', ArticleDeleteView.as_view(), name='article_delete'),

    # Hero
    path('Hero/',                HeroListView.as_view(),    name='Hero_list'),
    path('Hero/<int:pk>',        HeroDetailView.as_view(),  name='Hero_detail'),
    path('Hero/add',             HeroCreateView.as_view(),  name='Hero_add'),
    path('Hero/<int:pk>/',       HeroUpdateView.as_view(),  name='Hero_edit'),
    path('Hero/<int:pk>/delete', HeroDeleteView.as_view(),  name='Hero_delete'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)