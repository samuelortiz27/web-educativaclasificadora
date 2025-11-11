from django.shortcuts import render
from puntos.models import PuntoReciclaje
from .forms import BusquedaPuntosForm

def mapa_y_busqueda(request):
    form = BusquedaPuntosForm(request.GET or None)
    puntos = PuntoReciclaje.objects.all()

    if form.is_valid():
        tipo = form.cleaned_data.get('tipo_residuo')
        categoria = form.cleaned_data.get('categoria')

        if tipo:
            puntos = puntos.filter(tipo=tipo)
        if categoria:
            puntos = puntos.filter(categoria_reciclable=categoria)

    return render(request, 'puntos/mapa_y_busqueda.html', {'form': form,'puntos': puntos})
