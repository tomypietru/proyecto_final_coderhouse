from django.shortcuts import render, redirect, get_object_or_404
from coderapp.models import VideoJuego

from django.http import HttpResponseForbidden
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import VideoJuego
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CrearVideoJuegoFormulario
from .models import VideoJuego, Comentario
from .forms import ComentarioForm


def inicio(request):
    return render(request,"coderapp/index.html")



@login_required
def crear_videojuego(request):
    if request.method == 'POST':
        formulario = CrearVideoJuegoFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            videojuego = formulario.save(commit=False)
            videojuego.user = request.user  # Asigna el usuario autenticado
            videojuego.save()
            return redirect("videojuegos")
    else:
        formulario = CrearVideoJuegoFormulario()
    return render(request, 'coderapp/videojuego_templates/crear_videojuego.html', {'formulario': formulario})


class VideoJuegos(ListView):
    model = VideoJuego
    template_name = "coderapp/videojuego_templates/lista_videojuegos.html"
    context_object_name = "videojuegos"
    
                    
class EliminarVideoJuego(LoginRequiredMixin, DeleteView):
    model = VideoJuego
    template_name = "coderapp/videojuego_templates/eliminar_videojuego.html"
    success_url = reverse_lazy("videojuegos")
    
    def get_object(self, queryset=None):
        videojuego = super().get_object(queryset)
        if videojuego.user != self.request.user:
            return HttpResponseForbidden("No tienes permiso para eliminar este videojuego.")
        return videojuego

                    
class EditarVideoJuego(LoginRequiredMixin, UpdateView):        
    model = VideoJuego
    template_name = "coderapp/videojuego_templates/editar_videojuego.html"
    success_url = reverse_lazy("videojuegos")
    fields = ["nombre", "genero", "descripcion", "fecha", "imagen"]
    
    def get_object(self, queryset=None):
        videojuego = super().get_object(queryset)
        if videojuego.user != self.request.user:
            return HttpResponseForbidden("No tienes permiso para editar este videojuego.")
        return videojuego
     

def ver_videojuego(request, pk):
    videojuego = get_object_or_404(VideoJuego, pk=pk)
    comentarios = videojuego.comentarios.all()

    if request.method == 'POST':
        if 'comentario_id' in request.POST:
            comentario = get_object_or_404(Comentario, pk=request.POST.get('comentario_id'))
            if request.POST.get('action') == 'edit' and comentario.autor == request.user:
                form = ComentarioForm(request.POST, instance=comentario)
                if form.is_valid():
                    form.save()
                    return redirect('ver_videojuego', pk=videojuego.pk)
            elif request.POST.get('action') == 'delete' and comentario.autor == request.user:
                comentario.delete()
                return redirect('ver_videojuego', pk=videojuego.pk)
        else:
            form = ComentarioForm(request.POST)
            if form.is_valid():
                comentario = form.save(commit=False)
                comentario.videojuego = videojuego
                comentario.autor = request.user  # Asignar el autor
                comentario.save()
                return redirect('ver_videojuego', pk=videojuego.pk)
    else:
        form = ComentarioForm()

    return render(request, 'coderapp/videojuego_templates/ver_videojuego.html', {'videojuego': videojuego, 'comentarios': comentarios, 'form': form})



def aboutme(request):
    return render(request, "coderapp/aboutme.html")