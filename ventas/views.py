from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Persona
from django.db import DatabaseError
# Create your views here.
def inicio_sesion(request):

    return render(request,'index.html')

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
                return HttpResponse('Registro exitoso')
            else:
                return render(request, 'registro_usuario.html',{
                    'error':'contraseña no conincicden'
                })
        except DatabaseError:
            return HttpResponse('Error al conectar con la base de datos')

    