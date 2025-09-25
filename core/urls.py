from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.lista_retos, name='lista_retos'),
    path('reto/<int:reto_id>/', views.detalle_reto, name='detalle_reto'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]