from django.shortcuts import render, redirect
from coderapp.models import VideoJuego
from coderapp.forms import CrearVideojuegoFormulario


# Create your views here.

def inicio(request):
    return render(request,"coderapp/index.html")

    
def crear(request):
    formulario = CrearVideojuegoFormulario()
    if request.method == "POST":
        formulario = CrearVideojuegoFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            videojuego = VideoJuego(nombre=datos.get("nombre"), genero=datos.get("genero"))
            videojuego.save()
            return redirect("videojuegos")
    return render(request, "coderapp/videojuego_templates/crear_videojuego.html", {"formulario": formulario})



def videojuegos(request):
    videojuego = VideoJuego.objects.all()
    return render(request, "coderapp/videojuego_templates/lista_videojuegos.html", {"videojuegos": videojuego})
    
def eliminar_videojuego(request,id):
    videojuego = VideoJuego.objects.get(id=id)
    videojuego.delete()
    return redirect('videojuegos')     
    

def contacto(request):
    return render(request, "coderapp/contacto.html")