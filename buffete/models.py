from django.db import models
from django.utils import timezone

class Abogado(models.Model):
    usuario= models.ForeignKey('auth.User')
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    estado= models.BooleanField(default="True")
    dpi = models.CharField(max_length=20)
    telefono = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    estado= models.BooleanField(default="True")
    dpi = models.CharField(max_length=20)
    telefono = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Expediente(models.Model):
    resumen = models.CharField(max_length=30,blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha_ingreso = models.DateTimeField(default=timezone.now)
    fecha_inicio = models.DateTimeField(blank = True, null = True)
    fecha_finalizacion = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=2,default="1")
    abogado = models.ForeignKey(Abogado, on_delete = models.CASCADE, blank=True, null=True)
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)




# Create your models here.
