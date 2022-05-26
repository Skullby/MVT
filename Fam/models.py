from django.db import models

# Create your models here.
class Fam(models.Model):
    nombre = models.CharField(max_length=40)
    numero = models.IntegerField()
    fechaDeNac = models.DateField()