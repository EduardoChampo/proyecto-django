from django.shortcuts import render, HttpResponse

menu="""
<a href="/">Home</a>
<a href="/contacto">Contactos</a>
"""

def principal(request):
    contenido="<h1>HOLA DJANGO </h1>"
    return HttpResponse(menu+contenido)

def contacto(request):
    contenido = """ <h2> Contacto </h2>
    <p>Nombre: <input type="text" name="nombre"/></p>
    <p>Mensaje: </p><p><textarea cols="50" rows="10"></textarea></p>
    <p><input type="button" name="enviar" value="Enviar"/></p>"""
    return HttpResponse(contenido)

# Create your views here.
