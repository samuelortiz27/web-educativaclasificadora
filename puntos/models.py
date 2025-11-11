from django.db import models

TIPOS_RESIDUOS = [
    ('orgánico', 'Orgánico'),
    ('reciclable', 'Reciclable'),
    ('no_reciclable', 'No reciclable'),
]

CATEGORIAS_RECICLABLES = [
    ('carton', 'Cartón'),
    ('botellas', 'Botellas'),
    ('papel', 'Papel'),
    ('plastico', 'Plástico'),
    ('metal', 'Metal'),
    ('vidrio', 'Vidrio'),
]

class PuntoReciclaje(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=TIPOS_RESIDUOS)
    categoria_reciclable = models.CharField(max_length=20, choices=CATEGORIAS_RECICLABLES, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"


