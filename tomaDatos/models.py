from django.db import models

# Create your models here.

class Sintomas(models.Model):
    temperatura = models.FloatField()
    dolorGarganta = models.IntegerField()
    tos = models.IntegerField()
    senGusto = models.IntegerField()
    senOlfato = models.IntegerField()
    respiracion = models.IntegerField()