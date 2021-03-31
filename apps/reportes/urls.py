from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from django.urls import path
from .views import reporte_cumpleanios_children, index, conteo_cliente, conteo_contribuyentes_naturales, \
    conteo_contribuyentes_juridicos, conteo_empleados, form_view_combo, reporte_negocio, \
    reporte_cumpleanios_children_ci, index_ci, reporte_negocio_ruc, reporte_negocio_ruc_view, reporte_empleados, \
    reporte_empleados_ci, reporte_empleados_busqueda, reporte_empleados_busqueda_ci

urlpatterns = [
    url(r'^index$', login_required(index), name='index'),
    url(r'^index_ci$', login_required(index_ci), name='index_ci'),
    url(r'^dowload_report/$', login_required(reporte_cumpleanios_children), name='dowload_report'),
    url(r'^conteo_cliente/$', login_required(conteo_cliente), name='conteo_cliente'),
    url(r'^conteo_contribuyentes/$', login_required(conteo_contribuyentes_naturales), name='conteo_contribuyentes'),
    url(r'^conteo_contribuyentes_juridicos/$', login_required(conteo_contribuyentes_juridicos),
        name='conteo_contribuyentes_juridicos'),
    url(r'^conteo_empleados/$', login_required(conteo_empleados), name='conteo_empleados'),
    path('reporte_negocio_view/', form_view_combo.as_view(), name='reporte_negocio_view'),
    path('reporte_negocio/', login_required(reporte_negocio), name='reporte_negocio'),
    url(r'^dowload_report_ci/$', login_required(reporte_cumpleanios_children_ci), name='dowload_report_ci'),
    path('reporte_negocio_ruc/', login_required(reporte_negocio_ruc), name='reporte_negocio_ruc'),
    path('reporte_negocio_ruc_view/', login_required(reporte_negocio_ruc_view), name='reporte_negocio_ruc_view'),
    path('reporte_empleados_ci/', login_required(reporte_empleados_ci), name='reporte_empleados_ci'),
    path('reporte_empleados/', login_required(reporte_empleados), name='reporte_empleados'),
    path('reporte_empleados_busqueda/', login_required(reporte_empleados_busqueda), name='reporte_empleados_busqueda'),
    path('reporte_empleados_busqueda_ci/', login_required(reporte_empleados_busqueda_ci),
         name='reporte_empleados_busqueda_ci'),

]
