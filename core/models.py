from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.conf import settings
from django.core.validators import MinValueValidator

# Modelo de Usuario Personalizado que extiende AbstractUser.
class CustomUser(AbstractUser):
    """
    Modelo de usuario personalizado que hereda de AbstractUser.
    Añade un campo para la puntuación del usuario.
    """
    puntuacion = models.IntegerField(
        "Puntuación",
        default=0,
        validators=[MinValueValidator(0)],
        help_text="Puntuación acumulada del usuario."
    )

    def __str__(self):
        return f'{self.username} ({self.puntuacion} puntos)'

# Modelo para los retos o acertijos.
class Reto(models.Model):
    """
    Modelo que representa un reto o acertijo con su dificultad y puntuación.
    """
    class Dificultad(models.TextChoices):
        FACIL = 'Fácil'
        MEDIO = 'Medio'
        DIFICIL = 'Difícil'

    titulo = models.CharField(max_length=200)
    enunciado = models.TextField()
    respuesta_correcta = models.CharField(max_length=255)
    dificultad = models.CharField(
        max_length=10,
        choices=Dificultad.choices,
        default=Dificultad.FACIL
    )
    puntuacion = models.IntegerField(
        "Puntuación del reto",
        default=10,
        validators=[MinValueValidator(1)],
        help_text="Puntos que otorga el reto al ser resuelto."
    )
    fecha_publicacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo

# Modelo para registrar las respuestas de los usuarios a los retos.
class RespuestaUsuario(models.Model):
    """
    Registra los intentos de un usuario para resolver un reto.
    """
    # Usamos settings.AUTH_USER_MODEL para referenciar al usuario personalizado.
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='respuestas'
    )
    reto = models.ForeignKey(
        Reto,
        on_delete=models.CASCADE,
        related_name='respuestas'
    )
    respuesta_enviada = models.CharField(max_length=255)
    es_correcta = models.BooleanField(default=False)
    fecha_intento = models.DateTimeField(default=timezone.now)

    def __str__(self):
        estado = "Correcta" if self.es_correcta else "Incorrecta"
        return f'{self.usuario.username} -> {self.reto.titulo} ({estado})'