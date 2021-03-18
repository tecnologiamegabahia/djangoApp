"""planApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include(('apps.usuario.urls', 'usuario'), namespace='usuario')),
    path('roles/', include(('apps.rol.urls', 'rol'), namespace='rol')),
    path("accounts/", include("apps.authentication.urls")),
    path("", include("apps.authentication.urls")),
    path("clientes/", include(("apps.cliente.urls", 'clientes'), namespace='clientes')),
    path("contribuyentes/", include(("apps.contribuyente.urls", 'contribuyentes'), namespace='contribuyentes')),
    path("establecimientos/", include(("apps.establecimiento.urls", 'establecimientos'), namespace='establecimientos')),
    path("representante_legal/",
         include(("apps.representante_legal.urls", 'representante_legal'), namespace='representante_legal')),
    path("ubicaciones_geograficas/",
         include(("apps.ubicacione_geografica.urls", 'ubicaciones_geograficas'), namespace='ubicaciones_geograficas')),
    path("actividades_economicas/",
         include(("apps.actividad_economica.urls", 'actividades_economicas'), namespace='actividades_economicas')),
    path("medios_contacto/",
         include(("apps.medio_contacto.urls", 'medios_contacto'), namespace='medios_contacto')),
    path("tipos_contribuyentes/",
         include(("apps.tipo_contribuyente.urls", 'tipos_contribuyentes'), namespace='tipos_contribuyentes')),
    path("actividad_economica_est/",
         include(("apps.actividad_economica_establecimiento.urls", 'actividad_economica_est'), namespace='actividad_economica_est')),
]

urlpatterns += staticfiles_urlpatterns()
