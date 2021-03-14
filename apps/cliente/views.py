from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .cryp import AESCipher
from django.db import connection
from django.conf import settings
import os
from datetime import datetime
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views.generic.base import View

# Create your views here.
cipher = AESCipher(settings.SECRET_KEY)
resultInvalid = []
resultValid = []
datetime = datetime.now()
timestampStr = datetime.strftime("%Y%b%d%H%M%S%f")


@csrf_exempt
def uploads(request):
    if request.method == 'POST':
        first = True
        uploaded_file = request.FILES['document']
        lines = uploaded_file.readlines()
        for line in lines:
            if first:
                resultValid.append(line.decode().split("\t"))
                resultInvalid.append(line.decode().split("\t"))
                first = False
                continue
            else:
                values = line.decode().split("\t")
                if values[27] == '':
                    insert_value(values)
                    resultValid.append(values)
                else:
                    resultInvalid.append(values)

        listInvalid = listToString(resultInvalid)
        listValid = listToString(resultValid)
        insert_invalid(listInvalid)
        insert_valid(listValid)

    return render(request, 'cliente/upload.html')


@csrf_exempt
def insert_value(values):
    model = [cipher.encrypt(values[0]),
             cipher.encrypt(values[1]),
             cipher.encrypt(values[2]),
             values[3],
             values[4],
             values[5],
             values[6],
             values[7],
             cipher.encrypt(values[8]),
             cipher.encrypt(values[9]),
             values[10],
             values[11],
             values[12],
             values[13],
             values[14],
             values[15],
             values[16],
             cipher.encrypt(values[17]),
             cipher.encrypt(values[18]),
             cipher.encrypt(values[19]),
             values[20],
             cipher.encrypt(values[21]),
             values[22],
             cipher.encrypt(values[23]),
             cipher.encrypt(values[24]),
             values[25],
             cipher.encrypt(values[26]),
             values[27],
             values[28],
             values[29],
             cipher.encrypt(values[30]),
             cipher.encrypt(values[31]),
             cipher.encrypt(values[32]),
             values[33],
             values[34]
             ]
    cursor = connection.cursor()
    sql = "INSERT INTO cliente_datos_cliente (NUMERO_CEDULA, NUMERO_CEDULA_NUMERICO, NOMBRES_Y_APELLIDOS, COD_SEXO, DESCRIPCION_SEXO, COD_CIUDADANIA, DESCRIPCION_CIUDADANIA, FECH_NACIMIENTO, CODIGO_LUGAR_NACIMIENTO, CODIGO_NACIONALIDAD, DESCRIPCION_NACIONALIDAD, CODIGO_ESTADO_CIVIL, DESCRIPCION_ESTADO_CIVIL, CODIGO_NIVEL_ESTUDIOS, DESCRIPCION_NIVEL_ESTUDIOS, CODIGO_PROFESION, DESCRIPCION_PROFESION, NOMBRE_CONYUGUE, CEDULA_CONYUGUE, FECHA_MATRIMONIO, LUG_MATRIMONIO, NOMBRES_DEL_PADRE, NAC_PAD, NUMERO_CEDULA_PADRE, NOMBRES_DE_LA_MADRE, NAC_MAD, NUMERO_CEDULA_MADRE, FECH_DEF, LUG_DEF, LUG_INSC, CODIGO_DOMICILIO, CALLE_DOMICILIO, NUMERO_CASA, FECHA_ACTUALIZACION_DATOS, GENERO, ESTADO_PERSONA, created_at, updated_at, state) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 'ACTIVO', current_timestamp(6), '', '1');"
    cursor.execute(sql, model)


def insert_invalid(insert):
    archivo = open(settings.MEDIA_ROOT + "registros-invalidos" + str(timestampStr) + ".txt", "w")
    archivo.write(str(insert))
    archivo.close()
    return True


def insert_valid(insert):
    archivo = open(settings.MEDIA_ROOT + "registros-validos" + str(timestampStr) + ".txt", "w")
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
    with os.scandir(settings.MEDIA_ROOT) as ficheros:
        ficheros = [fichero.name for fichero in ficheros if fichero.is_file()]
        paginator = Paginator(ficheros, 10)
        page = request.GET.get('page')
        page_fichero = paginator.get_page(page)

        contexto = {'ficheros': page_fichero}
    return render(request, 'cliente/lista_subidos.html', contexto)


def home(request):
    return render(request, 'cliente/lista_subidos.html')


def download(request, path):
    print(path)
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/text")
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response


class DescargarArchivoView(View):

    def post(self, request, *args, **kwargs):
        form = request.POST['valuer']
        print(form)
        file_path = os.path.join(settings.MEDIA_ROOT, form)
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='text/plain')
            response['Content-Disposition'] = 'attachment; filename="%s"' % form
            return response
