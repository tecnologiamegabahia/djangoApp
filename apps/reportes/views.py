from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse, JsonResponse
import xlwt
from django.conf import settings
from apps.cliente.cryp import AESCipher
from apps.actividad_economica.models import actividad_economica
from django.views.generic import ListView, TemplateView
from apps.ubicacione_geografica.models import ubicacion_goegrafica
from datetime import datetime

# Create your views here.


cipher = AESCipher(settings.SECRET_KEY)


def reporte_cumpleanios_children(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="reporte_cumpleanios_children.xls"'
    cursor = connection.cursor()
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('reporte_cumpleanios_children')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = [
        'NOMBRES_Y_APELLIDOS',
        'FECHA_NACIMIENTO',
        'AÑOS_CUMPLIDOS',
        'NOMBRE_CANTON',
        'DESCRIPCION_SEXO',
        'NOMBRES_DEL_PADRE',
        'FECHA_NACIMIENTO_PADRE',
        'AÑOS_CUMPLIDOS_PADRE',
        'LUGAR_NACIMIENTO_PADRE',
        'NIVEL_ESTUDIOS_PADRE',
        'PROFESION_PADRE',
        'SEXO_PADRE',
        'CELULAR_PADRE_1',
        'CELULAR_PADRE_2',
        'CELULAR_PADRE_3',
        'CELULAR_PADRE_4',
        'CELULAR_PADRE_5',
        'CELULAR_PADRE_6',
        'CELULAR_PADRE_7',
        'CELULAR_PADRE_8',
        'CELULAR_PADRE_9',
        'CELULAR_PADRE_10',
        'CORREO_PADRE_1',
        'CORREO_PADRE_2',
        'CORREO_PADRE_3',
        'CORREO_PADRE_4',
        'CORREO_PADRE_5',
        'CORREO_PADRE_6',
        'CORREO_PADRE_7',
        'CORREO_PADRE_8',
        'CORREO_PADRE_9',
        'CORREO_PADRE_10',
        'NOMBRES_DE_LA_MADRE',
        'FECHA_NACIMIENTO_MADRE',
        'AÑOS_CUMPLIDOS_MADRE',
        'NIVEL_ESTUDIOS_MADRE',
        'PROFESION_MADRE',
        'SEXO_MADRE',
        'CELULAR_MADRE_1',
        'CELULAR_MADRE_2',
        'CELULAR_MADRE_3',
        'CELULAR_MADRE_4',
        'CELULAR_MADRE_5',
        'CELULAR_MADRE_6',
        'CELULAR_MADRE_7',
        'CELULAR_MADRE_8',
        'CELULAR_MADRE_9',
        'CELULAR_MADRE_10',
        'CORREO_MADRE_1',
        'CORREO_MADRE_2',
        'CORREO_MADRE_3',
        'CORREO_MADRE_4',
        'CORREO_MADRE_5',
        'CORREO_MADRE_6',
        'CORREO_MADRE_7',
        'CORREO_MADRE_8',
        'CORREO_MADRE_9',
        'CORREO_MADRE_10'
    ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    form = request.POST or None
    sexo = form['sexo']
    dia = form['dia']
    mes = form['mes']
    edad = form['edad']
    ciudad = form['ciudad']

    cursor.execute(
        "CALL reporte_cumpleanios_children('" + mes + "','" + dia + "','" + sexo + "','" + edad + "','" + ciudad + "')")

    rows = cursor.fetchall()
    list = []
    for row in rows:
        try:
            rowss = [(cipher.decrypt(row[0])),
                     (row[1]),
                     (row[2]),
                     (row[3]),
                     (row[4]),
                     (cipher.decrypt(row[5])),
                     (row[6]),
                     (row[7]),
                     (row[8]),
                     (row[9]),
                     (row[10]),
                     (row[11]),
                     (row[12]),
                     (row[13]),
                     (row[14]),
                     (row[15]),
                     (row[16]),
                     (row[17]),
                     (row[18]),
                     (row[19]),
                     (row[20]),
                     (row[21]),
                     (row[22]),
                     (row[23]),
                     (row[24]),
                     (row[25]),
                     (row[26]),
                     (row[27]),
                     (row[28]),
                     (row[29]),
                     (row[30]),
                     (row[31]),
                     (cipher.decrypt(row[32])),
                     (row[33]),
                     (row[34]),
                     (row[35]),
                     (row[36]),
                     (row[37]),
                     (row[38]),
                     (row[39]),
                     (row[40]),
                     (row[41]),
                     (row[42]),
                     (row[43]),
                     (row[44]),
                     (row[45]),
                     (row[46]),
                     (row[47]),
                     (row[48]),
                     (row[49]),
                     (row[50]),
                     (row[51]),
                     (row[52]),
                     (row[53]),
                     (row[54]),
                     (row[55]),
                     (row[56]),
                     (row[57])]
        except IndexError as e:
            break
        list.append(rowss)
    print(list)
    for row in list:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


def index(request):
    return render(request, 'reportes/reporte_cumpleanios_children.html')


def index_ci(request):
    return render(request, 'reportes/reporte_cumpleanios_children_ci.html')


def conteo_cliente(request):
    try:
        cursor = connection.cursor()
        sql = 'select count(*) from cliente_datos_cliente'
        cursor.execute(sql)
        count = cursor.fetchone()
        contexto = {'count': count}
        return render(request, 'reportes/reporte_conteo_contribuyente.html', contexto)
    except Exception as e:
        print(e)


def conteo_contribuyentes_naturales(request):
    try:
        cursor = connection.cursor()
        sql = "select count(*) from contribuyente_contribuyente cc where PERSONA_SOCIEDAD = 'PNL'"
        cursor.execute(sql)
        count = cursor.fetchone()
        persona = 'NATURALES'
        contexto = {'count': count, 'persona': persona}
        return render(request, 'reportes/reporte_conteo_contribuyente.html', contexto)
    except Exception as e:
        print(e)


def conteo_contribuyentes_juridicos(request):
    try:
        cursor = connection.cursor()
        sql = "select count(*) from contribuyente_contribuyente cc where PERSONA_SOCIEDAD != 'PNL'"
        cursor.execute(sql)
        count = cursor.fetchone()
        persona = 'JURIDICAS'
        contexto = {'count': count, 'persona': persona}
        return render(request, 'reportes/reporte_conteo_contribuyente.html', contexto)
    except Exception as e:
        print(e)


def conteo_empleados(request):
    try:
        cursor = connection.cursor()
        sql = "select count(*) from aportante_aportante cc"
        cursor.execute(sql)
        count = cursor.fetchone()
        contexto = {'count': count}
        return render(request, 'reportes/reporte_conteo_empleados.html', contexto)
    except Exception as e:
        print(e)


class form_view_combo(TemplateView):
    template_name = 'reportes/reporte_negocios.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nivel1'] = actividad_economica.objects.filter(NIVEL__contains='1')
        context['nivel2'] = actividad_economica.objects.filter(NIVEL__contains='2')
        context['nivel3'] = actividad_economica.objects.filter(NIVEL__contains='3')
        context['nivel4'] = actividad_economica.objects.filter(NIVEL__contains='4')
        context['nivel5'] = actividad_economica.objects.filter(NIVEL__contains='5')
        context['nivel6'] = actividad_economica.objects.filter(NIVEL__contains='6')
        context['nivel7'] = actividad_economica.objects.filter(NIVEL__contains='7')
        context['nivelUbicacion1'] = ubicacion_goegrafica.objects.filter(NIVEL__contains='1')
        context['nivelUbicacion2'] = ubicacion_goegrafica.objects.filter(NIVEL__contains='2')
        context['nivelUbicacion3'] = ubicacion_goegrafica.objects.filter(NIVEL__contains='3')
        context['nivelUbicacion4'] = ubicacion_goegrafica.objects.filter(NIVEL__contains='4')

        return context


def reporte_negocio(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="reporte_negocios.xls"'
    cursor = connection.cursor()
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('reporte_cumpleanios_children')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = [
        'RAZON_SOCIAL',
        'NOMBRE_FANTASIA_COMERCIAL',
        'FECHA_INSCRIPCION_RUC',
        'FECHA_INICIO_ACTIVIDADES',
        'OBLIGADO',
        'FECHA_NACIMIENTO',
        'FECHA_REINICIO_ACTIVIDADES',
        'TELEFONO',
        'CORREO_ELECTRONICO',
        'ACTIVIDAD_ECONOMICA_PRINCIPAL',
        'ESTADO_PERSONA_NATURAL',
        'DESCRIPCION_LUGAR_UBICACION',
        'CODIGO_ECONOMICA_PRINCIPAL',
        'ACTIVIDAD_ECONOMICA_PRINCIPAL',
        'CODIGO_TIPO_CONTACTO_1',
        'CELULAR_1',
        'CORREO_1',
        'CODIGO_TIPO_CONTACTO_2',
        'CELULAR_2',
        'CORREO_2',
        'CODIGO_TIPO_CONTACTO_3',
        'CELULAR_3',
        'CORREO_3',
        'CODIGO_TIPO_CONTACTO_4',
        'CELULAR_4',
        'CORREO_4',
        'CODIGO_TIPO_CONTACTO_5',
        'CELULAR_5',
        'CORREO_5',
        'CODIGO_TIPO_CONTACTO_6',
        'CELULAR_6',
        'CORREO_6',
        'CODIGO_TIPO_CONTACTO_7',
        'CELULAR_7',
        'CORREO_7',
        'CODIGO_TIPO_CONTACTO_8',
        'CELULAR_8',
        'CORREO_8',
        'CODIGO_TIPO_CONTACTO_9',
        'CELULAR_9',
        'CORREO_9',
        'CODIGO_TIPO_CONTACTO_10',
        'CELULAR_10',
        'CORREO_10'
    ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    form = request.POST or None
    print(form)

    economica_p = form['nivel7']
    ciudad_p = request.POST.get('txtvariable1', False)
    contribuyente_p = form['Contribuyente']
    estado_p = form['Estado']
    fechai_p = form['date_time']
    fechaf_p = form['date_time']
    if fechai_p == '':
        fi = datetime.strptime('1900-01-01', "%Y-%m-%d").strftime('%d/%m/%Y')
        ff = datetime.strptime('2030-01-01', "%Y-%m-%d").strftime('%d/%m/%Y')
    else:
        fi = datetime.strptime(fechai_p, "%Y-%m-%d").strftime('%d/%m/%Y')
        ff = datetime.strptime(fechaf_p, "%Y-%m-%d").strftime('%d/%m/%Y')

    cursor.execute(
        "CALL reporte_negocios('" + economica_p + "','" + ciudad_p + "','" + contribuyente_p + "','" + estado_p + "','"
        + str(fi) + "','" + str(ff) + "')")

    rows = cursor.fetchall()
    list = []
    for row in rows:
        try:
            rowss = [(cipher.decrypt(row[0])),
                     (row[1]),
                     (cipher.decrypt(row[2])),
                     (cipher.decrypt(row[3])),
                     (row[4]),
                     (cipher.decrypt(row[5])),
                     (row[6]),
                     (cipher.decrypt(row[7])),
                     (cipher.decrypt(row[8])),
                     (row[9]),
                     (row[10]),
                     (row[11]),
                     (row[12]),
                     (row[13]),
                     (row[14]),
                     (row[15]),
                     (row[16]),
                     (row[17]),
                     (row[18]),
                     (row[19]),
                     (row[20]),
                     (row[21]),
                     (row[22]),
                     (row[23]),
                     (row[24]),
                     (row[25]),
                     (row[26]),
                     (row[27]),
                     (row[28]),
                     (row[29]),
                     (row[30]),
                     (row[31]),
                     (row[32]),
                     (row[33]),
                     (row[34]),
                     (row[35]),
                     (row[36]),
                     (row[37]),
                     (row[38]),
                     (row[39]),
                     (row[40]),
                     (row[41]),
                     (row[42]),
                     (row[43])]
        except IndexError as e:
            break
        list.append(rowss)
    print(list)
    for row in list:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


def reporte_cumpleanios_children_ci(request):
    form = request.POST or None
    ci_p = form['ci_p']
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="reporte_cumpleanios_children_ci' + ci_p + '.xls"'
    cursor = connection.cursor()
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('reporte_cumpleanios_children_ci')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = [
        'NOMBRES_Y_APELLIDOS',
        'FECHA_NACIMIENTO',
        'AÑOS_CUMPLIDOS',
        'NOMBRE_CANTON',
        'DESCRIPCION_SEXO',
        'NOMBRES_DEL_PADRE',
        'FECHA_NACIMIENTO_PADRE',
        'AÑOS_CUMPLIDOS_PADRE',
        'LUGAR_NACIMIENTO_PADRE',
        'NIVEL_ESTUDIOS_PADRE',
        'PROFESION_PADRE',
        'SEXO_PADRE',
        'CELULAR_PADRE_1',
        'CELULAR_PADRE_2',
        'CELULAR_PADRE_3',
        'CELULAR_PADRE_4',
        'CELULAR_PADRE_5',
        'CELULAR_PADRE_6',
        'CELULAR_PADRE_7',
        'CELULAR_PADRE_8',
        'CELULAR_PADRE_9',
        'CELULAR_PADRE_10',
        'CORREO_PADRE_1',
        'CORREO_PADRE_2',
        'CORREO_PADRE_3',
        'CORREO_PADRE_4',
        'CORREO_PADRE_5',
        'CORREO_PADRE_6',
        'CORREO_PADRE_7',
        'CORREO_PADRE_8',
        'CORREO_PADRE_9',
        'CORREO_PADRE_10',
        'NOMBRES_DE_LA_MADRE',
        'FECHA_NACIMIENTO_MADRE',
        'AÑOS_CUMPLIDOS_MADRE',
        'NIVEL_ESTUDIOS_MADRE',
        'PROFESION_MADRE',
        'SEXO_MADRE',
        'CELULAR_MADRE_1',
        'CELULAR_MADRE_2',
        'CELULAR_MADRE_3',
        'CELULAR_MADRE_4',
        'CELULAR_MADRE_5',
        'CELULAR_MADRE_6',
        'CELULAR_MADRE_7',
        'CELULAR_MADRE_8',
        'CELULAR_MADRE_9',
        'CELULAR_MADRE_10',
        'CORREO_MADRE_1',
        'CORREO_MADRE_2',
        'CORREO_MADRE_3',
        'CORREO_MADRE_4',
        'CORREO_MADRE_5',
        'CORREO_MADRE_6',
        'CORREO_MADRE_7',
        'CORREO_MADRE_8',
        'CORREO_MADRE_9',
        'CORREO_MADRE_10'
    ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    ci_p = form['ci_p']

    cursor.execute(
        "CALL reporte_cumpleanios_children_ci('" + ci_p + "')")

    rows = cursor.fetchall()
    list = []
    for row in rows:
        try:
            rowss = [(cipher.decrypt(row[0])),
                     (row[1]),
                     (row[2]),
                     (row[3]),
                     (row[4]),
                     (cipher.decrypt(row[5])),
                     (row[6]),
                     (row[7]),
                     (row[8]),
                     (row[9]),
                     (row[10]),
                     (row[11]),
                     (row[12]),
                     (row[13]),
                     (row[14]),
                     (row[15]),
                     (row[16]),
                     (row[17]),
                     (row[18]),
                     (row[19]),
                     (row[20]),
                     (row[21]),
                     (row[22]),
                     (row[23]),
                     (row[24]),
                     (row[25]),
                     (row[26]),
                     (row[27]),
                     (row[28]),
                     (row[29]),
                     (row[30]),
                     (row[31]),
                     (cipher.decrypt(row[32])),
                     (row[33]),
                     (row[34]),
                     (row[35]),
                     (row[36]),
                     (row[37]),
                     (row[38]),
                     (row[39]),
                     (row[40]),
                     (row[41]),
                     (row[42]),
                     (row[43]),
                     (row[44]),
                     (row[45]),
                     (row[46]),
                     (row[47]),
                     (row[48]),
                     (row[49]),
                     (row[50]),
                     (row[51]),
                     (row[52]),
                     (row[53]),
                     (row[54]),
                     (row[55]),
                     (row[56]),
                     (row[57])]
        except IndexError as e:
            break
        list.append(rowss)
    print(list)
    for row in list:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response
