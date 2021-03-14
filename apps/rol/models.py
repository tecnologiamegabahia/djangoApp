from django.db import models


# Create your models here.
class rol(models.Model):
    code = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    config = models.TextField()
    permisoAdmin = models.CharField(max_length=50)
    permisoProcesos = models.CharField(max_length=50)
    permisoContactos = models.CharField(max_length=50)
    permisoGestion = models.CharField(max_length=50)
    permisoEstadisticas = models.CharField(max_length=50)
    permisoReportes = models.CharField(max_length=50)
    permisoCalidad = models.CharField(max_length=50)
    permisoMonitoreo = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    state = models.CharField(max_length=200, default=1)

    def __str__(self):
        return '{}'.format(self.name)
