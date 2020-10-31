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