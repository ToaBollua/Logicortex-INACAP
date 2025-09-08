from django.shortcuts import render

def index(request):
    """Muestra la página de inicio."""
    return render(request, 'index.html')