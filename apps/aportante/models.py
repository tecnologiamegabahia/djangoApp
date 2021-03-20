from django.db import models


# Create your models here.
class aportante(models.Model):
    NUMAFI = models.CharField(max_length=150)
    CODDIVPOL = models.CharField(max_length=150)
    RUCEMP = models.CharField(max_length=150)
    CODSUC = models.CharField(max_length=150)
    CODTIPEMP = models.CharField(max_length=150)
    NOMEMP = models.CharField(max_length=500)
    TELSUC = models.CharField(max_length=500)
    DIRSUC = models.CharField(max_length=500)
    FAXSUC = models.CharField(max_length=150)
    APENOMAFI = models.CharField(max_length=500)
    DIRAFI = models.CharField(max_length=150)
    TELAFI = models.CharField(max_length=150)
    CELULAR = models.CharField(max_length=150)
    EMAIL = models.CharField(max_length=150)
    SALARIO = models.CharField(max_length=150)
    FECINGAFI = models.CharField(max_length=150)
    FECSALAFI = models.CharField(max_length=150)
    OCUAFI = models.CharField(max_length=150)
    V19 = models.CharField(max_length=150)
    MES = models.CharField(max_length=150)
