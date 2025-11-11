from django import forms
from puntos.models import TIPOS_RESIDUOS, CATEGORIAS_RECICLABLES

class BusquedaPuntosForm(forms.Form):
    tipo_residuo = forms.ChoiceField(
        choices=[('', 'Todos')] + TIPOS_RESIDUOS,
        required=False,
        label="Tipo de residuo"
    )
    categoria = forms.ChoiceField(
        choices=[('', 'Todas')] + CATEGORIAS_RECICLABLES,
        required=False,
        label="Categoría reciclable"
    )