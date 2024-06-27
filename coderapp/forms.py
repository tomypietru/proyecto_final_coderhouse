from django import forms

class BaseVideojuegoFormulario(forms.Form):
    genero = forms.CharField(max_length=20)
    nombre = forms.CharField(max_length=30)
    
class CrearVideojuegoFormulario(BaseVideojuegoFormulario):
    ...    