from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from usuarios.models import DatosExtra
class NuestroFormularioDeCreacion(UserCreationForm):
    
    email = forms.EmailField()
    password1 = forms.CharField(label="Contrasenia", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contrasenia", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email","password1","password2"]
        help_texts = {key: "" for key in fields}
    
  
class VerPerfilForm(forms.ModelForm):
    username = forms.CharField(label='Nombre de usuario', required=False, widget=forms.TextInput(attrs={'readonly': True, 'class': 'form-control'}))
    email = forms.EmailField(label='Email', required=False, widget=forms.EmailInput(attrs={'readonly': True, 'class': 'form-control'}))
    first_name = forms.CharField(label='Nombre', required=False, widget=forms.TextInput(attrs={'readonly': True, 'class': 'form-control'}))
    last_name = forms.CharField(label='Apellido', required=False, widget=forms.TextInput(attrs={'readonly': True, 'class': 'form-control'}))
    avatar = forms.ImageField(label='Avatar', required=False, widget=forms.ClearableFileInput(attrs={'readonly': True, 'class': 'form-control'})) 
    
    class Meta:
        model = DatosExtra
        fields = ['username', 'email', 'first_name', 'last_name', 'avatar']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = self.instance.user
        self.fields['username'].initial = user.username
        self.fields['email'].initial = user.email
        self.fields['first_name'].initial = user.first_name
        self.fields['last_name'].initial = user.last_name    

    
class EditarPerfil(UserChangeForm):
    password = None
    email = forms.EmailField()
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'avatar']