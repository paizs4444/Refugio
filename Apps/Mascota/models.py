from django.db import models
from django.contrib.auth import get_user_model
from Apps.Adopcion.models import Persona

OPCIONES_GENERO = (
    ('M' , 'Macho'),
    ('H' , 'Hembra'),
)

# Create your models here.
class Vacuna(models.Model):
    """docstring for Vacuna."""
    Nombre = models.CharField(max_length = 50)

    def __str__(self):
        return "%s" % (self.Nombre )



class Mascota(models.Model):
    """docstring for Mascota."""
    Nombre = models.CharField(max_length = 50)
    Sexo = models.CharField(max_length=1, choices = OPCIONES_GENERO,)
    Edad_aproximada = models.IntegerField()
    Fecha_rescate = models.DateField()
    Persona = models.ForeignKey(Persona,  verbose_name='Persona', null=True, blank=True, on_delete=models.CASCADE )
    Vacuna = models.ManyToManyField(Vacuna, verbose_name='Vacuna', blank=True)

    def __str__(self):
        return "%s" % (self.Nombre )
