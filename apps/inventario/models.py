from django.db import models

# Create your models here.
class Inventario(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    stock = models.IntegerField()
    precio = models.IntegerField()
    observacion = models.TextField()