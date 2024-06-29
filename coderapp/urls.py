from django.urls import path
from coderapp import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("aboutme/", views.aboutme, name="aboutme"),
    path("videojuegos/crear/", views.CrearVideoJuego.as_view(), name="crear"),
    path("videojuegos/lista/",  views.VideoJuegos.as_view(), name="videojuegos"),
    path("videojuegos/<int:pk>/", views.VerVideoJuego.as_view(), name="ver_videojuego"),
    path('videojuegos/<int:pk>/eliminar/', views.EliminarVideoJuego.as_view() ,name='eliminar_videojuego'),
    path('videojuegos/<int:pk>/editar/', views.EditarVideoJuego.as_view() ,name='editar_videojuego'),

]
