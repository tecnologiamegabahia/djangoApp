from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from apps.cliente.cryp import AESCipher
from django.db import connection
from django.conf import settings
import os
from datetime import datetime
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views.generic.base import View
from django.contrib import messages

# Create your views here.
cipher = AESCipher(settings.SECRET_KEY)
resultInvalid = []
datetime = datetime.now()
timestampStr = datetime.strftime("%Y%b%d%H%M%S%f")


@csrf_exempt
def uploads(request):
    resultValid = []
    try:
        if request.method == 'POST':
            first = True
            drop_table()
            uploaded_file = request.FILES['document']
            lines = uploaded_file.readlines()
            for line in lines:
                if first:
                    resultValid.append(line.decode().split("\t"))
                    resultInvalid.append(line.decode().split("\t"))
                    first = False
                    continue
                else:
                    values = line.decode(encoding='latin-1').split("\t")
                    insert_value(values)
                    resultValid.append(values)

            listInvalid = listToString(resultInvalid)
            listValid = listToString(resultValid)
            insert_invalid(listInvalid)
            insert_valid(listValid)
            conta = len(resultValid)
            messages.success(request, 'La Importación se Realizo Correctamente, contactos cargados: ' + str(conta - 1))
        return render(request, 'contribuyentes/upload.html')
    except Exception as e:
        messages.success(request, 'Error verifique el archivo')
        return render(request, 'contribuyentes/upload.html')


@csrf_exempt
def insert_value(values):
    try:
        model = [values[0],
                 values[1],
                 '',
                 cipher.encrypt(values[3]),
                 values[4],
                 cipher.encrypt(values[5]),
                 values[6],
                 cipher.encrypt(values[7]),
                 cipher.encrypt(values[8]),
                 values[9],
                 cipher.encrypt(values[10]),
                 cipher.encrypt(values[11]),
                 cipher.encrypt(values[12]),
                 values[13],
                 values[14],
                 values[15],
                 values[16],
                 values[17],
                 values[18],
                 values[19],
                 values[20],
                 values[21],
                 values[22],
                 cipher.encrypt(values[23]),
                 cipher.encrypt(values[24]),
                 values[25],
                 values[26],
                 values[27],
                 values[28],
                 values[29],
                 values[30],
                 values[31],
                 values[32],
                 values[33],
                 values[34],
                 values[35],
                 values[36],
                 values[37],
                 values[38],
                 values[39],
                 values[40],
                 values[41],
                 values[42],
                 values[43],
                 values[44],
                 values[45],
                 values[46],
                 values[47],
                 values[48],
                 values[49],
                 values[50],
                 values[51],
                 values[52],
                 values[53],
                 values[54],
                 values[55]
                 ]
        cursor = connection.cursor()
        sql = "INSERT INTO contribuyente_contribuyente(PERSONA_SOCIEDAD, NUMERO_RUC, RUC_ANTERIOR, RAZON_SOCIAL, NOMBRE_FANTASIA_COMERCIAL, FECHA_INSCRIPCION_RUC, LISTA_BLANCA, FECHA_INICIO_ACTIVIDADES, VALOR_PATRIMONIO, OBLIGADO, FECHA_NACIMIENTO, FECHA_CANCELACION, PASAPORTE, NUMERO_REGISTRO_COLEGIO_GREMIO, FECHA_INSCRIPCION_COLEG_GREMIO, CALIFICACION_ARTESANAL, FECHA_CALIFICACION_ARTESANAL, FECHA_SOLICITUD_SUSPENSION, FECHA_SUSPENSION_DEFINITIVA, FECHA_REINICIO_ACTIVIDADES, CALLE, NUMERO, INTERSECCION, TELEFONO, CORREO_ELECTRONICO, REFERENCIA_UBICACION, FECHA_CONSTITUCION, NUMERO_REGISTRO_MERCANTIL, CAPITAL_SUSCRITO, CONSTITUCION, CARGO_REPRESENTANTE_LEGAL, FECHA_NOMBRAMIENTO, ACTIVIDAD_ECONOMICA_PRINCIPAL, AGENTE_RETENCION, CATEGORIA_RISE, CLASE_CONTRIBUYENTE, COMERCIO_EXTERIOR, CONTADOR, ESTADO_PERSONA_NATURAL, ESTADO_SOCIEDAD, ESTRUCTURA_ORGANIZACIONAL, FECHA_ACTUALIZACION, NUMERO_PATRONAL, PAIS, REPRESENTANTE_LEGAL, TIPO_CONTRIBUYENTE, TIPO_VISA, UBICACION_GEOGRAFICA, GERENTE_GENERAL, EMPRESA_PUBLICA, FECHA_NOMBRAMIENTO_GERENTE, ZONA_FRANCA, BIENES_SERVICIOS, OBLIGACION_VENCIDA, FECHA_NOTIFICACION, FECHA_GESTION, created_at, updated_at, state) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, current_timestamp(6), current_timestamp(6), '1');"

        cursor.execute(sql, model)
    except Exception as e:
        resultInvalid.append(values)
        print(e)


def insert_invalid(insert):
    archivo = open(settings.MEDIA_ROOT + "contribuyentes/registros-invalidos" + str(timestampStr) + ".txt", "w")
    archivo.write(str(insert))
    archivo.close()
    return True


def drop_table():
    try:
        cursor = connection.cursor()
        sql = 'TRUNCATE table contribuyente_contribuyente'
        cursor.execute(sql)
    except Exception as e:
        print(e)


def insert_valid(insert):
    archivo = open(settings.MEDIA_ROOT + "contribuyentes/registros-validos" + str(timestampStr) + ".txt", "w")
    archivo.write(str(insert))
    archivo.close()
    return True


def listToString(s):
    values = '\n'.join(str(v) for v in s)
    line = values.replace('\r\n', '')
    line = line.replace(',', '\t')
    line = line.replace('[', '')
    line = line.replace(']', '')
    line = line.replace('\'', '')

    return line


def verificarArchivos(request):
    with os.scandir(settings.MEDIA_ROOT + 'contribuyentes/') as ficheros:
        ficheros = [fichero.name for fichero in ficheros if fichero.is_file()]
        paginator = Paginator(ficheros, 5)
        page = request.GET.get('page')
        page_fichero = paginator.get_page(page)
        contexto = {'ficheros': page_fichero}
    return render(request, 'contribuyentes/lista_subidos.html', contexto)


def home(request):
    return render(request, 'contribuyentes/lista_subidos.html')


def download(request, path):
    print(path)
    file_path = os.path.join(settings.MEDIA_ROOT + 'contribuyentes/', path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/text")
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response


class DescargarArchivoView(View):

    def post(self, request, *args, **kwargs):
        form = request.POST['valuer']
        print(form)
        file_path = os.path.join(settings.MEDIA_ROOT + 'contribuyentes/', form)
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='text/plain')
            response['Content-Disposition'] = 'attachment; filename="%s"' % form
            return response
