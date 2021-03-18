from apps.tipo_contribuyente.views import uploads, verificarArchivos, DescargarArchivoView
from django.conf.urls import url

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
