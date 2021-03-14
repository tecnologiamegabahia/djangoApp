from django.db import connection
from django.contrib.auth.decorators import login_required
from django.conf import settings


@login_required()
def index_login(request):
    sql = 'SELECT r.permisoAdmin ,' \
          'r.permisoCalidad ,' \
          'r.permisoContactos ,' \
          'r.permisoEstadisticas ,' \
          'r.permisoGestion ,' \
          'r.permisoMonitoreo ,' \
          'r.permisoProcesos ,' \
          'r.permisoReportes ' \
          'FROM usuario_usuario uu join rol_rol r on uu.rol_id = r.id ' \
          'WHERE username = %s'
    cursor = connection.cursor()
    try:
        cursor.execute(sql, request.user)
        results = cursor.fetchone()
        list = []
        model = {}
        i = 0
        for row in results:
            dict = {}
            field = 0

            while True:
                try:
                    dict[cursor.description[i][0]] = str(results[i][field])
                    model = {'permisoAdmin': str(results[0][field]),
                             'permisoCalidad': str(results[1][field]),
                             'permisoContactos': str(results[2][field]),
                             'permisoEstadisticas': str(results[3][field]),
                             'permisoGestion': str(results[4][field]),
                             'permisoMonitoreo': str(results[5][field]),
                             'permisoProcesos': str(results[6][field]),
                             'permisoReportes': str(results[7][field])}

                    field = field + 1
                except IndexError as e:
                    break
            i = i + 1
            list.append(dict)
        return {'row': model}
    except Exception as e:
        cursor.close
