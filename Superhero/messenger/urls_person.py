
from django.urls import path

from .views_person import PersonDeleteView, PersonDetailView, PersonListView, PersonCreateView, PersonUpdateView


urlpatterns = [

    # Person
    path('person/',                       PersonListView.as_view(),    name='person_list'),
    path('person/<int:pk>',               PersonDetailView.as_view(),  name='person_detail'),
    path('person/add',                    PersonCreateView.as_view(),  name='person_add'),
    path('person/<int:pk>/',              PersonUpdateView.as_view(),  name='person_edit'),
    path('person/<int:pk>/delete',        PersonDeleteView.as_view(),  name='person_delete'),

]
