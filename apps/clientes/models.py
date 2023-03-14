from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombres = models.CharField(max_length=255, unique=True)
    apellidos = models.CharField(max_length=255, unique=True)
    dni = models.IntegerField(max_length=9, unique=True)
    telefono = models.CharField(max_length=15, unique=True)
    correo = models.CharField(max_length=255, unique=True)
    direccion = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nombres + " " + self.apellidos
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"