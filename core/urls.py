from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_retos, name='lista_retos'),
    path('reto/<int:reto_id>/', views.detalle_reto, name='detalle_reto'),
]
