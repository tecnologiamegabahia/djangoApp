from django.db import models


# Create your models here.
class actividad_economica(models.Model):
    CODIGO = models.CharField(max_length=150)
    DESCRIPCION = models.CharField(max_length=150)
    ULTIMO_NODO = models.CharField(max_length=150)
    CODIGO_PADRE = models.CharField(max_length=150)
    NIVEL = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    state = models.CharField(max_length=200, default=1)
