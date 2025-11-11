from django.urls import path
from . import views

app_name = 'ecoeduca'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('informacion/', views.informacion, name='informacion'),
    path('aprende/', views.aprende, name='aprende'),
    #path('aprende/<str:tipo>/', views.detalle_residuos, name='detalle_residuos'),
    path('aprende/detalle-residuos/', views.detalle_residuos_general, name='detalle_residuos_general'),
    path('impacto_ambiental/', views.impacto_ambiental, name='impacto_ambiental'),
]