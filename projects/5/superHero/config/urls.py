from django.contrib import admin
from django.urls import path

from hero.views import HeroDetailView, HeroListView

urlpatterns = [

    # Admin
    path('admin/', admin.site.urls),

    # Note
    path('', HeroListView.as_view()),
    path('<int:pk>', HeroDetailView.as_view()),
]