from django.db import models


# Create your models here.
class representante_legal(models.Model):
    NUMERO_IDENTIFICACION = models.CharField(max_length=150)
    TIPO_IDENTIFICACION = models.CharField(max_length=150)
    NOMBRE = models.CharField(max_length=150)
    CALLE = models.CharField(max_length=150)
    NUMERO = models.CharField(max_length=150)
    INTERSECCION = models.CharField(max_length=150)
    TELEFONO = models.CharField(max_length=150)
    CORREO_ELECTRONICO = models.CharField(max_length=150)
    REFERENCIA_UBICACION = models.CharField(max_length=150)
    PASAPORTE = models.CharField(max_length=150)
    PAIS = models.CharField(max_length=150)
    TIPO_VISA = models.CharField(max_length=150)
    UBICACION_GEOGRAFICA = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    state = models.CharField(max_length=200, default=1)
