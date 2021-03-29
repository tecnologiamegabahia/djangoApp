from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from django.urls import path
from .views import reporte_cumpleanios_children, index, conteo_cliente, conteo_contribuyentes_naturales, \
    conteo_contribuyentes_juridicos, conteo_empleados, form_view_combo, reporte_negocio, reporte_cumpleanios_children_ci

urlpatterns = [
    url(r'^index$', login_required(index), name='index'),
    url(r'^dowload_report/$', login_required(reporte_cumpleanios_children), name='dowload_report'),
    url(r'^conteo_cliente/$', login_required(conteo_cliente), name='conteo_cliente'),
    url(r'^conteo_contribuyentes/$', login_required(conteo_contribuyentes_naturales), name='conteo_contribuyentes'),
    url(r'^conteo_contribuyentes_juridicos/$', login_required(conteo_contribuyentes_juridicos),
        name='conteo_contribuyentes_juridicos'),
    url(r'^conteo_empleados/$', login_required(conteo_empleados), name='conteo_empleados'),
    path('combo/', form_view_combo.as_view(), name='combo'),
    path('reporte_negocio/', login_required(reporte_negocio), name='reporte_negocio'),
    url(r'^dowload_report_ci/$', login_required(reporte_cumpleanios_children_ci), name='dowload_report_ci'),

]
