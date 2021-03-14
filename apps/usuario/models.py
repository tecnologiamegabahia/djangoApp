from django.db import models
from apps.rol.models import rol
from django.contrib.auth.models import AbstractUser


# Create your models here.
class usuario(AbstractUser):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=250)
    documento = models.CharField(max_length=50)
    email = models.CharField(max_length=250)
    phone = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    created_user_id = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)
    updated_user_id = models.CharField(max_length=200)
    status = models.CharField(max_length=200, default=1)
    rol = models.ForeignKey(rol, null=True, blank=True, on_delete=models.CASCADE)  # Relacion Rol
