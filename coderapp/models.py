from django.db import models

# Create your models here.

class VideoJuego(models.Model):
    genero = models.CharField(max_length=20)
    nombre = models.CharField(max_length=30)
    
    def __str__(self):
        return f"Se creo el videojuego: {self.nombre}. Del genero: {self.genero}"