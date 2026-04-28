from django.urls import path
from . import views

urlpatterns = [
    path('', views.pokedex, name='index'),
    path('pokemon/<str:name>/', views.pokemons_details, name='pokemon_details'),
]
