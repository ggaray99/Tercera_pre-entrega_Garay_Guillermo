from django.db import models

# Create your models here.
class ActivosAsignados(models.Model):
    codigo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=255)
    fecha_de_carga = models.DateField()
    usuario_asignado = models.CharField(max_length=100)

class Usuarios(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    puesto = models.CharField(max_length=40)
    sucursal = models.CharField(max_length=40)

class TipoActivos(models.Model):
    codigo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=255)
