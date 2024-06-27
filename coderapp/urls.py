from django.urls import path
from coderapp import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("contacto/", views.contacto, name="contacto"),
    path("videojuegos/crear/", views.crear, name="crear"),
    path("videojuegos/lista/",  views.videojuegos, name="videojuegos"),
    path('eliminar/<int:id>', views.eliminar_videojuego,name='eliminar_videojuego'),
]
