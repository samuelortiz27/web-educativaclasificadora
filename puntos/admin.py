from django.contrib import admin
from .models import PuntoReciclaje

# Register your models here.

@admin.register(PuntoReciclaje)
class PuntoReciclajeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'categoria_reciclable', 'direccion')
    list_filter = ('tipo', 'categoria_reciclable')
    search_fields = ('nombre', 'direccion')
