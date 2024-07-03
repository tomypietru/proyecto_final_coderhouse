from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class VideoJuego(models.Model):
    nombre = models.CharField(max_length=30)
    genero = models.CharField(max_length=20)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateField(default=timezone.now)
    imagen = models.ImageField(upload_to='videojuego_imagenes/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Videojuego: {self.nombre}. Del genero: {self.genero}"

class Comentario(models.Model):
    videojuego = models.ForeignKey(VideoJuego, related_name='comentarios', on_delete=models.CASCADE)
    texto = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario por {self.autor.username} en {self.videojuego.nombre}"