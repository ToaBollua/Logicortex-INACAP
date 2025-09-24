from django.shortcuts import render, get_object_or_404, redirect
from .models import Reto, RespuestaUsuario, PerfilUsuario
from .forms import RespuestaForm
from django.contrib.auth.decorators import login_required

def lista_retos(request):
    retos = Reto.objects.all().order_by('-fecha_publicacion')
    return render(request, 'core/lista_retos.html', {'retos': retos})

@login_required
def detalle_reto(request, reto_id):
    reto = get_object_or_404(Reto, pk=reto_id)
    if request.method == 'POST':
        form = RespuestaForm(request.POST)
        if form.is_valid():
            respuesta_enviada = form.cleaned_data['respuesta']
            es_correcta = respuesta_enviada.lower() == reto.respuesta_correcta.lower()
            
            # Guardar el intento del usuario
            RespuestaUsuario.objects.create(
                usuario=request.user,
                reto=reto,
                respuesta_enviada=respuesta_enviada,
                es_correcta=es_correcta
            )
            
            # Actualizar puntuación si es correcta
            if es_correcta:
                perfil, created = PerfilUsuario.objects.get_or_create(usuario=request.user)
                perfil.puntuacion += reto.puntuacion
                perfil.save()

            return redirect('lista_retos') # Redirige a la lista de retos tras responder
    else:
        form = RespuestaForm()

    return render(request, 'core/detalle_reto.html', {'reto': reto, 'form': form})
