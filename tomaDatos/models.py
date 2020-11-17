from django.db import models

# Create your models here.

class Sintomas(models.Model):
    temperatura = models.FloatField()
    dolorGarganta = models.IntegerField()
    tos = models.IntegerField()
    senGusto = models.TextField()
    senOlfato = models.TextField()
    respiracion = models.IntegerField()
    dolorPecho = models.IntegerField(default=0)
    Secrecion = models.TextField(default="No")
    Malestar = models.IntegerField(default=0)
    Diarrea = models.TextField(default="No")
    DolorEspalda = models.TextField(default="No")
    DolorCabeza = models.TextField(default="No")
    resultado = models.TextField(default="No",null=True)