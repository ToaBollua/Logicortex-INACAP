from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Reto, RespuestaUsuario

# --- Admin para el Modelo de Usuario Personalizado ---
class CustomUserAdmin(UserAdmin):
    """
    Personalización del panel de administración para el modelo CustomUser.
    Muestra la puntuación en la lista y en los detalles del usuario.
    """
    # Añadir 'puntuacion' a los fieldsets para que se muestre en el formulario de edición
    fieldsets = UserAdmin.fieldsets + (
        ('Campos Personalizados', {'fields': ('puntuacion',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Campos Personalizados', {'fields': ('puntuacion',)}),
    )
    
    # Mostrar 'puntuacion' en la lista de usuarios
    list_display = ('username', 'email', 'is_staff', 'puntuacion')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')

# --- Admin para el Modelo de Retos ---
@admin.register(Reto)
class RetoAdmin(admin.ModelAdmin):
    """
    Personalización del panel de administración para el modelo Reto.
    """
    list_display = ('titulo', 'dificultad', 'puntuacion', 'fecha_publicacion')
    list_filter = ('dificultad', 'fecha_publicacion')
    search_fields = ('titulo', 'enunciado')
    ordering = ('-fecha_publicacion',)

# --- Admin para el Modelo de Respuestas de Usuario ---
@admin.register(RespuestaUsuario)
class RespuestaUsuarioAdmin(admin.ModelAdmin):
    """
    Personalización del panel de administración para el modelo RespuestaUsuario.
    """
    list_display = ('usuario', 'reto', 'es_correcta', 'fecha_intento')
    list_filter = ('es_correcta', 'fecha_intento', 'reto__dificultad')
    search_fields = ('usuario__username', 'reto__titulo')
    ordering = ('-fecha_intento',)
    
    # Optimiza las consultas de la base de datos
    autocomplete_fields = ('usuario', 'reto')

# Registrar el modelo de usuario personalizado con su admin personalizado
admin.site.register(CustomUser, CustomUserAdmin)