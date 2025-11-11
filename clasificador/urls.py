from django.urls import path
from . import views

app_name = 'clasificador'
urlpatterns = [
    path('clasificar/', views.clasificar_residuo, name='clasificar'),
]