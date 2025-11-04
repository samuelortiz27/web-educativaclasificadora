from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.templatetags.static import static
from .ml.predict import predict_image

def clasificar_residuo(request):
    resultado = None
    info = None
    color_contenedor = None
    imagen_url = None
    contenedor_img = None

    if request.method == 'POST' and request.FILES.get('imagen'):
        imagen = request.FILES['imagen']
        fs = FileSystemStorage()
        filename = fs.save(imagen.name, imagen)
        imagen_url = fs.url(filename)

        ruta_imagen = fs.path(filename)
        resultado = predict_image(ruta_imagen)

        resultado_lower = resultado.lower()

        if resultado_lower in ['carton', 'vidrio', 'plastico', 'metal', 'papel']:
            info = "♻️ Este residuo es reciclable. Debes depositarlo en el contenedor blanco."
            color_contenedor = "#FFFFFF"
            contenedor_img = static('clasificador/img/contenedor_reciclable.jpg')
            text_color = "#000000"  # negro para fondo blanco
        elif resultado_lower in ['organico', 'orgánico']:
            info = "🌿 Este residuo es orgánico. Debes depositarlo en el contenedor verde."
            color_contenedor = "#28a745"
            contenedor_img = static('clasificador/img/contenedor_organico.jpg')
            text_color = "#ffffff"
        elif resultado_lower in ['basura', 'no reciclable', 'mixto']:
            info = "🗑️ Este residuo no es reciclable. Debes depositarlo en el contenedor negro."
            color_contenedor = "#000000"
            contenedor_img = static('clasificador/img/contenedor_no_reciclable.jpg')
            text_color = "#ffffff"
        else:
            info = "No se reconoce el tipo de residuo. Intenta con otra imagen."
            color_contenedor = "#6c757d"
            contenedor_img = None

    return render(request, 'clasificador/clasificador.html', {
        'resultado': resultado,
        'imagen_url': imagen_url,
        'info': info,
        'color_contenedor': color_contenedor,
        'contenedor_img': contenedor_img,
        'text_color': text_color
    })