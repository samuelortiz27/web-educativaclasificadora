from django.urls import path
from . import views

app_name = 'puntos'

urlpatterns = [
    path('', views.mapa_y_busqueda, name='mapa_y_busqueda'),
]