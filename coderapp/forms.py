from django import forms
from .models import VideoJuego
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
class VideoJuegoFormulario(forms.ModelForm):
    class Meta:
        model = VideoJuego
        fields = ["nombre", "genero", "descripcion", "fecha", "imagen"]

class CrearVideoJuegoFormulario(forms.ModelForm):
    class Meta:
        model = VideoJuego
        fields = ["nombre", "genero", "descripcion", "fecha", "imagen"]

class EditarVideoJuegoFormulario(VideoJuegoFormulario):
    class Meta:
        model = VideoJuego
        fields = ["nombre", "genero", "descripcion", "fecha", "imagen"]

class BaseVideojuegoFormulario(forms.Form):
    genero = forms.CharField(max_length=20)
    nombre = forms.CharField(max_length=30)
    
class CrearVideojuegoFormulario(BaseVideojuegoFormulario):
    ...    