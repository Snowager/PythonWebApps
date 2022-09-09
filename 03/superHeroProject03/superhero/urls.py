from django.urls import path
from .views import JackView, BigbyWolfView, IndexView, SpawnView

urlpatterns = [
    path('', IndexView.as_view()),
    path('jackFrost', JackView.as_view()),
    path('bigbyWolf', BigbyWolfView.as_view()),
    path('spawn', SpawnView.as_view()),
]
