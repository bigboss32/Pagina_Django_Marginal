from django.urls import path
from . import views
urlpatterns = [
  path('', views.inicio_sesion),
  path('registro', views.registro_usuario),
  path('home', views.index,name='home'),
  path('cerrar_sesion', views.cerrar_sesion),
  path('inicar_sesion', views.iniciar_sesion,name='inicar_sesion'),
  path('crear_comprador', views.crear_comprador,name='crear_comprador'),
]