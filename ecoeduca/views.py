from django.shortcuts import render

# Create your views here.


def inicio(request):
    return render(request, 'ecoeduca/inicio.html')

def aprende(request):
    return render(request, 'ecoeduca/aprende.html')

def detalle_residuos_general(request):

    tipos_residuos = [
    {
        "nombre": "Orgánicos",
        "descripcion": (
            "Los residuos orgánicos son materiales biodegradables que provienen de seres vivos. "
            "Al descomponerse naturalmente, pueden transformarse en compost, aportando nutrientes al suelo. "
            "Separarlos correctamente ayuda a reducir la cantidad de basura enviada a los rellenos sanitarios."
        ),
        "ejemplos": [
            "Cáscaras de frutas y verduras",
            "Restos de comida",
            "Bolsas de té o café usado",
            "Hojas secas y residuos de jardinería",
            "Pan o arroz sobrante"
        ],
        "manejo": (
            "Deposítalos en la caneca **verde**, destinada a residuos orgánicos. "
            "Pueden aprovecharse mediante compostaje doméstico o comunitario. "
            "Evita mezclarlos con plásticos, vidrio o metales."
        ),
        "color": "#6bd96b", 
        "icono": "🟢",
        "caneca_color": "Verde",
        "imagen": "ecoeduca/img/residuos/organicos.jpg",
    },
    {
        "nombre": "Reciclables",
        "descripcion": (
            "Los residuos reciclables son materiales que pueden transformarse en nuevos productos. "
            "Su reciclaje reduce la extracción de recursos naturales y el consumo de energía, "
            "favoreciendo la economía circular y la sostenibilidad."
        ),
        "ejemplos": [
            "Botellas plásticas PET",
            "Papel limpio y seco",
            "Cartón sin grasa",
            "Latas de aluminio",
            "Frascos y botellas de vidrio"
        ],
        "manejo": (
            "Deposítalos en la caneca **blanca**, reservada para residuos reciclables. "
            "Asegúrate de limpiarlos y secarlos antes de desecharlos. "
            "Evita incluir residuos con grasa o suciedad."
        ),
        "color": "#d0e7ff",  
        "icono": "⚪",
        "caneca_color": "Blanca",
        "imagen": "ecoeduca/img/residuos/reciclables.jpg",
    },
    {
        "nombre": "No reciclables",
        "descripcion": (
            "Los residuos no reciclables son aquellos que no pueden aprovecharse ni transformarse "
            "por su composición o grado de contaminación. "
            "Su correcta disposición evita malos olores, focos de infección y contaminación ambiental."
        ),
        "ejemplos": [
            "Pañales y toallas higiénicas",
            "Servilletas sucias o papel contaminado con grasa",
            "Colillas de cigarrillo",
            "Envases metalizados de snacks o golosinas",
            "Tapabocas usados"
        ],
        "manejo": (
            "Deposítalos en la caneca **negra**, asignada para residuos no reciclables. "
            "Procura envolverlos antes de desecharlos y no mezclarlos con reciclables u orgánicos."
        ),
        "color": "#d6d6d6", 
        "icono": "⚫",
        "caneca_color": "Negra",
        "imagen": "ecoeduca/img/residuos/no_reciclables.jpg",
    },
]

    return render(request, "ecoeduca/detalle_residuos.html", {"tipos_residuos": tipos_residuos})

def informacion(request):
    return render(request, 'ecoeduca/informacion.html')

def impacto_ambiental(request):
    return render(request, 'ecoeduca/impacto_ambiental.html')