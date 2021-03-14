from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from apps.usuario.views import index, usuarios_view, usuarios_list, usuarios_edit, UsuariosList, usuario_delete, \
    indexLogin
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(UsuariosList.as_view()), name='index'),
    url(r'^nuevo$', login_required(usuarios_view), name='usuario_crear'),
    url(r'^editar/(?P<id>\d+)/$', login_required(usuarios_edit), name='usuario_editar'),
    url(r'^eliminar/(?P<id>\d+)/$', login_required(usuario_delete), name='usuario_eliminar'),
    url(r'^dash/$', login_required(indexLogin), name='dashboard'),
]
