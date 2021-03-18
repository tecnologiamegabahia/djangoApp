from django.db import models


# Create your models here.
class contribuyente(models.Model):
    PERSONA_SOCIEDAD = models.CharField(max_length=250)
    NUMERO_RUC = models.CharField(max_length=150)
    RUC_ANTERIOR = models.CharField(max_length=150)
    RAZON_SOCIAL = models.CharField(max_length=150)
    NOMBRE_FANTASIA_COMERCIAL = models.CharField(max_length=250)
    FECHA_INSCRIPCION_RUC = models.CharField(max_length=150)
    LISTA_BLANCA = models.CharField(max_length=150)
    FECHA_INICIO_ACTIVIDADES = models.CharField(max_length=150)
    VALOR_PATRIMONIO = models.CharField(max_length=150)
    OBLIGADO = models.CharField(max_length=150)
    FECHA_NACIMIENTO = models.CharField(max_length=150)
    FECHA_CANCELACION = models.CharField(max_length=150)
    PASAPORTE = models.CharField(max_length=150)
    NUMERO_REGISTRO_COLEGIO_GREMIO = models.CharField(max_length=150)
    FECHA_INSCRIPCION_COLEG_GREMIO = models.CharField(max_length=150)
    CALIFICACION_ARTESANAL = models.CharField(max_length=150)
    FECHA_CALIFICACION_ARTESANAL = models.CharField(max_length=150)
    FECHA_SOLICITUD_SUSPENSION = models.CharField(max_length=150)
    FECHA_SUSPENSION_DEFINITIVA = models.CharField(max_length=150)
    FECHA_REINICIO_ACTIVIDADES = models.CharField(max_length=150)
    CALLE = models.CharField(max_length=150)
    NUMERO = models.CharField(max_length=150)
    INTERSECCION = models.CharField(max_length=150)
    TELEFONO = models.CharField(max_length=150)
    CORREO_ELECTRONICO = models.CharField(max_length=150)
    REFERENCIA_UBICACION = models.CharField(max_length=150)
    FECHA_CONSTITUCION = models.CharField(max_length=150)
    NUMERO_REGISTRO_MERCANTIL = models.CharField(max_length=150)
    CAPITAL_SUSCRITO = models.CharField(max_length=150)
    CONSTITUCION = models.CharField(max_length=150)
    CARGO_REPRESENTANTE_LEGAL = models.CharField(max_length=150)
    FECHA_NOMBRAMIENTO = models.CharField(max_length=150)
    ACTIVIDAD_ECONOMICA_PRINCIPAL = models.CharField(max_length=150)
    AGENTE_RETENCION = models.CharField(max_length=150)
    CATEGORIA_RISE = models.CharField(max_length=150)
    CLASE_CONTRIBUYENTE = models.CharField(max_length=150)
    COMERCIO_EXTERIOR = models.CharField(max_length=150)
    CONTADOR = models.CharField(max_length=150)
    ESTADO_PERSONA_NATURAL = models.CharField(max_length=150)
    ESTADO_SOCIEDAD = models.CharField(max_length=150)
    ESTRUCTURA_ORGANIZACIONAL = models.CharField(max_length=150)
    FECHA_ACTUALIZACION = models.CharField(max_length=150)
    NUMERO_PATRONAL = models.CharField(max_length=150)
    PAIS = models.CharField(max_length=150)
    REPRESENTANTE_LEGAL = models.CharField(max_length=150)
    TIPO_CONTRIBUYENTE = models.CharField(max_length=150)
    TIPO_VISA = models.CharField(max_length=150)
    UBICACION_GEOGRAFICA = models.CharField(max_length=250)
    GERENTE_GENERAL = models.CharField(max_length=150)
    EMPRESA_PUBLICA = models.CharField(max_length=150)
    FECHA_NOMBRAMIENTO_GERENTE = models.CharField(max_length=150)
    ZONA_FRANCA = models.CharField(max_length=150)
    BIENES_SERVICIOS = models.CharField(max_length=150)
    OBLIGACION_VENCIDA = models.CharField(max_length=150)
    FECHA_NOTIFICACION = models.CharField(max_length=150)
    FECHA_GESTION = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    state = models.CharField(max_length=200, default=1)