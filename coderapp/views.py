from django.shortcuts import render, redirect
from coderapp.models import VideoJuego
from coderapp.forms import CrearVideojuegoFormulario


from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import VideoJuego
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime


def inicio(request):
    return render(request,"coderapp/index.html")

class CrearVideoJuego(CreateView):
    model = VideoJuego
    template_name = "coderapp/videojuego_templates/crear_videojuego.html"
    success_url = reverse_lazy("videojuegos")
    fields = ["nombre", "genero", "descripcion", "imagen"]
   


class VideoJuegos(ListView):
    model = VideoJuego
    template_name = "coderapp/videojuego_templates/lista_videojuegos.html"
    context_object_name = "videojuegos"
    
                    # LoginRequiredMixin, 
class EliminarVideoJuego(DeleteView):
    model = VideoJuego
    template_name = "coderapp/videojuego_templates/eliminar_videojuego.html"
    success_url = reverse_lazy("videojuegos")

                    # LoginRequiredMixin,
class EditarVideoJuego(UpdateView):        
    model = VideoJuego
    template_name = "coderapp/videojuego_templates/editar_videojuego.html"
    success_url = reverse_lazy("videojuegos")
    fields = ["nombre", "genero", "descripcion", "imagen"]
     
class VerVideoJuego(DetailView):
    model = VideoJuego
    template_name = "coderapp/videojuego_templates/ver_videojuego.html"
     

def aboutme(request):
    return render(request, "coderapp/aboutme.html")