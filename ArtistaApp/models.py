from django.db import models

class Artista(models.Model):
    nombre_artista = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=100)
    fechanacimiento = models.DateField()
    cancionescreada = models.IntegerField()
    aniosactivo = models.IntegerField()
# Create your models here.
