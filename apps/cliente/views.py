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
from django.contrib import messages
from .models import datos_cliente

# Create your views here.
cipher = AESCipher(settings.SECRET_KEY)
key = settings.SECRET_KEY
datetime = datetime.now()
timestampStr = datetime.strftime("%Y%b%d%H%M%S%f")


@csrf_exempt
def uploads(request):
    resultInvalid = []
    resultValid = []
    try:
        if request.method == 'POST':
            first = True
            uploaded_file = request.FILES['document']
            lines = uploaded_file.readlines()
            for line in lines:
                if first:
                    resultValid.append(line.decode(encoding='latin-1').split("\t"))
                    resultInvalid.append(line.decode(encoding='latin-1').split("\t"))
                    first = False
                    continue
                else:
                    values = line.decode(encoding='latin-1').split("\t")
                    if values[27] == '':
                        insert_value(values)
                        resultValid.append(values)
                    else:
                        resultInvalid.append(values)

            listInvalid = listToString(resultInvalid)
            listValid = listToString(resultValid)
            insert_invalid(listInvalid)
            insert_valid(listValid)
            conta = len(resultValid)
            messages.success(request, 'La Importación se Realizo Correctamente, contactos cargados: ' + str(conta - 1))
        return render(request, 'cliente/upload.html')
    except Exception as e:
        messages.success(request, 'Error verifique el archivo')
        return render(request, 'cliente/upload.html')


@csrf_exempt
def insert_value(values):
    try:
        model = [values[0],
                 cipher.encrypt(values[1]),
                 cipher.encrypt(values[2]),
                 values[3],
                 values[4],
                 values[5],
                 values[6],
                 values[7],
                 values[8],
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
                 values[23],
                 cipher.encrypt(values[24]),
                 values[25],
                 values[26],
                 values[27],
                 values[28],
                 values[29],
                 values[30],
                 cipher.encrypt(values[31]),
                 cipher.encrypt(values[32]),
                 values[33],
                 values[34],
                 values[0],
                 cipher.encrypt(values[1]),
                 cipher.encrypt(values[2]),
                 values[3],
                 values[4],
                 values[5],
                 values[6],
                 values[7],
                 values[8],
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
                 values[23],
                 cipher.encrypt(values[24]),
                 values[25],
                 values[26],
                 values[27],
                 values[28],
                 values[29],
                 values[30],
                 cipher.encrypt(values[31]),
                 cipher.encrypt(values[32]),
                 values[33],
                 values[34]
                 ]
        cursor = connection.cursor()
        insert = "INSERT INTO cliente_datos_cliente (NUMERO_CEDULA, NUMERO_CEDULA_NUMERICO, NOMBRES_Y_APELLIDOS, COD_SEXO, DESCRIPCION_SEXO, COD_CIUDADANIA, DESCRIPCION_CIUDADANIA, FECH_NACIMIENTO, CODIGO_LUGAR_NACIMIENTO, CODIGO_NACIONALIDAD, DESCRIPCION_NACIONALIDAD, CODIGO_ESTADO_CIVIL, DESCRIPCION_ESTADO_CIVIL, CODIGO_NIVEL_ESTUDIOS, DESCRIPCION_NIVEL_ESTUDIOS, CODIGO_PROFESION, DESCRIPCION_PROFESION, NOMBRE_CONYUGUE, CEDULA_CONYUGUE, FECHA_MATRIMONIO, LUG_MATRIMONIO, NOMBRES_DEL_PADRE, NAC_PAD, NUMERO_CEDULA_PADRE, NOMBRES_DE_LA_MADRE, NAC_MAD, NUMERO_CEDULA_MADRE, FECH_DEF, LUG_DEF, LUG_INSC, CODIGO_DOMICILIO, CALLE_DOMICILIO, NUMERO_CASA, FECHA_ACTUALIZACION_DATOS, GENERO, ESTADO_PERSONA, created_at, updated_at, state) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 'ACTIVO', current_timestamp(6), current_timestamp(6), '1')"
        update = "ON DUPLICATE KEY UPDATE NUMERO_CEDULA= %s, NUMERO_CEDULA_NUMERICO= %s, NOMBRES_Y_APELLIDOS= %s, COD_SEXO= %s, DESCRIPCION_SEXO= %s, COD_CIUDADANIA= %s, DESCRIPCION_CIUDADANIA= %s, FECH_NACIMIENTO= %s, CODIGO_LUGAR_NACIMIENTO= %s, CODIGO_NACIONALIDAD= %s, DESCRIPCION_NACIONALIDAD= %s, CODIGO_ESTADO_CIVIL= %s, DESCRIPCION_ESTADO_CIVIL= %s, CODIGO_NIVEL_ESTUDIOS= %s, DESCRIPCION_NIVEL_ESTUDIOS= %s, CODIGO_PROFESION= %s, DESCRIPCION_PROFESION= %s, NOMBRE_CONYUGUE= %s, CEDULA_CONYUGUE= %s, FECHA_MATRIMONIO= %s, LUG_MATRIMONIO= %s, NOMBRES_DEL_PADRE= %s, NAC_PAD= %s, NUMERO_CEDULA_PADRE= %s, NOMBRES_DE_LA_MADRE= %s, NAC_MAD= %s, NUMERO_CEDULA_MADRE= %s, FECH_DEF= %s, LUG_DEF= %s, LUG_INSC= %s, CODIGO_DOMICILIO= %s, CALLE_DOMICILIO= %s, NUMERO_CASA= %s, FECHA_ACTUALIZACION_DATOS= %s, GENERO= %s;"
        sql = insert + update 
        cursor.execute(sql, model)
        select_table()
    except Exception as e:
        print(e)
        

def drop_table(request):
    try:
        cursor = connection.cursor()
        sql = 'TRUNCATE table cliente_datos_cliente'
        cursor.execute(sql)
        messages.success(request, 'Archivos eliminados correctamente')
        return render(request, 'cliente/delete.html')
    except Exception as e:
        print(e)
        messages.success(request, 'Error al eliminar el archivo')
        return render(request, 'cliente/delete.html')


def select_table():
    try:
        cursor = connection.cursor()
        sql = 'select * from cliente_datos_cliente'
        cursor.execute(sql)
        results = cursor.fetchall()
    except Exception as e:
        print(e)


def insert_invalid(insert):
    archivo = open(settings.MEDIA_ROOT + 'clientes/' + "registros-invalidos" + str(timestampStr) + ".txt", "w")
    archivo.write(str(insert))
    archivo.close()
    return True


def insert_valid(insert):
    archivo = open(settings.MEDIA_ROOT + 'clientes/' + "registros-validos" + str(timestampStr) + ".txt", "w")
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
    with os.scandir(settings.MEDIA_ROOT + 'clientes/') as ficheros:
        ficheros = [fichero.name for fichero in ficheros if fichero.is_file()]
        paginator = Paginator(ficheros, 5)
        page = request.GET.get('page')
        page_fichero = paginator.get_page(page)
        contexto = {'ficheros': page_fichero}
    return render(request, 'cliente/lista_subidos.html', contexto)


def home(request):
    return render(request, 'cliente/lista_subidos.html')


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT + 'clientes/', path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/text")
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response


class DescargarArchivoView(View):

    def post(self, request, *args, **kwargs):
        form = request.POST['valuer']
        file_path = os.path.join(settings.MEDIA_ROOT + 'clientes/', form)
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='text/plain')
            response['Content-Disposition'] = 'attachment; filename="%s"' % form
            return response
