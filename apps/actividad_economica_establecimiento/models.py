from django.db import models


# Create your models here.
class actividad_economica_est(models.Model):
    ACTIVIDAD_ECONOMICA = models.CharField(max_length=150)
    ESTABLECIMIENTO = models.CharField(max_length=150)
    NUMERO_RUC = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    state = models.CharField(max_length=200, default=1)
