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

cipher = AESCipher(settings.SECRET_KEY)
resultInvalid = []
datetime = datetime.now()
timestampStr = datetime.strftime("%Y%b%d%H%M%S%f")


# Create your views here.

# def para cargar archivo
@csrf_exempt
def uploads(request):
    resultValid = []
    try:
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
                    values = line.decode(encoding='latin-1').split("\t")
                    insert_value(values)
                    resultValid.append(values)

            listInvalid = listToString(resultInvalid)
            listValid = listToString(resultValid)
            insert_invalid(listInvalid)
            insert_valid(listValid)
            conta = len(resultValid)
            messages.success(request, 'La Importación se Realizo Correctamente, contactos cargados: ' + str(conta - 1))
        return render(request, 'representante_legal/upload.html')
    except Exception as e:
        messages.success(request, 'Error verifique el archivo')
        return render(request, 'representante_legal/upload.html')


# def para inserta valores table
@csrf_exempt
def insert_value(values):
    try:
        model = [cipher.encrypt(values[0]),
                 values[1],
                 cipher.encrypt(values[2]),
                 values[3],
                 values[4],
                 values[5],
                 values[6],
                 cipher.encrypt(values[7]),
                 values[8],
                 cipher.encrypt(values[9]),
                 values[10],
                 values[11],
                 values[12],
                 ]
        cursor = connection.cursor()
        sql = "INSERT INTO representante_legal_representante_legal(NUMERO_IDENTIFICACION, TIPO_IDENTIFICACION, NOMBRE, CALLE, NUMERO, INTERSECCION, TELEFONO, CORREO_ELECTRONICO, REFERENCIA_UBICACION, PASAPORTE, PAIS, TIPO_VISA, UBICACION_GEOGRAFICA, created_at, updated_at, state)VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, current_timestamp(6), current_timestamp(6), '1');"
        cursor.execute(sql, model)
    except Exception as e:
        resultInvalid.append(values)
        print(e)


# def crear archivo registros invalidos
def insert_invalid(insert):
    archivo = open(settings.MEDIA_ROOT + "representante_legal/registros-invalidos" + str(timestampStr) + ".txt", "w")
    archivo.write(str(insert))
    archivo.close()
    return True


# def crear archivo registros validos
def insert_valid(insert):
    archivo = open(settings.MEDIA_ROOT + "representante_legal/registros-validos" + str(timestampStr) + ".txt", "w")
    archivo.write(str(insert))
    archivo.close()
    return True


# def convertir estring
def listToString(s):
    values = '\n'.join(str(v) for v in s)
    line = values.replace('\r\n', '')
    line = line.replace(',', '\t')
    line = line.replace('[', '')
    line = line.replace(']', '')
    line = line.replace('\'', '')

    return line


# def verificar archivos existentes, mapa de paginas
def verificarArchivos(request):
    with os.scandir(settings.MEDIA_ROOT + 'representante_legal/') as ficheros:
        ficheros = [fichero.name for fichero in ficheros if fichero.is_file()]
        paginator = Paginator(ficheros, 5)
        page = request.GET.get('page')
        page_fichero = paginator.get_page(page)
        contexto = {'ficheros': page_fichero}
    return render(request, 'representante_legal/lista_subidos.html', contexto)


def home(request):
    return render(request, 'representante_legal/lista_subidos.html')


# def descargar archivos existentes
def download(request, path):
    print(path)
    file_path = os.path.join(settings.MEDIA_ROOT + 'representante_legal/', path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/text")
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response


# clase descargar archivos existentes
class DescargarArchivoView(View):

    def post(self, request, *args, **kwargs):
        form = request.POST['valuer']
        print(form)
        file_path = os.path.join(settings.MEDIA_ROOT + 'representante_legal/', form)
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='text/plain')
            response['Content-Disposition'] = 'attachment; filename="%s"' % form
            return response
