from django.db import models
from datetime import datetime

class VideoJuego(models.Model):
    nombre = models.CharField(max_length=30)
    genero = models.CharField(max_length=20)
    descripcion = models.TextField(blank=True, null=True) 
    imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True) 
    # fecha =
    
    def __str__(self):
        return f"Videojuego: {self.nombre}. Del genero: {self.genero} "