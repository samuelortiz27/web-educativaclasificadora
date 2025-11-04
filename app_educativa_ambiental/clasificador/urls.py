from django.urls import path
from . import views

urlpatterns = [
    path('', views.clasificar_residuo, name='clasificar_residuo'),
]