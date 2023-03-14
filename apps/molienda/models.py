from django.db import models
from ..clientes.models import Cliente
# Create your models here.

class MaterialDureza(models.Model):
    dureza = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.dureza
    
    class Meta:
        verbose_name = "Material Dureza"
        verbose_name_plural = "Material Dureza"

class MaterialTamaño(models.Model):
    tamaño = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.tamaño

    class Meta:
        verbose_name = "Material Tamaño"
        verbose_name_plural = "Material Tamaño"

class MaterialHumedad(models.Model):
    humedad = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.humedad

    class Meta:
        verbose_name = "Material Humedad"
        verbose_name_plural = "Material Humedad"

class MaterialSulfuro(models.Model):
    sulfuro = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.sulfuro

    class Meta:
        verbose_name = "Material Sulfuro"
        verbose_name_plural = "Material Sulfuro"

class OrigenMaterial(models.Model):
    origen = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.origen

    class Meta:
        verbose_name = "Origen del Material"
        verbose_name_plural = "Origen del Material"

class Molienda(models.Model):
    fecha_carga = models.DateTimeField()
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    cod_asignado = models.CharField(max_length=2, unique=True)
    kg_estimados = models.IntegerField()
    dureza = models.ForeignKey(MaterialDureza, on_delete=models.CASCADE)
    tamaño = models.ForeignKey(MaterialTamaño, on_delete=models.CASCADE)
    humedad = models.ForeignKey(MaterialHumedad, on_delete=models.CASCADE)
    sulfuro = models.ForeignKey(MaterialSulfuro, on_delete=models.CASCADE)
    origen = models.ForeignKey(OrigenMaterial, on_delete=models.CASCADE)
    observaciones = models.TextField()
    guia_recepcion = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.fecha_carga)

    class Meta:
        verbose_name = "Molienda"
        verbose_name_plural = "Molienda"