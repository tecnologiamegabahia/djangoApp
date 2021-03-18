from django.db import models


# Create your models here.
class establecimiento(models.Model):
    NUMERO_RUC = models.CharField(max_length=150)
    NUMERO_ESTABLECIMIENTO = models.CharField(max_length=150)
    NOMBRE_FANTASIA_COMERCIAL = models.CharField(max_length=150)
    FECHA_INSCRIPCION = models.CharField(max_length=150)
    FECHA_INICIO_ACTIVIDADES = models.CharField(max_length=150)
    FECHA_REINICIO_ACTIVIDADES = models.CharField(max_length=150)
    FECHA_ACTUALIZACION = models.CharField(max_length=150)
    FECHA_CIERRE = models.CharField(max_length=150)
    ESTADO_ESTABLECIMIENTO = models.CharField(max_length=150)
    UBICACION_GEOGRAFICA = models.CharField(max_length=150)
    BARRIO = models.CharField(max_length=150)
    CALLE = models.CharField(max_length=150)
    INTERSECCION = models.CharField(max_length=150)
    NOMBRE_EDIFICIO = models.CharField(max_length=150)
    NUMERO = models.CharField(max_length=150)
    NUMERO_OFICINA = models.CharField(max_length=150)
    NUMERO_PISO = models.CharField(max_length=150)
    REFERENCIA_UBICACION = models.CharField(max_length=150)
    TIPO_ESTABLECIMIENTO = models.CharField(max_length=150)
    FECHA_VERIFICACION = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    state = models.CharField(max_length=200, default=1)
