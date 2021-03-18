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
resultValid = []
datetime = datetime.now()
timestampStr = datetime.strftime("%Y%b%d%H%M%S%f")


# Create your views here.

# def para cargar archivo
@csrf_exempt
def uploads(request):
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
                    print(values)
                    insert_value(values)
                    resultValid.append(values)

            listInvalid = listToString(resultInvalid)
            listValid = listToString(resultValid)
            insert_invalid(listInvalid)
            insert_valid(listValid)
            conta = len(resultValid)
            messages.success(request, 'La Importación se Realizo Correctamente, contactos cargados: ' + str(conta - 1))
        return render(request, 'medios_contacto/upload.html')
    except Exception as e:
        messages.success(request, 'Error verifique el archivo')
        return render(request, 'medios_contacto/upload.html')


# def para inserta valores table
@csrf_exempt
def insert_value(values):
    try:
        model = [values[0],
                 values[1],
                 values[2],
                 cipher.encrypt(values[3]),
                 values[4]
                 ]
        cursor = connection.cursor()
        sql = "INSERT INTO medio_contacto_medio_contacto(CODIGO, VALOR, ESTABLECIMIENTO, NUMERO_RUC, TIPO_MEDIO_CONTACTO, created_at, updated_at, state)VALUES(%s, %s, %s, %s, %s,current_timestamp(6), current_timestamp(6), '1')"
        cursor.execute(sql, model)
    except Exception as e:
        resultInvalid.append(values)
        print(e)


# def crear archivo registros invalidos
def insert_invalid(insert):
    archivo = open(settings.MEDIA_ROOT + "medios_contacto/registros-invalidos" + str(timestampStr) + ".txt", "w")
    archivo.write(str(insert))
    archivo.close()
    return True


# def crear archivo registros validos
def insert_valid(insert):
    archivo = open(settings.MEDIA_ROOT + "medios_contacto/registros-validos" + str(timestampStr) + ".txt", "w")
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
    with os.scandir(settings.MEDIA_ROOT + 'medios_contacto/') as ficheros:
        ficheros = [fichero.name for fichero in ficheros if fichero.is_file()]
        paginator = Paginator(ficheros, 5)
        page = request.GET.get('page')
        page_fichero = paginator.get_page(page)
        contexto = {'ficheros': page_fichero}
    return render(request, 'medios_contacto/lista_subidos.html', contexto)


def home(request):
    return render(request, 'medios_contacto/lista_subidos.html')


# def descargar archivos existentes
def download(request, path):
    print(path)
    file_path = os.path.join(settings.MEDIA_ROOT + 'medios_contacto/', path)
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
        file_path = os.path.join(settings.MEDIA_ROOT + 'medios_contacto/', form)
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='text/plain')
            response['Content-Disposition'] = 'attachment; filename="%s"' % form
            return response
