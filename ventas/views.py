from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Persona
from django.contrib.auth import login,logout,authenticate
from django.db import DatabaseError
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
      return render(request,'index.html')

def inicio_sesion(request):

    return render(request,'inicio_sesion.html')

def registro_usuario(request):
    if request.method == 'GET':
        return render(request, 'registro_usuario.html')
    else:
        try:
            if request.POST['password1'] == request.POST['password2']:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'],
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    email=request.POST['email']
                )
                user.save()
                login(request,user)
                return redirect('home')
            else:
                return render(request, 'registro_usuario.html',{
                    'error':'contraseña no conincicden'
                })
        except DatabaseError:
            return HttpResponse('Error al conectar con la base de datos')

def cerrar_sesion(request):
    logout(request)
    return redirect('inicar_sesion')

def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'inicio_sesion.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, 'inicio_sesion.html', {'error': 'Credenciales incorrectas'})
        else:
            login(request, user)
            return redirect('home')
        

def crear_comprador(request):
    return render(request, 'pages/compradores/Crear_comprador.html')


def crear_articulo(request):
    return render(request, 'pages/articulos/crear_articulo.html')


def crear_venta(request):
    return render(request, 'pages/ventas/registrar_venta.html')