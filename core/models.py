from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Modelo para extender el usuario nativo de Django y añadir puntuación.
class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    puntuacion = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.usuario.username} - {self.puntuacion} puntos'

# Modelo para los retos o acertijos.
class Reto(models.Model):
    class Dificultad(models.TextChoices):
        FACIL = 'Fácil'
        MEDIO = 'Medio'
        DIFICIL = 'Difícil'

    titulo = models.CharField(max_length=200)
    enunciado = models.TextField()
    respuesta_correcta = models.CharField(max_length=255)
    dificultad = models.CharField(max_length=10, choices=Dificultad.choices, default=Dificultad.FACIL)
    puntuacion = models.IntegerField(default=10)
    fecha_publicacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo

# Modelo para registrar las respuestas de los usuarios a los retos.
class RespuestaUsuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    reto = models.ForeignKey(Reto, on_delete=models.CASCADE)
    respuesta_enviada = models.CharField(max_length=255)
    es_correcta = models.BooleanField(default=False)
    fecha_intento = models.DateTimeField(default=timezone.now)

    def __str__(self):
        estado = "Correcta" if self.es_correcta else "Incorrecta"
        return f'{self.usuario.username} -> {self.reto.titulo} ({estado})'
