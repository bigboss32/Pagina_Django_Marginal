from django.urls import path
from . import views
urlpatterns = [
  path('', views.inicio_sesion),
  path('registro', views.registro_usuario),
]