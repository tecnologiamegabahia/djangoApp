from django.contrib import admin
from django.urls import path
from apps.cliente.views import uploads, verificarArchivos, home, DescargarArchivoView
from django.conf.urls import url, include
from django.views.static import serve
from django.conf import settings
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^$', login_required(uploads), name='upload'),
    url(r'^lista/$', login_required(verificarArchivos), name='lista'),
    url(r'^lista1/$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^download/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^archivo', DescargarArchivoView.as_view(), name='archivo_post'),

]
