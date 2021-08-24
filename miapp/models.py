import random

from django.db import models

# Create your models here.


class Persona(models.Model):
    nombre = models.CharField(max_length=120,default="visita")
    edad = models.IntegerField(default=18)
    def __str__(self):
        return f'{self.nombre} edad { self.edad}'