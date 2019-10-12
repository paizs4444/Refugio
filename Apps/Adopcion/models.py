from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Persona(models.Model):
    """docstring for Persona."""
    Nombre = models.CharField(max_length = 50)
    Apellido = models.CharField(max_length = 50)
    Edad = models.IntegerField()
    Telefono = models.CharField(max_length=12, null=True)
    Email = models.EmailField()
    Domicilio = models.TextField()


    def __str__(self):
        return "%s %s" % (self.Nombre, self.Apellido )

class Solicitud(models.Model):
    """docstring for Solicitud."""
    Persona = models.ForeignKey(Persona , verbose_name='Persona', null=True, blank=True,  on_delete=models.CASCADE )
    Numero_mascotas = models.IntegerField()
    Razones = models.TextField()

    def __str__(self):
        return "%s" % (self.id )
