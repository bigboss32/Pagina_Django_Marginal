from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TipoDocumento(models.TextChoices):
    CEDULA = 'CEDULA', 'Documento Nacional de Identidad'
    PASAPORTE = 'PASAPORTE', 'Pasaporte'
   

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    tipo_documento = models.CharField(max_length=50, choices=TipoDocumento.choices)
    cedula = models.IntegerField()
    celular = models.IntegerField()
    correo = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Venta(models.Model):
   persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
   fecha = models.DateField()
   total = models.IntegerField()
   estado_pagado = models.BooleanField(default=False)
   tipo_comprobante=models.CharField(max_length=50)

class Devolucion(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    fecha = models.DateField()
    motivo = models.TextField()
    cantidad_devuelta = models.IntegerField()

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    estado = models.BooleanField(default=False)

class Articulo(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio_venta=models.IntegerField()
    nombre = models.CharField(max_length=50)
    codigo=models.IntegerField()
    descripcion = models.CharField(max_length=250)

class Articulo_venta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.IntegerField()

class Ubicacion(models.Model):
    comprador = models.ForeignKey(Persona, on_delete=models.CASCADE)
    ciudad=models.CharField(max_length=50)
    barrio=models.CharField(max_length=50)
    dirrecion=models.CharField(max_length=50)
