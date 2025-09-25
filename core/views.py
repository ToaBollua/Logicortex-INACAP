from django.shortcuts import render, get_object_or_404, redirect
from .models import Reto, RespuestaUsuario
from .forms import RespuestaForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

def register_view(request):
    if request.user.is_authenticated:
        return redirect('core:lista_retos')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('core:lista_retos')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('core:lista_retos')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_staff:
                return redirect('/admin/')
            return redirect('core:lista_retos')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('core:lista_retos')

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
            es_correcta = respuesta_enviada.strip().lower() == reto.respuesta_correcta.strip().lower()
            
            RespuestaUsuario.objects.create(
                usuario=request.user,
                reto=reto,
                respuesta_enviada=respuesta_enviada,
                es_correcta=es_correcta
            )
            
            if es_correcta:
                request.user.puntuacion += reto.puntuacion
                request.user.save(update_fields=['puntuacion'])

            return redirect('core:lista_retos')
    else:
        form = RespuestaForm()

    return render(request, 'core/detalle_reto.html', {'reto': reto, 'form': form})